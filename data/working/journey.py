from collections import namedtuple

from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDialog

from data.database.db_query import Query
from data.ui.new_journey import Ui_Dialog as NewJourneyDialog
from data.working.common import Common

JourneyData = namedtuple('JourneyData', ['place', 'date', 'shift'])


class NewJourney(QDialog, NewJourneyDialog):
    """Dialog window for adding or updating journey details."""

    def __init__(self, parent=None, use_type='add', journey_id: int = None):
        """
        Initialize the NewJourney dialog.

        Args:
            parent: Parent widget (default: None).
            use_type: Type of usage ('add' for adding, 'update' for updating).
            journey_id: ID of the journey to be updated (default: None).
        """
        super().__init__(parent)
        self._query = Query()
        self._use_type = use_type
        self._journey_id = journey_id
        self._journey_data = None
        if self._journey_id is not None:
            self._journey_data = self._query.get_journey_detail_j_id(self._journey_id)

    def ui(self):
        """Set up the user interface."""
        self.setupUi(self)
        self.setWindowTitle("New Journey Detail")
        self._welcome()
        self._set_value()

    def _set_value(self):
        """Set initial values if updating an existing journey."""
        if self._journey_id and self._journey_data:
            journey_data = JourneyData(*self._journey_data)
            self.aJPlace.setCurrentText(journey_data.place)
            self.aJDate.setDate(QDate(journey_data.date))
            self.aJShift.setCurrentText(journey_data.shift)

    def _welcome(self):
        """Set up welcome message and populate place dropdown list."""
        self.aJSubmitBtn.clicked.connect(self._submit)
        self.aJPlace.clear()
        self.aJPlace.addItem("Select Place")
        self.aJDate.setDate(QDate.currentDate())

        place_name = self._query.get_center_name_from_transport_fee()
        if place_name:
            for item in place_name:
                self.aJPlace.addItem(item[0])

    def _save_other_journey_detail(self, _to: str, date, shift: str):
        """
        Save journey detail to the database.

        Args:
            _to: Destination place.
            date: Journey date.
            shift: Shift of the journey.

        Returns:
            bool: True if saving is successful, False otherwise.
        """
        date_str = date.toString("yyyy-MM-dd")
        value = (_to, date_str, shift, "other")
        try:
            success = self._query.insert_other_journey_detail(value)
            return success
        except Exception as e:
            Common.show_message(f"Error saving journey detail: {str(e)}", "C")
            return False

    def _submit(self):
        """Handle submission of journey details."""
        place = self.aJPlace.currentText()
        date = self.aJDate.date()
        shift = self.aJShift.currentText()

        if place == 'Select Place':
            Common.show_message("Please select a place.", "W")
            return
        elif shift == 'Select Shift':
            Common.show_message("Please select a shift.", "W")
            return

        if self._use_type == 'add':
            success = self._save_other_journey_detail(place, date, shift)
            if success:
                Common.show_message("Journey created successfully.", "I")
                self.close()
            else:
                Common.show_message("Failed to create journey. Please try again.", "C")
        elif self._use_type == 'update':
            if self._journey_data:
                date_str = date.toString("yyyy-MM-dd")
                value = (place, date_str, shift, self._journey_id)
                try:
                    success = self._query.update_journey_detail(value)
                    if success:
                        Common.show_message("Update successful.", "I")
                        self.close()
                    else:
                        Common.show_message("Failed to update journey. Please try again.", "C")
                except Exception as e:
                    Common.show_message(f"Error updating journey detail: {str(e)}", "C")
            else:
                Common.show_message("Provide with value!.", "W")
