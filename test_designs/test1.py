from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox

class SignUpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Layout
        layout = QVBoxLayout()

        # Username field
        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Enter your username")
        layout.addWidget(self.username)

        # Password field
        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Enter your password")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password)

        # Confirm password field
        self.confirm_password = QLineEdit(self)
        self.confirm_password.setPlaceholderText("Confirm your password")
        self.confirm_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.confirm_password)

        # Submit button
        self.submit_button = QPushButton('Sign Up', self)
        self.submit_button.clicked.connect(self.check_passwords)
        layout.addWidget(self.submit_button)

        # Set layout
        self.setLayout(layout)
        self.setWindowTitle("Sign Up")

    def check_passwords(self):
        if self.password.text() == self.confirm_password.text():
            QMessageBox.information(self, 'Success', 'Signup successful!')
        else:
            QMessageBox.warning(self, 'Error', 'Passwords do not match.')

# Run the application
def main():
    app = QApplication([])
    window = SignUpWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
