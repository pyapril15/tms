from PySide6.QtWidgets import QDialog

from data.database.db_query import Query
from data.working.common import Common
from data.ui.add_allotment import Ui_Dialog as AddAllotmentDialog


class AllotmentDialog(QDialog, AddAllotmentDialog):
    """Dialog for adding or updating Subject Allotment details."""

    def __init__(self, parent=None, use_type="add", usn=None, csn=None, semester=None, subject_name=None):
        """Initialize the dialog.

        Args:
            parent (QWidget, optional): Parent widget. Defaults to None.
            use_type (str, optional): Type of operation (add or update). Defaults to "add".
            usn (str, optional): University short name. Defaults to None.
            csn (str, optional): Course short name. Defaults to None.
            semester (str, optional): Semester. Defaults to None.
            subject_name (str, optional): Subject name. Defaults to None.
        """
        super().__init__(parent)
        self.query = Query()
        self._use_type = use_type
        self._university_short_name = usn
        self._course_short_name = csn
        self._semester = semester
        self._subject_name = subject_name

    def ui(self):
        """Set up the UI elements and connect signals."""
        self.setupUi(self)
        self.setWindowTitle("Allotment")
        self.aAAddBtn.clicked.connect(self._submit)

    def populate_value_in_combobox(self):
        """Populate values in combo boxes."""
        self.aAUniversity.addItem(self._university_short_name)
        self.aACourse.addItem(self._course_short_name)
        self.aASemester.addItem(self._semester)
        self.aASubject.addItem(self._subject_name)

    def populate_subject_combo_box(self):
        """Populate subject combo box."""
        if self.aASubject.count() != 1:
            c = self.aASubject.count()
            for i in range(1, c):
                self.aASubject.removeItem(1)

        if self.aASubject.count() == 1:
            subject_name = self.query.get_subject_name_from_subject()
            if subject_name is not None:
                for i in subject_name:
                    self.aASubject.addItem(i[0])

    def _submit(self):
        """Handle submission of subject allotment details."""
        university_short_name = self.aAUniversity.currentText()
        course_short_name = self.aACourse.currentText()
        semester = self.aASemester.currentText()
        subject_name = self.aASubject.currentText()

        if not all([university_short_name, course_short_name, semester, subject_name]):
            Common.show_message("Please fill all fields.")
            return

        subject_code = self.query.get_subject_code_of_subject_name_from_subject(subject_name)
        if not subject_code:
            Common.show_message("Subject code not found.")
            return

        if self._use_type == "add":
            value = (university_short_name, course_short_name, semester, subject_code[0], subject_name)
            success = self.query.insert_allotment_detail(value)
            if success:
                Common.show_message("Added successfully!", "I")
        elif self._use_type == "update":
            value = (
                subject_code[0], subject_name, self._university_short_name, self._course_short_name, self._subject_name)
            success = self.query.update_allotment_detail(value)
            if success:
                Common.show_message("Updated successfully!", "I")
            if success:
                self.clear_fields()

    def clear_fields(self):
        """Clear all input fields."""
        self.aAUniversity.setCurrentIndex(0)
        self.aACourse.setCurrentIndex(0)
        self.aASemester.setCurrentIndex(0)
        self.aASubject.setCurrentIndex(0)
