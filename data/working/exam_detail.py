from PySide6.QtWidgets import QDialog

from data.database.db_query import Query
from data.ui.exam_detail import Ui_Dialog as AddExamDetailDialog
from data.working.common import Common


class ExamDetailDialog(QDialog, AddExamDetailDialog):
    """Dialog window for adding or updating exam details."""

    def __init__(self, parent=None, use_type="add", usn=None, csn=None, semester=None, center=None, shift=None,
                 exam_date=None):
        """
        Initialize the ExamDetailDialog.

        Args:
            parent (QWidget, optional): Parent widget. Defaults to None.
            use_type (str, optional): Type of usage ("add" or "update"). Defaults to "add".
            usn (str, optional): University short name. Defaults to None.
            csn (str, optional): Course short name. Defaults to None.
            semester (str, optional): Semester. Defaults to None.
            center (str, optional): Center name. Defaults to None.
            shift (str, optional): Shift. Defaults to None.
            exam_date (list of tuples, optional): Exam dates. Defaults to None.
        """
        super().__init__(parent)
        self._query = Query("exam_detail")

        self._use_type = use_type
        self._university_short_name = usn
        self._course_short_name = csn
        self._semester = semester
        self._center = center
        self._shift = shift
        self._exam_date = exam_date

    def ui(self):
        """Set up the UI elements."""
        self.setupUi(self)
        self.setWindowTitle("Exam Detail")
        self.aEDAddBtn.clicked.connect(self._submit)
        self._add_values()

    def _add_values(self):
        """Populate combo boxes with provided values."""
        if self._university_short_name:
            self.aEDUniversity.addItem(self._university_short_name)
        if self._course_short_name:
            self.aEDCourse.addItem(self._course_short_name)
        if self._semester:
            self.aEDSemester.addItem(self._semester)

    def add_center_in_combobox(self):
        """Populate the center combo box with center names from the database."""
        self.aEDCenter.clear()  # Clear existing items
        center_names = self._query.get_center_name_from_transport_fee()
        if center_names:
            self.aEDCenter.addItems([item[0] for item in center_names])

    def _submit(self):
        """Handle submission of exam details."""
        university_short_name = self.aEDUniversity.currentText()
        course_short_name = self.aEDCourse.currentText()
        semester = self.aEDSemester.currentText()
        center_name = self.aEDCenter.currentText()
        shift = self.aEDShift.currentText()

        # Input validation
        if not all([university_short_name, course_short_name, semester, center_name, shift]):
            Common.show_message("All fields are required.")
            return

        try:
            if self._use_type == "add":
                value = (university_short_name, course_short_name, semester, center_name, shift)
                success = self._query.insert_exam_detail(value)
                if success:
                    Common.show_message("Exam detail added successfully!", "I")
                    self._clear_fields()
                    self.close()

            elif self._use_type == "update":
                exam_detail = (center_name, shift, self._university_short_name, self._course_short_name, self._semester)
                if self._exam_date[0][0] == 'None':
                    if self._query.update_exam_detail(exam_detail):
                        Common.show_message("Exam detail Update successfully!", "I")
                        self._clear_fields()
                        self.close()
                else:
                    if self._center is not None and self._shift is not None and self._exam_date is not None:
                        exam_journey = [(center_name, shift, self._center, item[0], self._shift) for item in
                                        self._exam_date]
                        if self._query.update_exam_detail_and_exam_journey(exam_detail, exam_journey):
                            Common.show_message("Both Exam detail and Journey Update successfully!", "I")
                            self._clear_fields()
                            self.close()

        except Exception as e:
            Common.show_message(f"An error occurred: {str(e)}", "C")

    def _clear_fields(self):
        """Clear all combo box selections."""
        self.aEDUniversity.setCurrentIndex(0)
        self.aEDCourse.setCurrentIndex(0)
        self.aEDSemester.setCurrentIndex(0)
        self.aEDCenter.setCurrentIndex(0)
