from PyQt6.QtWidgets import (
        QApplication, QWidget, QPushButton, 
        QLabel, QLineEdit, QVBoxLayout, QGridLayout
)
from PyQt6.QtCore import Qt
import sys

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Page")
        self.setContentsMargins(20, 20, 20, 20)

        layout = QGridLayout()
        self.setLayout(layout)

        self.label1 = QLabel("Username: ")
        layout.addWidget(self.label1, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter)

        self.label2 = QLabel("Password: ")
        layout.addWidget(self.label2, 1, 0, alignment=Qt.AlignmentFlag.AlignCenter)

        self.input1 = QLineEdit()
        self.input1.setFixedWidth(200)
        layout.addWidget(self.input1, 0, 1, alignment=Qt.AlignmentFlag.AlignCenter)

        self.input2 = QLineEdit()
        self.input2.setFixedWidth(200)
        layout.addWidget(self.input2, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)

        button = QPushButton("Submit")
        button.setFixedWidth(50)
        button.clicked.connect(self.display)
        layout.addWidget(button, 2, 1, Qt.AlignmentFlag.AlignRight)

    def display(self):
        print(self.input1.text())
        print(self.input2.text())

app = QApplication(sys.argv) 
window = LoginWindow()
window.show()
sys.exit(app.exec())