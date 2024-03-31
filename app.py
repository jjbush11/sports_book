import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Page")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)

        # Also change the window title.
        self.setWindowTitle("My Clicked App")

app = QApplication(sys.argv)
window = LoginWindow()
window.show()
app.exec()