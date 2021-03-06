"""
main_menu.py
============
A GUI for the main menu page
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainMenu(object):

    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.setEnabled(True)
        MainMenu.resize(1340, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainMenu.sizePolicy().hasHeightForWidth())
        MainMenu.setSizePolicy(sizePolicy)
        self.MainWidget = QtWidgets.QWidget(MainMenu)
        self.MainWidget.setGeometry(QtCore.QRect(0, 0, 1340, 720))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainWidget.sizePolicy().hasHeightForWidth())
        self.MainWidget.setSizePolicy(sizePolicy)
        self.MainWidget.setObjectName("MainWidget")
        self.SideWidget = QtWidgets.QWidget(self.MainWidget)
        self.SideWidget.setGeometry(QtCore.QRect(-50, 0, 512, 720))
        self.SideWidget.setStyleSheet("background-color:rgb(69, 69, 69) ;\n"
"border-radius:40px;")
        self.SideWidget.setObjectName("SideWidget")
        self.Title = QtWidgets.QLabel(self.SideWidget)
        self.Title.setGeometry(QtCore.QRect(70, 30, 421, 121))
        self.Title.setStyleSheet("font: 36pt \"Sans Serif\"; color:rgb(239, 239, 239)")
        self.Title.setObjectName("Title")
        self.InvestigationButton = QtWidgets.QPushButton(self.SideWidget)
        self.InvestigationButton.setGeometry(QtCore.QRect(170, 410, 231, 61))
        self.InvestigationButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.InvestigationButton.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:20px;\n"
"font: 18pt \"Sans Serif\";")
        self.InvestigationButton.setObjectName("InvestigationButton")
        self.LogInButton = QtWidgets.QPushButton(self.SideWidget)
        self.LogInButton.setGeometry(QtCore.QRect(170, 170, 231, 61))
        self.LogInButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LogInButton.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:20px;\n"
"font: 18pt \"Sans Serif\";")
        self.LogInButton.setCheckable(False)
        self.LogInButton.setChecked(False)
        self.LogInButton.setObjectName("LogInButton")
        self.TutorialButton = QtWidgets.QPushButton(self.SideWidget)
        self.TutorialButton.setGeometry(QtCore.QRect(170, 250, 231, 61))
        self.TutorialButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TutorialButton.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:20px;\n"
"font: 18pt \"Sans Serif\";")
        self.TutorialButton.setObjectName("TutorialButton")
        self.IntroductionButton = QtWidgets.QPushButton(self.SideWidget)
        self.IntroductionButton.setGeometry(QtCore.QRect(170, 330, 231, 61))
        self.IntroductionButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.IntroductionButton.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:20px;\n"
"font: 18pt \"Sans Serif\";")
        self.IntroductionButton.setObjectName("IntroductionButton")
        self.SummaryButton = QtWidgets.QPushButton(self.SideWidget)
        self.SummaryButton.setGeometry(QtCore.QRect(170, 490, 231, 61))
        self.SummaryButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SummaryButton.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:20px;\n"
"font: 18pt \"Sans Serif\";")
        self.SummaryButton.setObjectName("SummaryButton")
        self.ExitButton = QtWidgets.QPushButton(self.SideWidget)
        self.ExitButton.setGeometry(QtCore.QRect(170, 570, 231, 61))
        self.ExitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ExitButton.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:20px;\n"
"font: 18pt \"Sans Serif\";")
        self.ExitButton.setObjectName("ExitButton")
        self.BackgroundImage = QtWidgets.QLabel(self.MainWidget)
        self.BackgroundImage.setGeometry(QtCore.QRect(0, 0, 1340, 720))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BackgroundImage.sizePolicy().hasHeightForWidth())
        self.BackgroundImage.setSizePolicy(sizePolicy)
        self.BackgroundImage.setText("")
        self.BackgroundImage.setPixmap(QtGui.QPixmap("ui/../media/zeta-graph.jpg"))
        self.BackgroundImage.setScaledContents(True)
        self.BackgroundImage.setObjectName("BackgroundImage")
        self.UsernameButton = QtWidgets.QPushButton(self.MainWidget)
        self.UsernameButton.setGeometry(QtCore.QRect(1140, 20, 180, 50))
        self.UsernameButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.UsernameButton.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:20px;\n"
"font: 15pt \"Sans Serif\";\n"
"padding:3px;")
        self.UsernameButton.setObjectName("UsernameButton")
        self.BackgroundImage.raise_()
        self.SideWidget.raise_()
        self.UsernameButton.raise_()

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "Visualing The Riemann Hypothesis - Main Menu"))
        self.Title.setText(_translate("MainMenu", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600;\">Visualising The</span></p><p align=\"center\"><span style=\" font-size:28pt; font-weight:600;\">Riemann Hypothesis</span></p></body></html>"))
        self.InvestigationButton.setText(_translate("MainMenu", "Investigation"))
        self.LogInButton.setText(_translate("MainMenu", "Log In"))
        self.TutorialButton.setText(_translate("MainMenu", "Tutorial"))
        self.IntroductionButton.setText(_translate("MainMenu", "Introduction"))
        self.SummaryButton.setText(_translate("MainMenu", "Summary"))
        self.ExitButton.setText(_translate("MainMenu", "Exit"))
        self.UsernameButton.setText(_translate("MainMenu", "Username"))
