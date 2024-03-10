import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

app = QApplication([])

window = QMainWindow()
window.statusBar().showMessage("Welcome to the SoftEng Sportsbook")

window.show()

sys.exit(app.exec())