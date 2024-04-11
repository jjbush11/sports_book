import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QLineEdit, QListWidget

class SportsBettingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sports Betting App")
        self.setGeometry(100, 100, 400, 300)  # x, y, width, height

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.sport_selector = QComboBox()
        self.sport_selector.addItems(["Football", "Basketball", "Tennis"])
        self.layout.addWidget(self.sport_selector)

        self.matches_list = QListWidget()
        self.layout.addWidget(self.matches_list)
        self.populate_matches()  # Populate with dummy data

        self.bet_input = QLineEdit()
        self.bet_input.setPlaceholderText("Enter your bet amount")
        self.layout.addWidget(self.bet_input)

        self.bet_button = QPushButton("Place Bet")
        self.bet_button.clicked.connect(self.place_bet)
        self.layout.addWidget(self.bet_button)

        self.status_label = QLabel()
        self.layout.addWidget(self.status_label)

    def populate_matches(self):
        # This is just dummy data, in a real app, you'd fetch this from your backend
        self.matches_list.addItems(["Team A vs Team B", "Team C vs Team D"])

    def place_bet(self):
        # Logic to place bet goes here
        # This is just a placeholder implementation
        amount = self.bet_input.text()
        match = self.matches_list.currentItem().text() if self.matches_list.currentItem() else None
        if not amount or not match:
            self.status_label.setText("Please select a match and enter a bet amount.")
            return
        self.status_label.setText(f"Bet of {amount} on {match} placed!")

def main():
    app = QApplication(sys.argv)
    window = SportsBettingApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
