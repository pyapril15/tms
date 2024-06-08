from PySide6.QtCore import QTimer, QStringListModel, Qt, QItemSelection
from PySide6.QtGui import QIntValidator, QFont
from PySide6.QtWidgets import QCompleter, QDialog, QTableWidgetItem

from data.database.db_query import Query
from data.ui.ui_book_transport import Ui_Dialog as BookTransportDialog
from data.working.common import Common


class BookTransportUI(QDialog, BookTransportDialog):
    """
    Class representing the UI for booking transport.

    Inherits from QDialog and Ui_Dialog.

    Attributes:
        _query (Query): Instance of the Query class for database queries.
        _center (str): Center for the exam.
        _fee (int): Fee for transport.
        roll_no (int): Roll number of the student.
        _fee_status (str): Status of the fee payment.
        _fee_receipt_no (int): Receipt number for the fee.
        _already_paid (int): Amount already paid.
        count (int): Counter for fee payments.
        _already_paid_fee_journey_id (list): List of journey IDs for already paid fees.
        _completer (QCompleter): Completer for roll number input.
        _timer (QTimer): Timer for roll number search timeout.
    """

    def __init__(self, parent=None):
        """
        Initialize the BookTransportUI class.

        Args:
            parent: Parent widget (default is None).
        """
        try:
            super().__init__(parent)
            self.setupUi(self)
            self.setWindowTitle("Book Transport")

            self._query = Query()
            self._center = None
            self._fee = 0
            self.roll_no = 0
            self._fee_status = None
            self._fee_receipt_no = 0
            self._already_paid = 0
            self.count = 0
            self._already_paid_fee_journey_id = []

            self._completer = QCompleter()

            self._timer = QTimer()
            self._timer.setSingleShot(True)
            self._timer.timeout.connect(self.timeout)
        except Exception as e:
            pass

    def init_ui(self):
        """
        Initialize the UI components.
        """
        self._completer.setCompletionMode(QCompleter.PopupCompletion)
        self._completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.bTRollNumber.setCompleter(self._completer)
        self._completer.activated.connect(self.handle_completer_selection)

        self.bTAmount.setValidator(QIntValidator())
        self.bTViewTable.selectionModel().selectionChanged.connect(self.on_selection_changed)
        self.bTRollNumber.textChanged.connect(self.search_roll_no)
        self.bTSearchBtn.clicked.connect(self.search_by_button)
        self.bTSubmitBtn.clicked.connect(self.submit)

        self.set_completer_popup_style()

    def set_completer_popup_style(self):
        """
        Set the style for the completer popup.
        """
        completer_popup = self._completer.popup()
        completer_popup.setStyleSheet("""
            QListView {
                color: #333;
                background-color: #fff;
                border: 1px solid #aaa;
                border-radius: 4px;
                outline: none;
            }
            QListView::item {
                padding: 5px 10px;
                border-bottom: 1px solid #f0f0f0;
            }
            QListView::item:selected {
                background-color: #0057D9;
                color: #ffffff;
            }
            QListView::item:hover {
                background-color: #f7f7f7;
            }
            QScrollBar:vertical {
                border: none;
                background: #f0f0f0;
                width: 10px;
                margin: 10px 0 10px 0;
            }
            QScrollBar::handle:vertical {
                background: #b0b0b0;
                min-height: 20px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
                height: 0;
            }
        """)
        completer_popup.setFont(QFont("Segoe UI", 10, QFont.Bold))
        completer_popup.setMinimumHeight(100)
        completer_popup.setMaximumWidth(300)
        completer_popup.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        completer_popup.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

    def timeout(self):
        """
        Handle timeout for roll number search.
        """
        try:
            roll_no = self.bTRollNumber.text().strip()

            if len(roll_no) < 2:
                self._completer.setModel(QStringListModel([]))
                return

            pattern = (f"{roll_no}%",)
            similar_roll_numbers = self._query.get_similar_roll_no(pattern)

            if similar_roll_numbers:
                rolls = [row[0] for row in similar_roll_numbers]
                self._completer.setModel(QStringListModel(rolls))
            else:
                self._completer.setModel(QStringListModel([]))
                self.clear()
        except Exception as e:
            pass

    def search_roll_no(self):
        """
        Search for roll number.
        """
        try:
            self._timer.start(500)
        except Exception as e:
            pass

    def select_row(self, journey_ids: list):
        """
        Select row based on journey IDs.

        Args:
            journey_ids (list): List of journey IDs.
        """
        try:
            self._already_paid_fee_journey_id.clear()
            for row in range(self.bTViewTable.rowCount()):
                for journey_id in journey_ids:
                    if self.bTViewTable.item(row, 0).text() == str(journey_id[0]):
                        self._already_paid_fee_journey_id.append(journey_id[0])
                        self.bTViewTable.selectRow(row)
                        self.count += 1
        except Exception as e:
            pass

    def search_by_button(self):
        """
        Search roll number by button click.
        """
        try:
            self.handle_completer_selection(self.bTRollNumber.text())
        except Exception as e:
            pass

    def handle_completer_selection(self, text):
        """
        Handle selection from completer.

        Args:
            text (str): Text from completer.
        """
        try:
            roll = text.strip()
            self.bTRollNumber.setText(roll)
            self.roll_no = roll
            if roll:
                student_detail = self._query.get_student_detail_of_roll_no(roll)
                if student_detail:
                    self.set_student_data(student_detail)
                    self.handle_fee_already_paid(self.roll_no)
                else:
                    self.clear()
            else:
                self.clear()
        except Exception as e:
            pass

    def set_student_data(self, data: tuple):
        """
        Set student data.

        Args:
            data (tuple): Tuple containing student data.
        """
        try:
            if data:
                self.bTStudentName.setText(data[1])
                self.bTGardianName.setText(data[2])
                self.bTMobileNumber.setText(data[3])
                self.bTUniversity.setText(data[4])
                self.bTCourse.setText(data[5])
                self.bTSemester.setText(str(data[6]))
                self.refresh_exam_date_view(data[4], data[5], str(data[6]))
        except Exception as e:
            pass

    def refresh_exam_date_view(self, university_short_name: str, course_short_name: str, semester: str):
        """
        Refresh the exam date view.

        Args:
            university_short_name (str): Short name of the university.
            course_short_name (str): Short name of the course.
            semester (str): Semester.
        """
        try:
            self.clear_selections()
            if university_short_name and course_short_name and semester:
                is_exam_active = self._query.get_is_active_from_exam_detail(
                    (university_short_name, course_short_name, semester))
                if is_exam_active and is_exam_active[0]:
                    read_exam = self.read_exam_data_sheet(university_short_name, course_short_name, semester)
                    read_center = self.read_exam_center(university_short_name, course_short_name, semester)
                    if read_exam and read_center:
                        self._center = read_center[0]
                        self.read_transport_fee()
                        self.populate_exam_date_table(read_exam)
        except Exception as e:
            Common.show_message("Error in refreshing exam date:-\n" + str(e), "C")

    def populate_exam_date_table(self, exams: list):
        """
        Populate exam date table.

        Args:
            exams (list): List of exams.
        """
        try:
            self.bTViewTable.setRowCount(len(exams))
            for row, exam in enumerate(exams):
                self.populate_exam_date_row(row, exam)
                self.bTViewTable.setItem(row, 4, QTableWidgetItem(str(self._center)))
        except Exception as e:
            pass

    def populate_exam_date_row(self, row, exam: tuple):
        """
        Populate exam date row.

        Args:
            row: Row index.
            exam (tuple): Exam data.
        """
        try:
            for col, value in enumerate(exam):
                item = QTableWidgetItem(str(value))
                self.bTViewTable.setItem(row, col, item)
        except Exception as e:
            pass

    def read_exam_data_sheet(self, university_short_name: str, course_short_name: str, semester: str):
        """
        Read exam data sheet.

        Args:
            university_short_name (str): Short name of the university.
            course_short_name (str): Short name of the course.
            semester (str): Semester.

        Returns:
            list: List of exam data.
        """
        try:
            value = (university_short_name, course_short_name, semester)
            return self._query.get_j_id_subject_code_subject_name_exam_date(value)
        except Exception as e:
            pass

    def read_exam_center(self, university_short_name: str, course_short_name: str, semester: str):
        """
        Read exam center.

        Args:
            university_short_name (str): Short name of the university.
            course_short_name (str): Short name of the course.
            semester (str): Semester.

        Returns:
            str: Exam center.
        """
        try:
            if university_short_name and course_short_name and semester:
                value = (university_short_name, course_short_name, semester)
                return self._query.get_exam_center_from_exam_detail(value)
        except Exception as e:
            pass

    def read_transport_fee(self):
        """
        Read transport fee.
        """
        try:
            if self._center:
                success = self._query.get_transport_fee(self._center)
                if success:
                    self._fee = success[0]
        except Exception as e:
            pass

    def clear_selections(self):
        """
        Clear selections.
        """
        try:
            self.bTViewTable.clearSelection()
            self.bTViewTable.selectionModel().clearCurrentIndex()
        except Exception as e:
            pass

    def on_selection_changed(self, selected, deselected):
        """
        Handle selection change.

        Args:
            selected: Selected item.
            deselected: Deselected item.
        """
        try:
            price = int(self.bTAmount.text())

            if selected:
                self.bTAmount.setText(str(price + self._fee))
                if isinstance(selected, QItemSelection):
                    for i in selected.indexes():
                        j_id = self.bTViewTable.item(i.row(), 0).text()
                        if int(j_id) in self._already_paid_fee_journey_id:
                            self.bTAmount.setText(str(price + self._already_paid))
                        else:
                            self.bTAmount.setText(str(price + self._fee))
                        break

            elif deselected:
                if isinstance(deselected, QItemSelection):
                    for i in deselected.indexes():
                        j_id = self.bTViewTable.item(i.row(), 0).text()
                        if int(j_id) in self._already_paid_fee_journey_id:
                            self.bTAmount.setText(str(price - self._already_paid))
                        else:
                            self.bTAmount.setText(str(price - self._fee))
                        break

        except Exception as e:
            pass

    def read_fee_detail(self, roll_no: str):
        """
        Read fee detail.

        Args:
            roll_no (str): Roll number.
        """
        try:
            fee_detail = self._query.get_amount_mode_roll_no(roll_no)
            if fee_detail:
                for value in fee_detail:
                    self.bTAmount.setText(str(value[0]))
                    self._already_paid = int(int(value[0]) / self.count)
                    self.bTModeOfPayment.setCurrentText(str(value[1]))
        except Exception as e:
            pass

    def handle_fee_already_paid(self, roll_no: str):
        """
        Handle already paid fee.

        Args:
            roll_no (str): Roll number.
        """
        try:
            journey_ids = self._query.get_fee_journey_id_roll_no(roll_no)
            if journey_ids:
                self.select_row(journey_ids)
                self._fee_receipt_no = self._query.get_fee_receipt_no_roll_no(roll_no)[0]
                self._already_paid = int(int(self.bTAmount.text()) / self.count)
                self._fee_status = "paid"
            else:
                return

            self.read_fee_detail(roll_no)
        except Exception as e:
            pass

    def submit(self):
        """
        Submit fee details.
        """
        try:
            roll_no = self.bTRollNumber.text()
            student_name = self.bTStudentName.text()
            guardian_name = self.bTGardianName.text()
            mobile_number = self.bTMobileNumber.text()
            university_short_name = self.bTUniversity.text()
            course_short_name = self.bTCourse.text()
            semester = self.bTSemester.text()
            amount = self.bTAmount.text()
            mode = self.bTModeOfPayment.currentText()
            selected_exam_data = Common().get_selected_row_specific_column_data(self.bTViewTable, column=0)

            if not all([roll_no, student_name, guardian_name, mobile_number, university_short_name, course_short_name,
                        semester]):
                Common.show_message("Fill all the input")
                return

            if amount == '0':
                Common.show_message("Amount is Zero")
                return

            if mode == "Mode of Payment":
                Common.show_message("Select mode of payment!.")
                return

            if self._fee_status == "paid":
                self._query.delete_fee_journey_and_fee_detail(str(self._fee_receipt_no))

            success = self._query.insert_fee_detail_and_fee_journey((self.roll_no, amount, mode), selected_exam_data)
            if success:
                Common.show_message("Fee Add successfully!", "I")
                self.clear()
            else:
                Common.show_message("Failed to add fee detail. Please try again.", "C")
        except Exception as e:
            Common.show_message("Error in submitting" + str(e), "C")

    def clear(self):
        """
        Clear all input fields.
        """
        try:
            self.bTStudentName.setText("")
            self.bTGardianName.setText("")
            self.bTMobileNumber.setText("")
            self.bTUniversity.setText("")
            self.bTCourse.setText("")
            self.bTSemester.setText("")
            self.bTViewTable.setRowCount(0)
            self.bTAmount.setText("0")
            self._center = None
            self._fee = 0
        except Exception as e:
            pass
