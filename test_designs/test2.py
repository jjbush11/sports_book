import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.setGeometry(0, 0, 800, 600)  # Set initial geometry to cover the whole screen
        self.setCentralWidget(QWidget())  # Central widget for the layout
        self.setStyleSheet("background-color: #f0f0f0;")  # Set background color

        self.initstartUI()

    def initstartUI(self):

        layout = QVBoxLayout()
        layout.setSpacing(20)
        self.centralWidget().setLayout(layout)

        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)

        # Set the number of rows and columns
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Sport", "Teams", "Status"])
        self.table_widget.setColumnWidth(0, 100)
        self.table_widget.setColumnWidth(1, 200)
        self.table_widget.setColumnWidth(2, 200)
        self.table_widget.setFixedHeight(300)
        self.table_widget.setFixedWidth(900)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
