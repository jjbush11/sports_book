import sys
import login
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QGridLayout, QTableWidget
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

        navbar_layout = QHBoxLayout()
        navbar_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        layout.addLayout(navbar_layout)

        activebets_layout = QVBoxLayout()

        pastbets_layout = QVBoxLayout()
        

        layout.addLayout(navbar_layout)
        layout.addLayout(activebets_layout)
        layout.addLayout(pastbets_layout)

        home_button = QPushButton("Home")
        home_button.setStyleSheet("padding: 10px 20px; background-color: BlueViolet; color: white; border: none; border-radius: 5px;")
        navbar_layout.addWidget(home_button)
        mybets_button = QPushButton("My Bets")
        mybets_button.setStyleSheet("padding: 10px 20px; background-color: BlueViolet; color: white; border: none; border-radius: 5px;")
        navbar_layout.addWidget(mybets_button)
        balance_button = QPushButton("Balance: $1205")
        balance_button.setStyleSheet("padding: 10px 20px; background-color: BlueViolet; color: white; border: none; border-radius: 5px;")
        navbar_layout.addWidget(balance_button)

        activebets_label = QLabel("Active Bets")
        activebets_label.setFont(font)
        activebets_layout.addWidget(activebets_label)

        pastbets_label = QLabel("Past Bets")
        pastbets_label.setFont(font)
        pastbets_layout.addWidget(pastbets_label)

        bets_table = QTableWidget()
        bets_table.setColumnCount(4)
        bets_table.setHorizontalHeaderLabels(["Event", "Bet Type", "Amount", "Status"])
        bets_table.setFixedHeight(300)
        bets_table.setFixedWidth(600)
        activebets_layout.addWidget(bets_table)

        bets_table1 = QTableWidget()
        bets_table1.setColumnCount(4)
        bets_table1.setHorizontalHeaderLabels(["Event", "Bet Type", "Amount", "Status"])
        bets_table1.setFixedHeight(300)
        bets_table1.setFixedWidth(600)

        pastbets_layout.addWidget(bets_table1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StartWindow()
    window.showFullScreen()  # Show the window in fullscreen mode
    sys.exit(app.exec())
