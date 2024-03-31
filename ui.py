import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Page")
        self.setGeometry(0, 0, 800, 600)  # Set initial geometry to cover the whole screen
        self.setCentralWidget(QWidget())  # Central widget for the layout
        self.setStyleSheet("background-color: #f0f0f0;")  # Set background color

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)  # Center-align widgets
        self.centralWidget().setLayout(layout)

        font1 = QFont()
        font1.setPointSize(16)

        font2 = QFont()
        font2.setPointSize(20)

        label_password = QLabel("Welcome to our betting app, please login if you have an existing account or sign-up to create a new one")
        label_password.setFont(font2)
        
        layout.addWidget(label_password)

        login_button = QPushButton("Login")
        login_button.setFixedHeight(50)
        login_button.setFont(font2)
        login_button.setStyleSheet("padding: 10px 20px; background-color: BlueViolet; color: white; border: none; border-radius: 5px;")
        layout.addWidget(login_button)
        login_button.clicked.connect(self.login_click)

        signup_button = QPushButton("Sign-up")
        signup_button.setFixedHeight(50)
        signup_button.setFont(font2)
        signup_button.setStyleSheet("padding: 10px 20px; background-color: BlueViolet; color: white; border: none; border-radius: 5px;")
        layout.addWidget(signup_button)
        signup_button.clicked.connect(self.signup_click)
    
    def login_click(self):
        print("Login clicked!")
    
    def signup_click(self):
        print("Sign-up clicked!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.showFullScreen()  # Show the window in fullscreen mode
    sys.exit(app.exec())
