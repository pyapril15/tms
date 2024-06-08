import bcrypt
from PySide6.QtWidgets import QDialog

from data.database.db_query import Query
from data.ui.user_registration import Ui_Dialog as UserRegistrationDialog
from data.working.common import Common


def generate_salt():
    """Generates a random salt using bcrypt."""
    return bcrypt.gensalt(rounds=12)


def hash_password(password, salt):
    """Hashes a password with the provided salt using bcrypt.

    Args:
        password (str): The password to be hashed.
        salt (bytes): The salt to be used for hashing.

    Returns:
        bytes: The hashed password.
    """
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password


class UserRegistration(QDialog, UserRegistrationDialog):
    """Dialog box for user registration."""

    def __init__(self, parent=None, user_type="staff"):
        """Initialize the UserRegistration dialog.

        Args:
            parent (QWidget): The parent widget of the dialog.
            user_type (str): The type of user. Default is "staff".
        """
        super().__init__(parent)
        self._query = Query()
        self._user_type = user_type

    def ui(self):
        """Set up the UI elements of the dialog."""
        self.setupUi(self)
        self.setWindowTitle("User Registration")
        self.uSignUpBtn.clicked.connect(self._signup)
        if self._user_type == "admin":
            self.uTitle.setText("Admin Registration")

    def _signup(self):
        """Handle the sign-up button click event."""
        username = self.uUsername.text()
        fullname = self.uFullName.text()
        mobile = self.uMobileNumber.text()
        password = self.uPassword.text()

        if not username:
            Common.show_message("Username is empty!")
            return
        if not fullname:
            Common.show_message("Fullname is empty!")
            return
        if not mobile:
            Common.show_message("Mobile Number is empty!")
            return
        if not password:
            Common.show_message("Password is empty!")
            return

        salt = generate_salt()
        hashed_password = hash_password(password, salt)

        staff = (username, fullname, mobile)
        auth = (username, salt, hashed_password, 0)
        if self._user_type == "admin":
            auth = (username, salt, hashed_password, 1)

        success = self._query.insert_staff_and_auth(staff, auth)

        if success:
            Common.show_message("User registered successfully!", "I")
            self._clear_fields()
            self.accept()
        else:
            Common.show_message("Registration Failed! Please try again.", "C")

    def _clear_fields(self):
        """Clear all input fields."""
        self.uUsername.clear()
        self.uFullName.clear()
        self.uMobileNumber.clear()
        self.uPassword.clear()
