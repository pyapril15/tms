from PySide6.QtWidgets import QDialog

from data.database.db_query import Query
from data.ui.add_course import Ui_Dialog as AddCourseDialog
from data.working.common import Common


class CourseDialog(QDialog, AddCourseDialog):
    """Dialog for adding or updating Course details."""

    def __init__(self, parent=None, use_type="add", course_code=None, course_short_name=None, course_name=None,
                 year=None):
        """Initialize the dialog.

        Args:
            parent (QWidget): The parent widget of the dialog.
            use_type (str): Indicates whether the dialog is used for adding or updating a course.
            course_code (str): The code of the course.
            course_short_name (str): The short name of the course.
            course_name (str): The name of the course.
            year (str): The year of the course.
        """
        super().__init__(parent)

        self._use_type = use_type
        self._course_code = course_code
        self._course_short_name = course_short_name
        self._course_name = course_name
        self._year = year
        self._short_name = ""

    def ui(self):
        """Set up the UI elements and connect signals."""
        self.setupUi(self)
        self.setWindowTitle("Add Course")
        self.acAddBtn.clicked.connect(self._submit)
        self.acCourseName.textChanged.connect(self._update_short_name)
        self.acCourseCode.textChanged.connect(self._update_short_name)

    def set_values(self):
        """Set initial values for course details."""
        self.acCourseName.setText(self._course_name)
        self.acCourseCode.setText(self._course_code)
        self.acCourseShortName.setText(self._course_short_name)
        self.acCourseYear.setText(self._year)

    def _update_short_name(self):
        """Update short name based on course name and code."""
        name = ""
        text = self.acCourseName.text()
        try:
            for word in text.split(' '):
                if 'of' not in word:
                    name += word[0].upper()
        except IndexError:
            pass
        self._short_name = name + self.acCourseCode.text()
        self.acCourseShortName.setText(self._short_name)

    def _submit(self):
        """Handle submission of Course details."""
        course_name = self.acCourseName.text().capitalize()
        course_code = self.acCourseCode.text().upper()
        course_short_name = self.acCourseShortName.text().upper()
        course_year = self.acCourseYear.text()
        if not course_name:
            Common.show_message("Course Name is empty!.")
            return
        if not course_code:
            Common.show_message("Course Code is empty!.")
            return
        if not course_short_name:
            Common.show_message("Course short code is empty!.")
            return

        if not course_year:
            Common.show_message("Course year is empty!.")
            return

        query = Query()
        try:
            if self._use_type == "add":
                success = query.insert_course_detail((course_name, course_code, course_short_name, course_year))
                if success:
                    Common.show_message("Course added successfully!", "I")
                    self._clear_fields()
                    self.close()

            elif self._use_type == "update":
                success = query.update_course_detail(
                    (course_name, course_code, course_short_name, course_year, self._course_code))
                if success:
                    Common.show_message("Update successful!", "I")
                    self._clear_fields()
                    self.close()
        except Exception as e:
            Common.show_message(f"An error occurred: {str(e)}", "C")

    def _clear_fields(self):
        """Clear all input fields."""
        self.acCourseName.clear()
        self.acCourseCode.clear()
        self.acCourseShortName.clear()
        self.acCourseYear.clear()
