from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('SoftEng Sports Book')
        self.setWindowIcon(QIcon('C:/Users/mason.LAPTOP-5MD6OBTH/Downloads/fanduel_icon'))
        self.setStyleSheet('background-color: grey')


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
