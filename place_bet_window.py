import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox
from database.db_bet import ConnectDbBet

class PlaceBetInputWindow(QWidget):

    username = ""
    id = -1
    win = 0
    odds = 0
    settled = 0

    def __init__(self, username, id, odds):
        super().__init__()
        self.initUI()

        self.username = username
        self.id = id
        self.odds = odds

    def initUI(self):
        self.setWindowTitle('Place Bet')

        # Create Label container, input line, and push button
        self.label = QLabel('Enter dollar amount (00.00 format):')
        self.wager_input = QLineEdit()
        self.submit_button = QPushButton('Place Bet')
        self.submit_button.clicked.connect(self.process_input)

        # Adds the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.wager_input)
        layout.addWidget(self.submit_button)

        # Displays widgets to users
        self.setLayout(layout)
        self.show()

    def process_input(self):
        wager_str = self.wager_input.text()
        try:
            # Convert user input to float and validate input
            wager = float(wager_str)
            if wager >= 0:
                # Connect to database and insert bet
                db = ConnectDbBet()
                new_bet = db.add_new_bet(
                    username=self.username,
                    par_id=self.id,
                    win=self.win,
                    odds=self.odds,
                    wager=wager,
                    settled=0
                )

                # Verify new bet is added
                if new_bet == 0:
                   QMessageBox.information(self, 'Success', f'Bet placed!\nYou wagered: ${wager:.2f}')
                else:
                    QMessageBox.warning(self, 'Error', 'Unable to place bet, please try again later.')
            else:
                QMessageBox.warning(self, 'Error', 'Please enter a positive dollar amount.')
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Invalid input. Please enter a valid dollar amount.')

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = PlaceBetInputWindow()
#     sys.exit(app.exec())

def test():
    PlaceBetInputWindow('jjbush', 'FakeTeamApr 12', -200)

test()