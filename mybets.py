import sys
import user_session_info, home_window_UI
from database import db_bet, db_settled_matches, db_upcoming_matches, db_connect_user
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QGridLayout, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

db = db_connect_user.ConnectDbUser()
db1 = db_bet.ConnectDbBet()
db2 = db_settled_matches.ConnectDbSettledMatch()
db3 = db_upcoming_matches.ConnectDbUpcomingMatch()

class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 600)  # Set initial geometry to cover the whole screen
        self.setCentralWidget(QWidget())  # Central widget for the layout
        self.setStyleSheet("background-color: #f0f0f0;")  # Set background color

        self.initstartUI()

    #Updates users displayed balance
    def getUserBalance(self, username):
        user_rows = db.get_row_by_user(username)
        if user_rows is None:
            print ("failed")
        return user_rows

    def initstartUI(self):
        
        user_info = self.getUserBalance(user_session_info.session_username)
        balance = user_info[2]
        balance_string = str(balance)

        #Create font
        font = QFont()
        font.setPointSize(25)

        ##Create main layout
        layout = QVBoxLayout()
        layout.setSpacing(20)
        self.centralWidget().setLayout(layout)


        ##Create child layouts
        navbar_layout = QHBoxLayout()
        navbar_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        activebets_layout = QVBoxLayout()

        pastbets_layout = QVBoxLayout()
        

        #Add child layouts to main layout
        layout.addLayout(navbar_layout)
        layout.addLayout(activebets_layout)
        layout.addLayout(pastbets_layout)


        #Nav bar
        home_button = QPushButton("Home")
        home_button.setStyleSheet("padding: 10px 20px; background-color: BlueViolet; color: white; border: none; border-radius: 5px;")
        navbar_layout.addWidget(home_button)
        home_button.clicked.connect(self.home_clicked)

        mybets_button = QPushButton("My Bets")
        mybets_button.setStyleSheet("padding: 10px 20px; background-color: Indigo; color: white; border: none; border-radius: 5px;")
        navbar_layout.addWidget(mybets_button)

        balance_button = QPushButton("Balance: $" + balance_string)
        balance_button.setStyleSheet("padding: 10px 20px; background-color: BlueViolet; color: white; border: none; border-radius: 5px;")
        navbar_layout.addWidget(balance_button)


        #Active bets table
        activebets_label = QLabel("Active Bets")
        activebets_label.setFont(font)
        activebets_layout.addWidget(activebets_label)

        self.bets_table = QTableWidget()
        activebets_layout.addWidget(self.bets_table)
        self.bets_table.setColumnCount(8)
        self.bets_table.setHorizontalHeaderLabels(["Sport", "Home", "Away", "Bet Placed", "Odds", "Wager", "Payout", "Status"])
        for column in range(self.bets_table.columnCount()):
            self.bets_table.setColumnWidth(column, 160)
        self.bets_table.setFixedHeight(300)
        self.bets_table.setFixedWidth(1300)


        #Past bets table
        pastbets_label = QLabel("Past Bets")
        pastbets_label.setFont(font)
        pastbets_layout.addWidget(pastbets_label)

        self.bets_table1 = QTableWidget()
        pastbets_layout.addWidget(self.bets_table1)
        self.bets_table1.setColumnCount(9)
        self.bets_table1.setHorizontalHeaderLabels(["Sport", "Home", "Away", "Score", "Bet Placed", "Odds", "Wager", "Payout", "Status"])
        for column in range(self.bets_table.columnCount()):
            self.bets_table1.setColumnWidth(column, 147)
        self.bets_table1.setFixedHeight(300)
        self.bets_table1.setFixedWidth(1300)


        #Get data for tables

        #Get data for settled matches
        past_bets = self.get_past_bets()

        #Get data for active matches
        current_bets = self.get_active_bets()
        

        #Create rows and populate table
        if (past_bets is not None):
            #Creating rows for settled matches
            for i in range(len(past_bets)):
                self.add_rows_table1(i, past_bets[i])
        
        if (current_bets is not None):
            #Creating rows for active matches
            for i in range(len(current_bets)):
                self.add_rows_table2(i, current_bets[i])


    def get_past_bets(self):

        try:
            bets = db1.get_all_settled_bets_by_user(user_session_info.session_username)
            bets_list = []
            overall_list = []

            for bet in bets:
                settled_match = db2.get_settled_matches_by_id(bet[1])
                settled_match = list(settled_match)
                bet = list(bet)
                bets_list.append(bet + settled_match)
        except:
            print("User has no settled bets")
        
        else:

            #Modifying bet list for proper display in table
            for bet in bets_list:
                bet = list(map(str, bet))
                sorted_bets_list = []
                sorted_bets_list.append(bet[14])
                sorted_bets_list.append(bet[12])
                sorted_bets_list.append(bet[10])
                sorted_bets_list.append(bet[13] + "-" + bet[11])
                sorted_bets_list.append(bet[4])
                sorted_bets_list.append(bet[3])
                sorted_bets_list.append(bet[5])
                sorted_bets_list.append(bet[6])
                if (bet[2]):
                    sorted_bets_list.append("Bet won")
                else:
                    sorted_bets_list.append("Bet lost")
                overall_list.append(sorted_bets_list)

            return overall_list

    def get_active_bets(self):
        try:
            bets = db1.get_all_active_bets_by_user(user_session_info.session_username)
            bets_list = []
            overall_list = []

            for bet in bets:
                active_match = db3.get_upcoming_matches_by_id(bet[1])
                active_match = list(active_match)
                bet = list(bet)
                bets_list.append(bet + active_match)
            
        except:
            print("User has no settled bets")
        
        else:
            #Modifying bet list for proper display in table
            for bet in bets_list:
                bet = list(map(str, bet))
                sorted_bets_list = []
                sorted_bets_list.append(bet[16])
                sorted_bets_list.append(bet[10])
                sorted_bets_list.append(bet[12])
                sorted_bets_list.append(bet[4])
                sorted_bets_list.append(bet[3])
                sorted_bets_list.append(bet[5])
                sorted_bets_list.append(bet[6])
                sorted_bets_list.append("Pending")

                overall_list.append(sorted_bets_list)

            return overall_list

    #Functions to populate tables
    def add_rows_table1(self, position, row):
        self.bets_table1.insertRow(position)
        accumulator = 0
        for col in row:
            item = QTableWidgetItem(col)
            self.bets_table1.setItem(position, accumulator, item )
            accumulator += 1

    def add_rows_table2(self, position, row):
        self.bets_table.insertRow(position)
        accumulator = 0
        for col in row:
            item = QTableWidgetItem(col)
            self.bets_table.setItem(position, accumulator, item )
            accumulator += 1

    #Routes back to app homepage when clicked
    def home_clicked(self):
        self.home_window = home_window_UI.Ui_MainWindow()
        self.home_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StartWindow()
    window.showFullScreen()  # Show the window in fullscreen mode
    sys.exit(app.exec())
