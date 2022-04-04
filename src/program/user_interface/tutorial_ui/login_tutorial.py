"""
login_tutorial.py
=================
A GUI for the login tutorial page of the tutorial section
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginTutorialScreen(object):

    def setupUi(self, LoginTutorialScreen):
        LoginTutorialScreen.setObjectName("LoginTutorialScreen")
        LoginTutorialScreen.resize(1340, 723)
        LoginTutorialScreen.setToolTipDuration(0)
        LoginTutorialScreen.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(LoginTutorialScreen)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1340, 720))
        self.widget.setStyleSheet("background-color: rgb(69, 69, 69);")
        self.widget.setObjectName("widget")
        self.Title = QtWidgets.QLabel(self.widget)
        self.Title.setGeometry(QtCore.QRect(590, 20, 161, 51))
        self.Title.setStyleSheet("font: 36pt \"Sans Serif\"; color:rgb(239, 239, 239)")
        self.Title.setObjectName("Title")
        self.TabBar = QtWidgets.QWidget(self.widget)
        self.TabBar.setGeometry(QtCore.QRect(0, 80, 1340, 80))
        self.TabBar.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.TabBar.setObjectName("TabBar")
        self.TutorialTab = QtWidgets.QPushButton(self.TabBar)
        self.TutorialTab.setGeometry(QtCore.QRect(10, 5, 200, 70))
        self.TutorialTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TutorialTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.TutorialTab.setObjectName("TutorialTab")
        self.LoginTab = QtWidgets.QPushButton(self.TabBar)
        self.LoginTab.setGeometry(QtCore.QRect(430, 5, 221, 70))
        self.LoginTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LoginTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239);\n"
"font: 18pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"")
        self.LoginTab.setObjectName("LoginTab")
        self.IntroductionTab = QtWidgets.QPushButton(self.TabBar)
        self.IntroductionTab.setGeometry(QtCore.QRect(660, 5, 200, 70))
        self.IntroductionTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.IntroductionTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.IntroductionTab.setObjectName("IntroductionTab")
        self.InvestigationTab = QtWidgets.QPushButton(self.TabBar)
        self.InvestigationTab.setGeometry(QtCore.QRect(870, 5, 200, 70))
        self.InvestigationTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.InvestigationTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.InvestigationTab.setObjectName("InvestigationTab")
        self.SummaryTab = QtWidgets.QPushButton(self.TabBar)
        self.SummaryTab.setGeometry(QtCore.QRect(1080, 5, 200, 70))
        self.SummaryTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SummaryTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.SummaryTab.setObjectName("SummaryTab")
        self.ProgramStructureTab = QtWidgets.QPushButton(self.TabBar)
        self.ProgramStructureTab.setGeometry(QtCore.QRect(220, 5, 200, 70))
        self.ProgramStructureTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ProgramStructureTab.setStyleSheet("border-radius: 20px;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font: 18pt \"Sans Serif\";\n"
"")
        self.ProgramStructureTab.setText("")
        self.ProgramStructureTab.setObjectName("ProgramStructureTab")
        self.ProgramStructureLabel = QtWidgets.QLabel(self.TabBar)
        self.ProgramStructureLabel.setGeometry(QtCore.QRect(220, 5, 200, 70))
        self.ProgramStructureLabel.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.ProgramStructureLabel.setObjectName("ProgramStructureLabel")
        self.TutorialTab.raise_()
        self.LoginTab.raise_()
        self.IntroductionTab.raise_()
        self.InvestigationTab.raise_()
        self.SummaryTab.raise_()
        self.ProgramStructureLabel.raise_()
        self.ProgramStructureTab.raise_()
        self.MainWidget = QtWidgets.QWidget(self.widget)
        self.MainWidget.setGeometry(QtCore.QRect(10, 170, 1320, 540))
        self.MainWidget.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius: 20px;")
        self.MainWidget.setObjectName("MainWidget")
        self.PrevButton = QtWidgets.QPushButton(self.MainWidget)
        self.PrevButton.setGeometry(QtCore.QRect(10, 460, 200, 70))
        self.PrevButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PrevButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.PrevButton.setObjectName("PrevButton")
        self.NextButton = QtWidgets.QPushButton(self.MainWidget)
        self.NextButton.setGeometry(QtCore.QRect(1110, 460, 200, 70))
        self.NextButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NextButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.NextButton.setObjectName("NextButton")
        self.SubTitleText = QtWidgets.QLabel(self.MainWidget)
        self.SubTitleText.setGeometry(QtCore.QRect(40, 20, 311, 41))
        self.SubTitleText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.SubTitleText.setObjectName("SubTitleText")
        self.MainText = QtWidgets.QLabel(self.MainWidget)
        self.MainText.setGeometry(QtCore.QRect(40, 60, 1251, 391))
        self.MainText.setStyleSheet("font: 13pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.MainText.setWordWrap(True)
        self.MainText.setObjectName("MainText")
        self.SubTitleText.raise_()
        self.PrevButton.raise_()
        self.NextButton.raise_()
        self.MainText.raise_()

        self.retranslateUi(LoginTutorialScreen)
        QtCore.QMetaObject.connectSlotsByName(LoginTutorialScreen)

    def retranslateUi(self, LoginTutorialScreen):
        _translate = QtCore.QCoreApplication.translate
        LoginTutorialScreen.setWindowTitle(_translate("LoginTutorialScreen", "Visualising the Riemann Hypothesis - Tutorial"))
        self.Title.setText(_translate("LoginTutorialScreen", "Tutorial"))
        self.TutorialTab.setText(_translate("LoginTutorialScreen", "Tutorial"))
        self.LoginTab.setText(_translate("LoginTutorialScreen", "Login"))
        self.IntroductionTab.setText(_translate("LoginTutorialScreen", "Introduction"))
        self.InvestigationTab.setText(_translate("LoginTutorialScreen", "Investigation"))
        self.SummaryTab.setText(_translate("LoginTutorialScreen", "Summary"))
        self.ProgramStructureLabel.setText(_translate("LoginTutorialScreen", "<html><head/><body><p align=\"center\">Program<br/>Structure</p></body></html>"))
        self.PrevButton.setText(_translate("LoginTutorialScreen", "Prev"))
        self.NextButton.setText(_translate("LoginTutorialScreen", "Next"))
        self.SubTitleText.setText(_translate("LoginTutorialScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Login</span></p></body></html>"))
        self.MainText.setText(_translate("LoginTutorialScreen", "<html><head/><body><p>The Login section of this program allows you to sign in to an account.</p><p>The different options you have are: </p><p>Login In</p><p>Sign Up</p><p>Forgotten Password</p><p>Reset Password</p><p><br/></p><p>Although you can use this program without an account, once you create and sign in to an account you will be able to use this program to it\'s full extent. When signed into an account, you will be able to answer questions on the Riemann Hypothesis, make your own notes, and participate to the leaderboard</p></body></html>"))
