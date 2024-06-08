from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDialog, QDateEdit, QTableWidgetItem

from data.database.db_query import Query
from data.ui.dateSheet import Ui_Form as DateSheetForm
from data.working.common import Common


class DateSheetDialog(QDialog, DateSheetForm):
    """Dialog for managing date sheets for exams."""

    def __init__(self, parent=None, usn=None, csn=None, semester=None, subject_date=None, place=None, shift=None):
        """
        Initialize the DateSheetDialog.

        Args:
            parent: Parent widget.
            usn (str): University short name.
            csn (str): Course short name.
            semester (str): Semester.
            subject_date (list of tuples): Subject dates.
            place (str): Exam center.
            shift (str): Exam shift.
        """
        super().__init__(parent)

        self._query = Query()

        self._university_short_name = usn
        self._course_short_name = csn
        self._semester = semester
        self._subject_date = subject_date
        self._center = place
        self._shift = shift

    def ui(self):
        """Set up the UI."""
        self.setupUi(self)
        self.setWindowTitle("DateSheet")
        self._set_values_in_combobox()
        self._refresh_date_sheet_view()
        self.dateSheetSubmitBtn.clicked.connect(self._submit)

    def _set_values_in_combobox(self):
        """Set values in combobox."""
        self.dUniversity.setText(self._university_short_name)
        self.dCourse.setText(self._course_short_name)
        self.dSemester.setText(self._semester)

    def _get_date_sheet_table_data(self):
        """
        Get data from the date sheet table.

        Returns:
            list: List of data from the table.
        """
        data = []
        for row in range(self.dateSheetTable.rowCount()):
            row_data = []
            for column in range(self.dateSheetTable.columnCount()):
                item = self.dateSheetTable.item(row, column)
                if isinstance(item, QTableWidgetItem):
                    row_data.append(item.text())
                else:
                    widget = self.dateSheetTable.cellWidget(row, column)
                    if isinstance(widget, QDateEdit):
                        row_data.append(widget.date().toString('yyyy-MM-dd'))
            data.append(row_data)
        return data

    def _refresh_date_sheet_view(self):
        """Refresh the date sheet view."""
        if self._subject_date:
            self._populate_date_sheet_table()

    def _populate_date_sheet_table(self):
        """Populate the date sheet table."""
        self.dateSheetTable.setRowCount(len(self._subject_date))
        for row, subject_date in enumerate(self._subject_date):
            self._populate_date_sheet_row(row, subject_date)

    def _populate_date_sheet_row(self, row: int, date_sheet: tuple):
        """
        Populate a row in the date sheet table.

        Args:
            row (int): Row index.
            date_sheet (tuple): Date sheet data.
        """
        try:
            for col, value in enumerate(date_sheet):
                if col == 0:
                    item = QTableWidgetItem(str(value))
                    self.dateSheetTable.setItem(row, col, item)
                if col == 1:
                    date_edit = QDateEdit()
                    date_edit.setCalendarPopup(True)
                    date_edit.setDisplayFormat("yyyy-MM-dd")
                    date_edit.setDate(QDate.currentDate())
                    if value is not None:
                        date_edit.setDate(QDate(value.year, value.month, value.day))
                    self.dateSheetTable.setCellWidget(row, col, date_edit)
        except Exception as e:
            Common.show_message(f"Error populating date sheet row:- {str(e)}", "C")
        finally:
            self.dateSheetTable.resizeColumnsToContents()
            self.dateSheetTable.resizeRowsToContents()

    def _read_date_for_exam(self, value: tuple):
        """
        Read date for exam from the database.

        Args:
            value (tuple): Query parameters.

        Returns:
            tuple: Exam date data.
        """
        read_allotment = self._query.get_subject_exam_date(value)
        if read_allotment:
            return read_allotment
        return

    def _save_exam_journey_detail(self, value: list):
        """
        Save exam journey detail to the database.

        Args:
            value (list): List of journey details.

        Returns:
            bool: True if successful, False otherwise.
        """
        success = self._query.insert_exam_journey_detail(value)
        if success:
            return True
        return False

    def _submit(self):
        """Handle submission."""
        try:
            value = (self._university_short_name, self._course_short_name, self._semester)
            # First, retrieve current data to decide on the update or insert
            exam_date_existing = self._read_date_for_exam(value)

            # Extract table data from UI
            date_sheet_table_data = self._get_date_sheet_table_data()

            # Prepare data for updates or inserts
            exam_dates_to_process = [
                (item[1], self._university_short_name, self._course_short_name, self._semester, item[0]) for item in
                date_sheet_table_data]

            # Decide based on existing data
            if exam_date_existing is None:
                self._handle_inserts(date_sheet_table_data, exam_dates_to_process)
            else:
                self._handle_updates(date_sheet_table_data, exam_dates_to_process, exam_date_existing)

        except Exception as e:
            Common.show_message(f"Error during submission: {str(e)}", "C")

    def _handle_inserts(self, date_sheet_table_data, exam_dates_to_process):
        """Handle inserts."""
        try:
            journey_details = [(self._center, item[1], self._shift, "exam") for item in date_sheet_table_data]
            success = self._query.update_exam_date_create_exam_journey(exam_dates_to_process, journey_details)
            if success:
                Common.show_message("Date sheet and Journey Created Successfully!", "I")
                self.update_journey_id_allotment(date_sheet_table_data)
        except Exception as e:
            Common.show_message(f"Error handling Inserting: {str(e)}", "C")

    def _handle_updates(self, date_sheet_table_data: list, exam_dates_to_process, exam_date_existing):
        """Handle updates."""
        try:
            journey_updates = []
            for i, item in enumerate(date_sheet_table_data):
                journey_updates.append((item[1], self._center, exam_date_existing[i][0], self._shift))

            success = self._query.update_exam_date_update_exam_journey(exam_dates_to_process, journey_updates)
            if success:
                Common.show_message("Date sheet and Journey Updated Successfully!", "I")
        except Exception as e:
            Common.show_message(f"Error handling updates: {str(e)}", "C")

    def update_journey_id_allotment(self, date_sheet_table_data: list):
        try:
            value = (self._university_short_name, self._course_short_name, self._semester)
            center_name_shift = self._query.get_center_name_shift_from_exam_detail(value)
            list_of_exam_date = [i[1] for i in date_sheet_table_data]
            tuple_of_exam_date = tuple(list_of_exam_date)
            journey = [(center_name_shift[0], i, center_name_shift[1]) for i in tuple_of_exam_date]

            journey_id = []
            for i in journey:
                success = self._query.get_journey_id(i)
                if success:
                    journey_id.append(success[0])

            journey_id_allotment = [(journey_id[i], self._university_short_name, self._course_short_name, self._semester, date_sheet_table_data[i][0]) for i in range(len(date_sheet_table_data))]
            self._query.update_journey_id_allotment(journey_id_allotment)
        except Exception as e:
            Common.show_message(f"Error in update journey_id in allotment:-\n{str(e)}", "C")


