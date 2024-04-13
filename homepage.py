import sys
import user_session_info
from database import db_connect_user

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QGridLayout, QTableWidget
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
 
db = db_connect_user.ConnectDbUser()

class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 600)  # Set initial geometry to cover the whole screen
        self.setCentralWidget(QWidget())  # Central widget for the layout
        self.setStyleSheet("background-color: #f0f0f0;")  # Set background color

        self.initstartUI()

    def getUserBalance(self, username):
        user_rows = db.get_row_by_user(username)
        if (user_rows == None):
            print ("failed")
        return (user_rows)
    
    def initstartUI(self):

        user_info = self.getUserBalance(user_session_info.session_username)
        balance = user_info[2]
        balance_string = str(balance)


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
        balance_button = QPushButton("Balance: $" + balance_string)
        balance_button.setStyleSheet("padding: 10px 20px; background-color: BlueViolet; color: white; border: none; border-radius: 5px;")
        navbar_layout.addWidget(balance_button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StartWindow()
    window.showFullScreen()  # Show the window in fullscreen mode
    sys.exit(app.exec())
