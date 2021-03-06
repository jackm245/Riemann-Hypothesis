"""
login.py
========
A GUI for the login page of the login section
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginScreen(object):

    def setupUi(self, LoginScreen):
        LoginScreen.setObjectName("LoginScreen")
        LoginScreen.resize(1340, 720)
        LoginScreen.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(LoginScreen)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1340, 720))
        self.widget.setStyleSheet("background-color: rgb(69, 69, 69);")
        self.widget.setObjectName("widget")
        self.Title = QtWidgets.QLabel(self.widget)
        self.Title.setGeometry(QtCore.QRect(612, 20, 116, 51))
        self.Title.setStyleSheet("font: 36pt \"Sans Serif\"; color:rgb(239, 239, 239)")
        self.Title.setObjectName("Title")
        self.TabBar = QtWidgets.QWidget(self.widget)
        self.TabBar.setGeometry(QtCore.QRect(0, 80, 1340, 80))
        self.TabBar.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.TabBar.setObjectName("TabBar")
        self.LoginTab = QtWidgets.QPushButton(self.TabBar)
        self.LoginTab.setGeometry(QtCore.QRect(10, 5, 200, 70))
        self.LoginTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LoginTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239);\n"
"font: 18pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"")
        self.LoginTab.setObjectName("LoginTab")
        self.SignUpTab = QtWidgets.QPushButton(self.TabBar)
        self.SignUpTab.setGeometry(QtCore.QRect(220, 5, 200, 70))
        self.SignUpTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SignUpTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"padding: 7px;\n"
"")
        self.SignUpTab.setObjectName("SignUpTab")
        self.ResetPasswordTab = QtWidgets.QPushButton(self.TabBar)
        self.ResetPasswordTab.setGeometry(QtCore.QRect(640, 5, 200, 70))
        self.ResetPasswordTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ResetPasswordTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.ResetPasswordTab.setObjectName("ResetPasswordTab")
        self.ForgottenPasswordTab = QtWidgets.QPushButton(self.TabBar)
        self.ForgottenPasswordTab.setGeometry(QtCore.QRect(430, 5, 200, 70))
        self.ForgottenPasswordTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ForgottenPasswordTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")
        self.ForgottenPasswordTab.setText("")
        self.ForgottenPasswordTab.setObjectName("ForgottenPasswordTab")
        self.ForgottenPasswordLabel = QtWidgets.QLabel(self.TabBar)
        self.ForgottenPasswordLabel.setGeometry(QtCore.QRect(430, 5, 200, 70))
        self.ForgottenPasswordLabel.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"padding: 7px;\n"
"")
        self.ForgottenPasswordLabel.setObjectName("ForgottenPasswordLabel")
        self.LoginTab.raise_()
        self.SignUpTab.raise_()
        self.ResetPasswordTab.raise_()
        self.ForgottenPasswordLabel.raise_()
        self.ForgottenPasswordTab.raise_()
        self.MainWidget = QtWidgets.QWidget(self.widget)
        self.MainWidget.setGeometry(QtCore.QRect(10, 170, 1320, 540))
        self.MainWidget.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius: 20px;")
        self.MainWidget.setObjectName("MainWidget")
        self.UsernameOrEmailText = QtWidgets.QLabel(self.MainWidget)
        self.UsernameOrEmailText.setGeometry(QtCore.QRect(300, 130, 301, 61))
        self.UsernameOrEmailText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.UsernameOrEmailText.setObjectName("UsernameOrEmailText")
        self.PasswordText = QtWidgets.QLabel(self.MainWidget)
        self.PasswordText.setGeometry(QtCore.QRect(320, 280, 281, 61))
        self.PasswordText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.PasswordText.setObjectName("PasswordText")
        self.UsernameInput = QtWidgets.QLineEdit(self.MainWidget)
        self.UsernameInput.setGeometry(QtCore.QRect(720, 130, 231, 60))
        self.UsernameInput.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\";\n"
"border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);")
        self.UsernameInput.setText("")
        self.UsernameInput.setCursorPosition(0)
        self.UsernameInput.setObjectName("UsernameInput")
        self.PasswordInput = QtWidgets.QLineEdit(self.MainWidget)
        self.PasswordInput.setGeometry(QtCore.QRect(720, 280, 231, 60))
        self.PasswordInput.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\";\n"
"border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);")
        self.PasswordInput.setText("")
        self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordInput.setCursorPosition(0)
        self.PasswordInput.setObjectName("PasswordInput")
        self.SubmitButton = QtWidgets.QPushButton(self.MainWidget)
        self.SubmitButton.setGeometry(QtCore.QRect(570, 440, 200, 70))
        self.SubmitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SubmitButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.SubmitButton.setObjectName("SubmitButton")
        self.ErrorLabel = QtWidgets.QLabel(self.MainWidget)
        self.ErrorLabel.setGeometry(QtCore.QRect(440, 350, 461, 71))
        self.ErrorLabel.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 18pt \"Sans Serif\";")
        self.ErrorLabel.setObjectName("ErrorLabel")
        self.ShowHideButton = QtWidgets.QPushButton(self.MainWidget)
        self.ShowHideButton.setGeometry(QtCore.QRect(980, 290, 111, 41))
        self.ShowHideButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ShowHideButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.ShowHideButton.setObjectName("ShowHideButton")
        self.BackButton = QtWidgets.QPushButton(self.MainWidget)
        self.BackButton.setGeometry(QtCore.QRect(10, 460, 200, 70))
        self.BackButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BackButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.BackButton.setObjectName("BackButton")

        self.retranslateUi(LoginScreen)
        QtCore.QMetaObject.connectSlotsByName(LoginScreen)

    def retranslateUi(self, LoginScreen):
        _translate = QtCore.QCoreApplication.translate
        LoginScreen.setWindowTitle(_translate("LoginScreen", "Visualising the Riemann Hypothesis - Log In"))
        self.Title.setText(_translate("LoginScreen", "Login"))
        self.LoginTab.setText(_translate("LoginScreen", "Login"))
        self.SignUpTab.setText(_translate("LoginScreen", "Sign Up"))
        self.ResetPasswordTab.setText(_translate("LoginScreen", "Reset Password"))
        self.ForgottenPasswordLabel.setText(_translate("LoginScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Forgotten<br/>Password</span></p></body></html>"))
        self.UsernameOrEmailText.setText(_translate("LoginScreen", "<html><head/><body><p align=\"right\">Username:</p></body></html>"))
        self.PasswordText.setText(_translate("LoginScreen", "<html><head/><body><p align=\"right\">Password:</p></body></html>"))
        self.UsernameInput.setPlaceholderText(_translate("LoginScreen", "Enter Username"))
        self.PasswordInput.setPlaceholderText(_translate("LoginScreen", "Enter Password"))
        self.SubmitButton.setText(_translate("LoginScreen", "Submit"))
        self.ErrorLabel.setText(_translate("LoginScreen", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.ShowHideButton.setText(_translate("LoginScreen", "Show"))
        self.BackButton.setText(_translate("LoginScreen", "Back"))
