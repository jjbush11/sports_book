from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
import sys
from home_window_ui import Ui_MainWindow
from nhl_window_ui import nhl_MainWindow


class home_UI (QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_home_window()

    def initialize_home_window(self):
        home_window = QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(home_window)
        home_window.show()
        app.exec()

        ui.pushButton_6.clicked.connect(self.nhl_clicked())

    def nhl_clicked(self):
        self.nhl_window = nhl_Window()
        self.window.show()
        self.close()


class nhl_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_nhl_window()

    def initialize_nhl_window(self):
        nhl_app = QApplication([])
        nhl_window = QMainWindow()
        nhl_ui = nhl_MainWindow()
        nhl_ui.setupUi(nhl_window)
        nhl_window.show()
        sys.exit(nhl_app.exec())

        # TODO: James, insert database connection stuff here. I'm not sure if this is where it will go in the final
        #  product, but just insert it here for now and I will move it later if I need to. If you have any trouble with
        #   anything, please lmk, I'm happy to help. Or even if you wanna just tell me what I'm supposed to do to link it
        #   to the DB and I can do it myself too if you are having issues.

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = home_UI()
    window.show()
    sys.exit(app.exec())






