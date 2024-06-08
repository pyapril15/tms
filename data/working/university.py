from PySide6.QtWidgets import QDialog

from data.database.db_query import Query
from data.ui.add_university import Ui_Dialog as AddUniversityDialog
from data.working.common import Common


class UniversityDialog(QDialog, AddUniversityDialog):
    """Dialog for adding or updating university details."""

    def __init__(self, parent=None, use_type="add", university_code=None,
                 university_short_name=None, university_name=None):
        """Initialize the dialog.

        Args:
            parent: Optional parent widget.
            use_type: Type of usage, either 'add' or 'update'.
            university_code: The code of the university.
            university_short_name: The short name of the university.
            university_name: The full name of the university.
        """
        super().__init__(parent)

        self._use_type = use_type
        self._university_code = university_code
        self._university_short_name = university_short_name
        self._university_name = university_name
        self._short_name = ""

    def ui(self):
        """Set up the UI elements and connect signals."""
        self.setupUi(self)
        self.setWindowTitle("Add University")
        self.auSubmitBtn.clicked.connect(self._submit)
        self.auUniversityName.textChanged.connect(self._update_short_name)
        self.auUniversityCode.textChanged.connect(self._update_short_name)

    def set_values(self):
        """Set initial values for university details."""
        self.auUniversityName.setText(self._university_name)
        self.auUniversityCode.setText(self._university_code)
        self.auUniversityShortName.setText(self._university_short_name)

    def _update_short_name(self):
        """Update short name based on university name and code."""
        name = ""
        text = self.auUniversityName.text()
        try:
            for word in text.split(' '):
                if 'of' not in word:
                    name += word[0].upper()
        except IndexError:
            pass
        self._short_name = name + self.auUniversityCode.text()
        self.auUniversityShortName.setText(self._short_name)

    def _submit(self):
        """Handle submission of university details."""
        university_name = self.auUniversityName.text().capitalize()
        university_code = self.auUniversityCode.text().upper()
        university_short_name = self.auUniversityShortName.text().upper()

        if not university_name:
            Common.show_message("University Name is empty!.")
            return
        if not university_code:
            Common.show_message("University Code is empty!.")
            return
        if not university_short_name:
            Common.show_message("University short code is empty!.")
            return

        query = Query()
        try:
            if self._use_type == "add":
                success = query.insert_university_detail((university_name, university_code, university_short_name))
                if success:
                    Common.show_message("University added successfully!", "I")
                    self._clear_fields()
                    self.close()

            elif self._use_type == "update":
                success = query.update_university_detail(
                    (university_name, university_code, university_short_name, self._university_code))
                if success:
                    Common.show_message("Update successful!", "I")
                    self._clear_fields()
                    self.close()
        except Exception as e:
            Common.show_message(f"An error occurred: {str(e)}", "C")

    def _clear_fields(self):
        """Clear all input fields."""
        self.auUniversityName.clear()
        self.auUniversityCode.clear()
        self.auUniversityShortName.clear()
