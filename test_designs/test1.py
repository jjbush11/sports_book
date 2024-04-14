import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple Table Example")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.table_widget = QTableWidget()
        self.layout.addWidget(self.table_widget)

        # Set the number of rows and columns
        self.table_widget.setRowCount(5)
        self.table_widget.setColumnCount(3)
        self.table_widget.setColumnWidth(0, 200)
        self.table_widget.setColumnWidth(1, 200)
        self.table_widget.setColumnWidth(2, 200)


        # Populate the table with some data
        data = [
            ("Item 1", "Description 1", "$10.00"),
            ("Item 2", "Description 2", "$20.00"),
            ("Item 3", "Description 3", "$30.00"),
            ("Item 4", "Description 4", "$40.00"),
            ("Item 5", "Description 5", "$50.00"),
        ]
        for row, item in enumerate(data):
            for column, value in enumerate(item):
                self.table_widget.setItem(row, column, QTableWidgetItem(value))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
