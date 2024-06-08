from PySide6.QtWidgets import QDialog

from data.database.db_query import Query
from data.ui.add_subject import Ui_Dialog as AddSubjectDialog
from data.working.common import Common


class SubjectDialog(QDialog, AddSubjectDialog):
    """Dialog for adding or updating Subject details."""

    def __init__(self, parent=None, use_type="add", subject_code=None, subject_name=None):
        """Initialize the dialog.

        Args:
            parent: The parent widget (default is None).
            use_type (str): The type of operation - "add" or "update" (default is "add").
            subject_code (str): The subject code (default is None).
            subject_name (str): The subject name (default is None).
        """
        super().__init__(parent)

        self._use_type = use_type
        self._subject_code = subject_code
        self._subject_name = subject_name

    def ui(self):
        """Set up the UI elements and connect signals."""
        self.setupUi(self)
        self.setWindowTitle("Add Subject")
        self.asAddBtn.clicked.connect(self._submit)

    def set_values(self):
        """Set initial values for subject code and name."""
        self.asSubjectName.setText(self._subject_name)
        self.asSubjectCode.setText(self._subject_code)

    def _submit(self):
        """Handle submission of Subject details."""
        subject_name = self.asSubjectName.text()
        subject_code = self.asSubjectCode.text()
        if not subject_name:
            Common.show_message("Subject Name is empty!.")
            return
        if not subject_code:
            Common.show_message("Subject Code is empty!.")
            return

        query = Query()
        try:
            if self._use_type == "add":
                success = query.insert_subject_detail((subject_name, subject_code))
                if success:
                    Common.show_message("Subject added successfully!", "I")
                    self._clear_fields()
                    self.close()

            elif self._use_type == "update":
                success = query.update_subject_detail((subject_name, subject_code, self._subject_code))
                if success:
                    Common.show_message("Update successful!", "I")
                    self._clear_fields()
                    self.close()
        except Exception as e:
            Common.show_message(f"An error occurred: {str(e)}", "C")

    def _clear_fields(self):
        """Clear all input fields."""
        self.asSubjectName.clear()
        self.asSubjectCode.clear()
