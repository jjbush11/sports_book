import homepage
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QGridLayout
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
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)  # Center-align widgets
        self.centralWidget().setLayout(layout)

        font1 = QFont()
        font1.setPointSize(16)

        font2 = QFont()
        font2.setPointSize(20)

        label_welcome_mess = QLabel("Welcome to our betting app, please login if you have an existing account or sign-up to create a new one")
        label_welcome_mess.setFont(font2)
        
        layout.addWidget(label_welcome_mess)

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
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()
    
    def signup_click(self):
        self.signin_window = SignInWindow()
        self.signin_window.show()
        self.close()

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Page")
        self.setGeometry(0, 0, 800, 600)  # Set initial geometry to cover the whole screen
        self.setCentralWidget(QWidget())  # Central widget for the layout
        self.setStyleSheet("background-color: #f0f0f0;")  # Set background color

        self.loginUI()

    def loginUI(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)  # Center-align widgets

        self.centralWidget().setLayout(layout)

        font2 = QFont()
        font2.setPointSize(20)

        back_button = QPushButton("Back")
        back_button.setFont(font2)
        back_button.setStyleSheet("padding: 10px 20px; background-color: BlueViolet; color: white; border: none; border-radius: 5px;")
        layout.addWidget(back_button)
        back_button.clicked.connect(self.back_click)

        user_label = QLabel("Enter your username: ")
        user_label.setFont(font2)
        layout.addWidget(user_label)

        self.username = QLineEdit()
        self.username.setFixedWidth(200)
        layout.addWidget(self.username)

        password_label = QLabel("Enter your password: ")
        password_label.setFont(font2)
        layout.addWidget(password_label)

        self.password = QLineEdit()
        self.password.setFixedWidth(200)
        layout.addWidget(self.password)

        submit_button = QPushButton("Submit")
        submit_button.setFont(font2)
        submit_button.setStyleSheet("padding: 10px 20px; background-color: BlueViolet; color: white; border: none; border-radius: 5px;")
        layout.addWidget(submit_button)
        submit_button.clicked.connect(self.submit_click)

    def back_click(self):
        self.start_window = StartWindow()
        self.start_window.show()
        self.close()

    def submit_click(self):
        print (self.username.text())
        print (self.password.text())
        #Logic to check user credentials against user_db

        #If passed, route to main application window
        self.home_window = homepage.StartWindow()
        self.home_window.show()
        self.close()

class SignInWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sign-Up Page")
        self.setGeometry(0, 0, 800, 600)  # Set initial geometry to cover the whole screen
        self.setCentralWidget(QWidget())  # Central widget for the layout
        self.setStyleSheet("background-color: #f0f0f0;")  # Set background color

        self.signInUI()

    def signInUI(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)  # Center-align widgets
        self.centralWidget().setLayout(layout)

        font2 = QFont()
        font2.setPointSize(20)

        back_button = QPushButton("Back")
        back_button.setFont(font2)
        back_button.setStyleSheet("padding: 10px 20px; background-color: BlueViolet; color: white; border: none; border-radius: 5px;")
        layout.addWidget(back_button)
        back_button.clicked.connect(self.back_click)


        user_label = QLabel("Create a username: ")
        user_label.setFont(font2)
        layout.addWidget(user_label)

        self.username = QLineEdit()
        self.username.setFixedWidth(200)
        layout.addWidget(self.username)

        password_label = QLabel("Create a password: ")
        password_label.setFont(font2)
        layout.addWidget(password_label)

        self.password = QLineEdit()
        self.password.setFixedWidth(200)
        layout.addWidget(self.password)

        password_label2 = QLabel("Re-enter password: ")
        password_label2.setFont(font2)
        layout.addWidget(password_label2)

        self.password2 = QLineEdit()
        self.password2.setFixedWidth(200)
        layout.addWidget(self.password2)

        submit_button = QPushButton("Submit")
        submit_button.setFont(font2)
        submit_button.setStyleSheet("padding: 10px 20px; background-color: BlueViolet; color: white; border: none; border-radius: 5px;")
        layout.addWidget(submit_button)
        submit_button.clicked.connect(self.submit_click)

    def back_click(self):
        self.start_window = StartWindow()
        self.start_window.show()
        self.close()     

    def submit_click(self):
        print (self.username.text())
        print (self.password.text())   
        print (self.password2.text())

        passed = self.check_match(self.password.text(), self.password2.text())
        #if (passed == False):
            

        #Logic to put created username and password into user_db
    
    def check_match(self, password1, password2):
        if (password1 == password2):
            return True
        else:
            return False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StartWindow()
    window.showFullScreen()  # Show the window in fullscreen mode
    sys.exit(app.exec())
