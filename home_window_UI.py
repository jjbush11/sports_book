import sys
import user_session_info, nba_home_UI, nhl_home_UI, mlb_home_UI, mybets
from database import db_connect_user

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QGridLayout, QTableWidget
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
 
db = db_connect_user.ConnectDbUser()

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 600)  # Set initial geometry to cover the whole screen
        self.setCentralWidget(QWidget())  # Central widget for the layout
        self.setStyleSheet("background-color: #f0f0f0;")  # Set background color

        self.initstartUI()

    def getUserBalance(self, username):
        user_rows = db.get_row_by_user(username)
        if user_rows is None:
            print ("failed")
        return user_rows
    
    def initstartUI(self):

        user_info = self.getUserBalance(user_session_info.session_username)
        balance = user_info[2]
        balance_string = str(balance)

        font = QFont()
        font.setPointSize(25)

        main_layout = QVBoxLayout()
        self.centralWidget().setLayout(main_layout)

        # Navigation bar
        navbar_layout = QHBoxLayout()
        navbar_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        home_button = QPushButton("Home")
        home_button.setStyleSheet("padding: 10px 20px; background-color: Indigo; color: white; border: none; border-radius: 5px;")
        navbar_layout.addWidget(home_button)

        mybets_button = QPushButton("My Bets")
        mybets_button.setStyleSheet("padding: 10px 20px; background-color: BlueViolet; color: white; border: none; border-radius: 5px;")
        navbar_layout.addWidget(mybets_button)
        mybets_button.clicked.connect(self.mybets_click)

        balance_button = QPushButton("Balance: $" + balance_string)
        balance_button.setStyleSheet("padding: 10px 20px; background-color: BlueViolet; color: white; border: none; border-radius: 5px;")
        navbar_layout.addWidget(balance_button)

        main_layout.addLayout(navbar_layout)

        # Sports buttons
        sports_layout = QHBoxLayout()
        sports_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)  # Align top and horizontally center
        sports_layout.setSpacing(20)

        nba_button = QPushButton("NBA")
        nba_button.setFixedHeight(50)
        nba_button.setFixedWidth(200)
        nba_button.setFont(font)
        nba_button.setStyleSheet("padding: 10px 20px; background-color: BlueViolet; color: white; border: none; border-radius: 5px;")
        sports_layout.addWidget(nba_button)
        nba_button.clicked.connect(self.nba_click)

        nhl_button = QPushButton("NHL")
        nhl_button.setFixedHeight(50)
        nhl_button.setFixedWidth(200)
        nhl_button.setFont(font)
        nhl_button.setStyleSheet("padding: 10px 20px; background-color: BlueViolet; color: white; border: none; border-radius: 5px;")
        sports_layout.addWidget(nhl_button)
        nhl_button.clicked.connect(self.nhl_click)

        mlb_button = QPushButton("MLB")
        mlb_button.setFixedHeight(50)
        mlb_button.setFixedWidth(200)
        mlb_button.setFont(font)
        mlb_button.setStyleSheet("padding: 10px 20px; background-color: BlueViolet; color: white; border: none; border-radius: 5px;")
        sports_layout.addWidget(mlb_button)
        mlb_button.clicked.connect(self.mlb_click)

        main_layout.addLayout(sports_layout)

    def nba_click(self):
        self.nba_window = nba_home_UI.Ui_MainWindow()
        self.nba_window.show()
        self.close()
        
    def nhl_click(self):
        self.nhl_window = nhl_home_UI.Ui_MainWindow()
        self.nhl_window.show()
        self.close()

    def mlb_click(self):
        self.mlb_window = mlb_home_UI.Ui_MainWindow()
        self.mlb_window.show()
        self.close()

    def mybets_click(self):
        self.mybets_window = mybets.StartWindow()
        self.mybets_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.showFullScreen()  # Show the window in fullscreen mode
    sys.exit(app.exec())
