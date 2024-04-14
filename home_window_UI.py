# Form implementation generated from reading ui file 'home_window.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication
import nhl_home_UI, nba_home_UI, mlb_home_UI

class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi()

    def setupUi(self):
        # MainWindow.setObjectName("MainWindow")
        # MainWindow.setEnabled(True)
        self.resize(788, 660)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_main_groupBox")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 44))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.verticalLayout_2.addWidget(self.groupBox, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.MenuItems = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.MenuItems.setMaximumSize(QtCore.QSize(16777215, 50))
        self.MenuItems.setTitle("")
        self.MenuItems.setObjectName("MenuItems")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.MenuItems)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.MenuItems)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_home")
        self.horizontalLayout.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.pushButton = QtWidgets.QPushButton(parent=self.MenuItems)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.MenuItems)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.verticalLayout_2.addWidget(self.MenuItems)
        self.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Welcome to the Software SportsBook</span></p><p align=\"center\"><br/></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "Sports"))
        self.pushButton_5.setText(_translate("MainWindow", "NBA"))
        self.pushButton_6.setText(_translate("MainWindow", "NHL"))
        self.pushButton_4.setText(_translate("MainWindow", "MLB"))
        self.pushButton_2.setText(_translate("MainWindow", "{balance}"))
        self.pushButton.setText(_translate("MainWindow", "Home"))
        self.pushButton_3.setText(_translate("MainWindow", "My Bets"))

        self.pushButton_6.clicked.connect(self.nhl_clicked)

        self.pushButton_5.clicked.connect(self.nba_clicked)

        self.pushButton_4.clicked.connect(self.mlb_clicked)



    def nhl_clicked(self):
        self.nhl_window = nhl_home_UI.Ui_MainWindow()
        self.nhl_window.show()
        self.close()

    def nba_clicked(self):
        self.nba_window = nba_home_UI.Ui_MainWindow()
        self.nba_window.show()
        self.close()

    def mlb_clicked(self):
        self.mlb_window = mlb_home_UI.Ui_MainWindow()
        self.mlb_window.show()
        self.close()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec())
