from PySide6.QtGui import QTextDocument, QTextCursor, QPageSize
from PySide6.QtPrintSupport import QPrinter, QPrintPreviewDialog


class PrintPreviewDialog:
    def __init__(self, tableWidget):
        self.tableWidget = tableWidget

    def print_preview(self):
        printer = QPrinter()
        printer.setPageSize(QPageSize(QPageSize.Letter))  # Set the page size
        printer.setOutputFormat(QPrinter.NativeFormat)  # Use the native format for the printer
        printer.setOutputFileName("output.pdf")  # Optional: set the output file name

        preview_dialog = QPrintPreviewDialog(printer)
        preview_dialog.paintRequested.connect(self.print)
        preview_dialog.exec()

    def print(self, printer):
        with open("template/table.html", "r") as file:
            html_template = file.read()

        # Prepare the table headers
        headers_html = "<tr>"
        is_function_present = 0
        for col in range(self.tableWidget.columnCount()):
            column_name = self.tableWidget.horizontalHeaderItem(col).text()
            if column_name != "Function":
                headers_html += f"<th>{column_name}</th>"
            else:
                is_function_present += 1

        headers_html += "</tr>"

        # Prepare the table rows
        rows_html = ""
        for row in range(self.tableWidget.rowCount()):
            rows_html += "<tr>"
            column_count = self.tableWidget.columnCount()
            if is_function_present:
                column_count -= is_function_present
            for col in range(column_count):
                item = self.tableWidget.item(row, col)
                if item is not None:
                    rows_html += f"<td>{item.text()}</td>"
                else:
                    rows_html += "<td></td>"
            rows_html += "</tr>"

        # Insert headers and rows into the HTML template
        html_content = html_template.replace("<thead></thead>", f"<thead>{headers_html}</thead>")
        html_content = html_content.replace("<tbody></tbody>", f"<tbody>{rows_html}</tbody>")

        document = QTextDocument()
        cursor = QTextCursor(document)
        cursor.insertHtml(html_content)
        document.print_(printer)
