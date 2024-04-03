from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
import sys
from home_window_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

