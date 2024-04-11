from PyQt6.QtWidgets import (
        QApplication, QWidget, QPushButton, 
        QLabel, QLineEdit, QVBoxLayout, QGridLayout, QMainWindow
)
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Page")
        self.setGeometry(0, 0, 800, 600)
        self.setCentralWidget(QWidget())
        self.setStyleSheet("background-color: #f0f0f0;")

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(0, 0, 0, 0)
        #layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.centralWidget().setLayout(layout)

        font = QFont()
        font.setPointSize(16)

        #Header label
        label_header = QLabel("Welcome to our betting app, please login if you have an existing account or sign-up to create a new account")
        label_header.setFont(font)
        label_header.setFixedHeight(20)
        layout.addWidget(label_header, alignment=Qt.AlignmentFlag.AlignCenter)

        #Login button
        login_button = QPushButton("Login")
        login_button.setFixedWidth(500)
        login_button.setFixedHeight(50)
        login_button.setFont(font)
        login_button.setStyleSheet("padding: 10px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 5px;")
        layout.addWidget(login_button, alignment=Qt.AlignmentFlag.AlignCenter)

        #Sign-up button
        signup_button = QPushButton("Sign-up")
        signup_button.setFixedWidth(500)
        signup_button.setFixedHeight(50)
        signup_button.setFont(font)
        signup_button.setStyleSheet("padding: 10px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 5px;")
        layout.addWidget(signup_button, alignment=Qt.AlignmentFlag.AlignCenter)
        

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Page")
        self.setGeometry(0, 0, 800, 600)
        self.setCentralWidget(QWidget())
        self.setStyleSheet("background-color: #f0f0f0;")

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.centralWidget().setLayout(layout)

        font = QFont()
        font.setPointSize(16)

        #Username label
        label_username = QLabel("Username:")
        label_username.setFont(font)
        layout.addWidget(label_username)

        #Username input
        input_username = QLineEdit()
        input_username.setFont(font)
        input_username.setFixedWidth(300)
        layout.addWidget(input_username)

        #Password label
        label_password = QLabel("Password:")
        label_password.setFont(font)
        layout.addWidget(label_password)

        #Password input
        input_password = QLineEdit()
        input_password.setFont(font)
        input_password.setEchoMode(QLineEdit.EchoMode.Password)
        input_password.setFixedWidth(300)
        layout.addWidget(input_password)

        #Login button
        login_button = QPushButton("Login")
        login_button.setFont(font)
        login_button.setStyleSheet("padding: 10px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 5px;")
        layout.addWidget(login_button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.showFullScreen()
    sys.exit(app.exec())
