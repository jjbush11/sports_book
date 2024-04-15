import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox
from database.db_bet import ConnectDbBet
from database.db_connect_user import ConnectDbUser

class PlaceBetInputWindow(QWidget):

    username = ""
    id = -1
    win = 0
    odds = 0
    team = ""

    def __init__(self, username, id, odds, team):
        super().__init__()
        self.initUI()

        self.username = username
        self.id = id
        self.odds = odds
        self.team = team

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
                # Check that user has enough funds to place bet
                db_user = ConnectDbUser()
                user = db_user.get_row_by_user(self.username)

                # Check that user exits
                if user is None:
                    QMessageBox.critical(self, 'Error', 'Username does not exist!')
                    self.close()
                # Check that user has enough money to place bet
                elif user.balance < wager:
                    QMessageBox.critical(self, 'Error', 'Insufficient funds!\nPlease enter a lower amount.')
                else:
                    # Connect to database and insert bet
                    db_bet = ConnectDbBet()
                    new_bet = db_bet.add_new_bet(
                        username=self.username,
                        par_id=self.id,
                        win=self.win,
                        odds=self.odds,
                        team=self.team,
                        wager=wager,
                        settled=0
                    )

                    # Add bet to live bets so its displayed right away
                    live_bet = []
                    live_bet.append('NA')
                    live_bet.append('NA')
                    live_bet.append('NA')
                    live_bet.append(self.team)
                    live_bet.append(self.odds)
                    live_bet.append(wager)
                    live_bet.append('Return Pending')
                    live_bet.append('Pending')
                    # Add to global list
                    session_live_bets.append(live_bet)

                    # Verify new bet is added
                    if new_bet == 0:
                        # If bet is placed, subtract funds from user
                        new_balance = user.balance - wager
                        db_user.edit_row(self.username, 'balance', new_balance)
                        QMessageBox.information(self, 'Success', f'Bet placed!\nYou wagered: ${wager:.2f}')
                        self.close()
                    else:
                        QMessageBox.warning(self, 'Error', 'Unable to place bet, please try again later.')
            else:
                QMessageBox.warning(self, 'Error', 'Please enter a positive dollar amount.')
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Invalid input. Please enter a valid dollar amount.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PlaceBetInputWindow('jjbush', 'Miami MarlinsAtlanta BravesApr 12', 300, "Atlanta Braves")
    sys.exit(app.exec())
