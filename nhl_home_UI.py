# Form implementation generated from reading ui file '.\nhl_home.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt6.QtWidgets import QApplication, QMainWindow

import home_window_UI
from database import db_upcoming_matches
from place_bet_window import PlaceBetInputWindow
import user_session_info


from PyQt6 import QtCore, QtGui, QtWidgets

from functools import partial
from on_logon_functions import check_time


class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #f0f0f0;")  # Set background color


        self.setupUi()


    def setupUi(self):
        self.resize(925, 664)
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.page_title = QtWidgets.QLabel(parent=self.centralwidget)
        self.page_title.setObjectName("page_title")
        self.verticalLayout.addWidget(self.page_title, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 905, 546))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # connect to database
        db = db_upcoming_matches.ConnectDbUpcomingMatch()

        # Create game objects dynamically
        for game in db.get_all_matches():
            if game[7] == 'NHL':

                # create gamebox object. this is where game contents will be saved
                self.gamebox = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents_2)
                self.gamebox.setMaximumSize(QtCore.QSize(16777215, 100))
                self.gamebox.setTitle("")
                self.gamebox.setObjectName("gamebox")

                # set layout for the widgets inside of the gamebox as horizontal
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.gamebox)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")

                # title of the matchup
                self.matchup_label = QtWidgets.QLabel(parent=self.gamebox)
                self.matchup_label.setObjectName("matchup_label")
                self.matchup_label.setText(str(game.away) + " @ " + str(game.home))
                self.horizontalLayout_2.addWidget(self.matchup_label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)

                # Date and time
                self.matchup_label_date = QtWidgets.QLabel(parent=self.gamebox)
                self.matchup_label_date.setObjectName("matchup_label")
                self.matchup_label_date.setText(str(game.date) + " @ " + str(game.time))
                self.horizontalLayout_2.addWidget(self.matchup_label_date, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)

                # If true the game has not started yet, so display buttons to allow user to bet on
                if check_time(game.time, game.date):
                    # create moneyline button for 1st team
                    self.moneyline_home = QtWidgets.QPushButton(parent=self.gamebox)
                    self.moneyline_home.setObjectName("moneyline_home")
                    # call button function to get individual game data
                    self.moneyline_home.clicked.connect(partial(self.place_bet_home_games, game))
                    self.moneyline_home.setText(f"{game[1]}: {game[2]}")
                    self.horizontalLayout_2.addWidget(self.moneyline_home)

                    # create moneyline button for 2nd team
                    self.moneyline_away = QtWidgets.QPushButton(parent=self.gamebox)
                    self.moneyline_away.setObjectName("moneyline_away")
                    # call button function to get individual game data
                    self.moneyline_away.clicked.connect(partial(self.place_bet_away_games, game))
                    self.horizontalLayout_2.addWidget(self.moneyline_away)
                    self.moneyline_away.setText(f"{game[3]}: {game[4]}")
                else:
                    # create moneyline button for 1st team
                    self.moneyline_home = QtWidgets.QLabel(parent=self.gamebox)
                    self.moneyline_home.setObjectName("moneyline_home")
                    self.moneyline_home.setText(f"{game[1]}: {game[2]}")
                    self.horizontalLayout_2.addWidget(self.moneyline_home)

                    # create moneyline button for 2nd team
                    self.moneyline_away = QtWidgets.QLabel(parent=self.gamebox)
                    self.moneyline_away.setObjectName("moneyline_away")
                    self.horizontalLayout_2.addWidget(self.moneyline_away)
                    self.moneyline_away.setText(f"{game[3]}: {game[4]}")

                # add the gamebox to the scroll area
                self.verticalLayout_2.addWidget(self.gamebox)
                self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
                self.verticalLayout.addWidget(self.scrollArea)


        self.toolbar_box = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.toolbar_box.setMinimumSize(QtCore.QSize(0, 60))
        self.toolbar_box.setMaximumSize(QtCore.QSize(16777215, 60))
        self.toolbar_box.setTitle("")
        self.toolbar_box.setObjectName("toolbar_box")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.toolbar_box)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.home_button = QtWidgets.QPushButton(parent=self.toolbar_box)
        self.home_button.setObjectName("home_button")
        self.home_button.setStyleSheet("padding: 10px 20px; background-color: BlueViolet; color: white; border: none; border-radius: 5px;")
        self.horizontalLayout.addWidget(self.home_button)
        self.verticalLayout.addWidget(self.toolbar_box)
        self.setCentralWidget(self.centralwidget)

        self.home_button.clicked.connect(self.home_button_clicked)


        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def place_bet_home_games(self, game):
        """
        Shows user the window to place bet for home team
        :param game:
        :return:
        """
        self.place_bet_window = PlaceBetInputWindow(user_session_info.session_username, game.id, game.home_odds, game.home)
        self.place_bet_window.show()

    def place_bet_away_games(self, game):
        """
        Shows user the window to place bet for away team
        :param game:
        :return:
        """
        self.place_bet_window = PlaceBetInputWindow(user_session_info.session_username, game.id, game.away_odds, game.away)
        self.place_bet_window.show()

    def home_button_clicked(self):
        self.home_window = home_window_UI.Ui_MainWindow()
        self.home_window.show()
        self.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.page_title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">NHL Home</span></p></body></html>"))
        self.matchup_label.setText(_translate("MainWindow", "Team A vs Team B"))
        self.home_button.setText(_translate("MainWindow", "Home"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec())