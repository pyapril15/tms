from PySide6.QtWidgets import QDialog

from data.database.db_query import Query
from data.ui.addStudent import Ui_Dialog as AddStudentDialog
from data.working.common import Common


class StudentDialog(QDialog, AddStudentDialog):
    """
    Dialog for adding or updating student details.

    Args:
        parent: Parent widget.
        use_type (str): Either "add" or "update" indicating the mode of the dialog.
        roll_no (str): Roll number of the student (only applicable for updates).
    """

    def __init__(self, parent=None, use_type="add", roll_no=None):
        super().__init__(parent)
        self._query = Query("student")
        self._roll_no = roll_no
        self._use_type = use_type

    def ui(self):
        """
        Sets up the user interface elements and connects signals to slots.
        """
        self.setupUi(self)
        self.setWindowTitle("Student Detail")
        self._add_in_student_combobox()
        self.aSCourse.currentIndexChanged.connect(self._selection_change_course)
        self.aSAddBtn.clicked.connect(self._submit)

    def set_values(self, student_name: str, guardian_name: str, mobile_no: str, university_short_name: str,
                   course_short_name: str, semester: str):
        """
        Sets initial values for the student details in the dialog.

        Args:
            student_name (str): Student's name.
            guardian_name (str): Guardian's name.
            mobile_no (str): Student's mobile number.
            university_short_name (str): Short name of the university.
            course_short_name (str): Short name of the course.
            semester (str): Semester of the student.
        """
        self.aSRollNumber.setText(self._roll_no)
        self.aSStudentName.setText(student_name)
        self.aSGuardianName.setText(guardian_name)
        self.aSSMobileNumber.setText(mobile_no)
        self.aSUniversity.setCurrentText(university_short_name)
        self.aSCourse.setCurrentText(course_short_name)
        self.aSSemester.setCurrentText(semester)

    def _add_in_student_combobox(self):
        """
        Populates combo boxes for selecting university, course, and semester.
        """
        if self.aSUniversity.count() != 1:
            c = self.aSUniversity.count()
            for i in range(1, c):
                self.aSUniversity.removeItem(1)

        if self.aSCourse.count() != 1:
            c = self.aSCourse.count()
            for i in range(1, c):
                self.aSCourse.removeItem(1)

        if self.aSSemester.count() != 1:
            c = self.aSSemester.count()
            for i in range(1, c):
                self.aSSemester.removeItem(1)

        if self.aSUniversity.count() == 1:
            university_short_name = self._query.get_university_short_name()
            if university_short_name:
                for i in university_short_name:
                    self.aSUniversity.addItem(i[0])

        if self.aSCourse.count() == 1:
            course_short_name = self._query.get_course_short_name()
            if course_short_name:
                for i in course_short_name:
                    self.aSCourse.addItem(i[0])

    def _selection_change_course(self):
        """
        Updates the semester combo box based on the selected course.
        """
        if self.aSSemester.count() != 1:
            c = self.aSSemester.count()
            for i in range(1, c):
                self.aSSemester.removeItem(1)

        duration_year = self._query.get_course_year(self.aSCourse.currentText())
        if duration_year:
            semester = duration_year[0] * 2 + 1
            for i in range(1, semester):
                self.aSSemester.addItem(f"{i}")

    def _submit(self):
        """
        Handles adding or updating student details based on the use type.
        """
        roll_no = self.aSRollNumber.text()
        student_name = self.aSStudentName.text()
        guardian_name = self.aSGuardianName.text()
        mobile_number = self.aSSMobileNumber.text()
        university_short_name = self.aSUniversity.currentText()
        course_short_name = self.aSCourse.currentText()
        semester = self.aSSemester.currentText()

        if not roll_no:
            Common.show_message("Roll Number is empty!.")
            return

        if not student_name:
            Common.show_message("Student name is empty!.")
            return
        if not guardian_name:
            Common.show_message("Guardian name is empty!.")
            return
        if not mobile_number:
            Common.show_message("Mobile Number is empty!.")
            return

        if not university_short_name:
            Common.show_message("Select University")
            return
        if not course_short_name:
            Common.show_message("Select Course!.")
            return
        if not semester:
            Common.show_message("Select Semester!.")
            return

        try:
            if self._use_type == "add":
                value = (roll_no, student_name, guardian_name, mobile_number, university_short_name, course_short_name,
                         semester)
                success = self._query.insert_student_detail(value)
                if success:
                    Common.show_message("Student add successfully!", "I")
                    self._clear_fields()

            elif self._use_type == "update":
                value = (roll_no, student_name, guardian_name, mobile_number, university_short_name, course_short_name,
                         semester, self._roll_no)
                success = self._query.update_student_detail(value)
                if success:
                    Common.show_message("Student update successfully!", "I")
                    self._clear_fields()
                    self.accept()
        except Exception as e:
            Common.show_message(f"An error occurred: {str(e)}", "C")

    def _clear_fields(self):
        """
        Clears all input fields in the dialog.
        """
        self.aSStudentName.clear()
        self.aSRollNumber.clear()
        self.aSGuardianName.clear()
        self.aSSMobileNumber.clear()
        self.aSUniversity.setCurrentIndex(0)
        self.aSCourse.setCurrentIndex(0)
        self.aSSemester.setCurrentIndex(0)
