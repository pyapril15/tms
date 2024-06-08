from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox, QTableWidget


class Common:
    def __init__(self):
        pass

    @staticmethod
    def show_message(message: str, t="W"):
        msg = QMessageBox()
        if t == "YN":
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        elif t == "C":
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Cancel)

        elif t == "I":
            msg.setIcon(QMessageBox.Information)

        else:
            msg.setIcon(QMessageBox.Warning)

        msg.setText(message)

        x = msg.exec()
        return x

    @staticmethod
    def get_selected_row_data(table: QTableWidget):
        selected_row = table.currentRow()
        if selected_row >= 0:
            selected_row_data = []
            for col in range(table.columnCount()):
                index = table.model().index(selected_row, col)
                data = table.model().data(index, Qt.DisplayRole)
                selected_row_data.append(data)
            return selected_row_data
        return

    @staticmethod
    def get_selected_row_specific_column_data(table: QTableWidget, column: int):
        selected_rows = set()
        for item in table.selectedItems():
            selected_rows.add(item.row())

        column_data = []
        for row in selected_rows:
            item = table.item(row, column)
            if item is not None:
                column_data.append(item.text())
        return column_data

    def get_table_data(self, table: QTableWidget, row=None, column=None, gap=1):
        starting_row = 0
        starting_col = 0
        stopping_row = table.rowCount()
        stopping_col = table.columnCount()
        gap = gap
        data = []

        if row is not None:
            starting_row = row
            stopping_row = starting_row + gap

        if column is not None:
            starting_col = column
            stopping_col = starting_col + gap

        for i in range(starting_row, stopping_row):
            row_data = self._table_column_data(table, i, [starting_col, None if column is not None else stopping_col])
            data.append(row_data)
        return data

    @staticmethod
    def _table_column_data(table: QTableWidget, row: int, column: list):
        row_data = []
        if None in column:
            column.remove(None)
        else:
            j = 0
            for i in range(column[0], column[1]):
                column[j] = i
                j += 1
        for j in column:
            item = table.item(row, j)
            if item is not None:
                row_data.append(item.text())
            else:
                row_data.append(None)
        return row_data

    @staticmethod
    def get_row_items(table: QTableWidget, row):
        # Get QTableWidgetItem objects for a given row
        return [table.item(row, col) for col in range(table.columnCount())]

    def select_rows_based_on_criteria(self, table: QTableWidget, criteria: tuple):
        # Precompute all row items
        all_row_items = [self.get_row_items(table, row) for row in range(table.rowCount())]

        # Iterate through all rows and select rows matching the criteria
        for row, row_items in enumerate(all_row_items):
            if self.row_matches_criteria(row_items, criteria):
                table.selectRow(row)
                return True
        return False

    @staticmethod
    def row_matches_criteria(row_items, criteria: tuple):
        # Check if given row matches the criteria tuple in the first three columns
        return all(item.text() == data for item, data in zip(row_items, criteria))
