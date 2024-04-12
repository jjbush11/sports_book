from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
import sys
from home_window_UI import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec())

