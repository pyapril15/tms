from PySide6.QtWidgets import QDialog

from data.database.db_query import Query
from data.ui.add_transport_fee_detail import Ui_Dialog as AddTransportFeeDetailDialog
from data.working.common import Common


class TransportPlaceFeeDialog(QDialog, AddTransportFeeDetailDialog):
    """Dialog for adding or updating transport fee details.

    This dialog allows users to add new transport fee details or update existing ones. It provides
    input fields for center code, center name, and fee amount, and handles the submission of data
    to the database.
    """

    def __init__(self, parent=None, use_type="add", center_code=None, center_name=None, fee=None):
        """Initialize the dialog.

        Args:
            parent: The parent widget (optional).
            use_type (str): The type of usage, either 'add' or 'update'.
            center_code (str): The code of the transport center (optional).
            center_name (str): The name of the transport center (optional).
            fee (str): The fee amount (optional).
        """
        super().__init__(parent)

        self._use_type = use_type
        self._center_code = center_code
        self._center_name = center_name
        self._fee = fee

    def ui(self):
        """Set up the UI elements and connect signals."""
        self.setupUi(self)
        self.setWindowTitle("Add Transport Fee Detail")
        self.aTAddBtn.clicked.connect(self._submit)

    def set_values(self):
        """Set initial values for Center and Fee details."""
        self.aTCenterName.setText(self._center_name)
        self.aTCenterCode.setText(self._center_code)
        self.aTAmount.setText(self._fee)

    def _submit(self):
        """Handle submission of Transport details."""
        center_code = self.aTCenterCode.text()
        center_name = self.aTCenterName.text()
        center_fee = self.aTAmount.text()

        if not center_code:
            Common.show_message("Center Code is empty!.")
            return
        if not center_name:
            Common.show_message("Center name is empty!.")
            return

        if not center_fee:
            Common.show_message("Center fee is empty!.")
            return

        query = Query()
        try:
            if self._use_type == "add":
                success = query.insert_transport_place_fee_detail((center_code, center_name, center_fee))
                if success:
                    Common.show_message("Center name and fee added successfully!", "I")
                    self._clear_fields()
                    self.close()

            elif self._use_type == "update":
                success = query.update_transport_place_fee_detail(
                    (center_code, center_name, center_fee, self._center_code))
                if success:
                    Common.show_message("Update successful!", "I")
                    self._clear_fields()
                    self.close()
        except Exception as e:
            Common.show_message(f"An error occurred: {str(e)}", "C")

    def _clear_fields(self):
        """Clear all input fields."""
        self.aTCenterCode.clear()
        self.aTCenterName.clear()
        self.aTAmount.clear()
