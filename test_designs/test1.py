
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QGridLayout, QTableWidget, QTableWidgetItem, QSizePolicy
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 600)  # Set initial geometry to cover the whole screen
        self.setCentralWidget(QWidget())  # Central widget for the layout
        self.setStyleSheet("background-color: #f0f0f0;")  # Set background color

        self.initstartUI()

    def initstartUI(self):

        font = QFont()
        font.setPointSize(25)

        layout = QVBoxLayout()
        layout.setSpacing(20)
        self.centralWidget().setLayout(layout)


        self.bets_table = QTableWidget()
        layout.addWidget(self.bets_table)

        self.bets_table.setColumnCount(7)
        self.bets_table.setColumnWidth(0, 500)
        # for column in range(self.bets_table.columnCount()):
        #     self.bets_table.setColumnWidth(column, 400)
        self.bets_table.setHorizontalHeaderLabels(["Sport", "Teams", "Status", "Home Odds", "Away Odds", "Wager", "Payout"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StartWindow()
    window.showFullScreen()  # Show the window in fullscreen mode
    sys.exit(app.exec())
