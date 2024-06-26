from database import web_scraper
import home_window_UI
import user_session_info
from database import db_connect_user
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QGridLayout, QMessageBox
from PyQt6.QtGui import QFont, QGuiApplication
from PyQt6.QtCore import Qt
import on_logon_functions
import database.matches_to_database


class StartWindow(QMainWindow):
    #Initializes main window and calls initStartUI() function
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 600)  # Set initial geometry to cover the whole screen
        self.setCentralWidget(QWidget())  # Central widget for the layout
        self.setStyleSheet("background-color: #f0f0f0;")  # Set background color

        self.initstartUI()

    #Creates primary window
    def initstartUI(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)  # Center-align widgets
        self.centralWidget().setLayout(layout)

        #Create fonts to be used
        font1 = QFont()
        font1.setPointSize(16)

        font2 = QFont()
        font2.setPointSize(20)

        #Display welcome message
        label_welcome_mess = QLabel("Welcome to our betting app, please login if you have an existing account or sign-up to create a new one")
        label_welcome_mess.setFont(font2)
        
        layout.addWidget(label_welcome_mess)

        #Create Login and Sign-up Buttons
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
    
    #Routes to login page when button is clicked
    def login_click(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

    #Routes to sign-up page when button is clicked
    def signup_click(self):
        self.signin_window = SignInWindow()
        self.signin_window.show()
        self.close()
    

class LoginWindow(QMainWindow):
    #Initializes login window and classes loginUI() function to initialize window
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Page")
        self.setGeometry(0, 0, 800, 600)  # Set initial geometry to cover the whole screen
        self.setCentralWidget(QWidget())  # Central widget for the layout
        self.setStyleSheet("background-color: #f0f0f0;")  # Set background color

        self.loginUI()

    #Creates login page
    def loginUI(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)  # Center-align widgets

        self.centralWidget().setLayout(layout)

        font2 = QFont()
        font2.setPointSize(20)

        #Create login "form"
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

    #Routes back to main window when clicked
    def back_click(self):
        self.start_window = StartWindow()
        self.start_window.show()
        self.close()

    #When clicked, checks user credentials in database and if they exist, initialize app and route to app homepage
    def submit_click(self, layout):
        username = self.username.text()
        password = self.password.text()

        db = db_connect_user.ConnectDbUser()

       # Logic to check user credentials against user_db
        if(db.check_userandpass(username, password)):
            #If passed, route to main application window
            #Set global username
            user_session_info.session_username = username

            # Initialization functions
            on_logon_functions.check_balance(username)
            on_logon_functions.update_tables()
            on_logon_functions.check_if_settled_and_pay(username)

            self.home_window = home_window_UI.Ui_MainWindow()
            self.home_window.show()
            self.close()
        else:
            QMessageBox.warning(self, 'Error', 'Error: User credentials not found in database, please check your username and password and try again')


class SignInWindow(QMainWindow):
    #Initializes sign-in window and calls signInUI() to create main window
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sign-Up Page")
        self.setGeometry(0, 0, 800, 600)  # Set initial geometry to cover the whole screen
        self.setCentralWidget(QWidget())  # Central widget for the layout
        self.setStyleSheet("background-color: #f0f0f0;")  # Set background color

        self.signInUI()
    
    #Creates sign-in page
    def signInUI(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)  # Center-align widgets
        self.centralWidget().setLayout(layout)

        font2 = QFont()
        font2.setPointSize(20)

        #Create sign-in form
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

    #Routes back to main window when clicked
    def back_click(self):
        self.start_window = StartWindow()
        self.start_window.show()
        self.close()     
    
    #Checks to see if passwords match and enter new login credentials into database
    def submit_click(self):
        username = self.username.text()
        password = self.password.text()  
        password_check = self.password2.text()

        db = db_connect_user.ConnectDbUser()

        passed = self.check_match(password, password_check)
        if (passed == False):
            #display message that passwords don't match
            QMessageBox.warning(self, 'Error', 'Error: Passwords do not match, please try again')
        else:  
            #logic to put created username and password into user_db
            status = db.add_new_user(username, password)
            match (status):
                case 0:
                    QMessageBox.information(self, 'Success', 'Success: User credentials successfully created, please login to access your account')
                case 1:
                    QMessageBox.warning(self, 'Error', 'Error: User credentials already exist, please choose a new username and password')
                case _:
                    QMessageBox.warning(self, 'Error', 'Error: Unknown error creating user credentials, please try again')

    #Checks if passwords match
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
