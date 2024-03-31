from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
import sys
from home_window_ui import Ui_MainWindow
from nhl_window_ui import nhl_MainWindow

def nhl_clicked():
    nhl_app = QApplication([])
    nhl_window = QMainWindow()
    nhl_ui = nhl_MainWindow()
    nhl_ui.setupUi(nhl_window)
    nhl_window.show()
    sys.exit(nhl_app.exec())

class home_UI (QWidget):
    def __init__(self):
        super().__init__()

        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.main_ui.pushButton_6.clicked.connect(nhl_clicked())


if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    app.exec()

    # TODO: James, insert database connection stuff here. I'm not sure if this is where it will go in the final
    #  product, but just insert it here for now and I will move it later if I need to. If you have any trouble with
    #   anything, please lmk, I'm happy to help. Or even if you wanna just tell me what I'm supposed to do to link it
    #   to the DB and I can do it myself too if you are having issues.



