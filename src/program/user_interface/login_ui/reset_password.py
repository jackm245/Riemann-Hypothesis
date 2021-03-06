"""
reset_password.py
=================
A GUI for the reset password page of the login section
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ResetPasswordScreen(object):

    def setupUi(self, ResetPasswordScreen):
        ResetPasswordScreen.setObjectName("ResetPasswordScreen")
        ResetPasswordScreen.resize(1340, 720)
        ResetPasswordScreen.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(ResetPasswordScreen)
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
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
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
"")
        self.SignUpTab.setObjectName("SignUpTab")
        self.ResetPasswordTab = QtWidgets.QPushButton(self.TabBar)
        self.ResetPasswordTab.setGeometry(QtCore.QRect(640, 5, 200, 70))
        self.ResetPasswordTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ResetPasswordTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239);\n"
"font: 18pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"")
        self.ResetPasswordTab.setObjectName("ResetPasswordTab")
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
        self.ForgottenPasswordTab = QtWidgets.QPushButton(self.TabBar)
        self.ForgottenPasswordTab.setGeometry(QtCore.QRect(430, 5, 200, 70))
        self.ForgottenPasswordTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ForgottenPasswordTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")
        self.ForgottenPasswordTab.setText("")
        self.ForgottenPasswordTab.setObjectName("ForgottenPasswordTab")
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
        self.UsernameInput.setGeometry(QtCore.QRect(720, 130, 261, 60))
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
        self.PasswordInput.setGeometry(QtCore.QRect(720, 280, 261, 60))
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
        self.ShowHideButton = QtWidgets.QPushButton(self.MainWidget)
        self.ShowHideButton.setGeometry(QtCore.QRect(1010, 290, 111, 41))
        self.ShowHideButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ShowHideButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.ShowHideButton.setObjectName("ShowHideButton")
        self.ErrorLabel = QtWidgets.QLabel(self.MainWidget)
        self.ErrorLabel.setGeometry(QtCore.QRect(440, 350, 461, 71))
        self.ErrorLabel.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 18pt \"Sans Serif\";")
        self.ErrorLabel.setObjectName("ErrorLabel")

        self.retranslateUi(ResetPasswordScreen)
        QtCore.QMetaObject.connectSlotsByName(ResetPasswordScreen)

    def retranslateUi(self, ResetPasswordScreen):
        _translate = QtCore.QCoreApplication.translate
        ResetPasswordScreen.setWindowTitle(_translate("ResetPasswordScreen", "Visualising the Riemann Hypothesis - Reset Password"))
        self.Title.setText(_translate("ResetPasswordScreen", "Login"))
        self.LoginTab.setText(_translate("ResetPasswordScreen", "Login"))
        self.SignUpTab.setText(_translate("ResetPasswordScreen", "Sign Up"))
        self.ResetPasswordTab.setText(_translate("ResetPasswordScreen", "Reset Password"))
        self.ForgottenPasswordLabel.setText(_translate("ResetPasswordScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Forgotten<br/>Password</span></p></body></html>"))
        self.UsernameOrEmailText.setText(_translate("ResetPasswordScreen", "<html><head/><body><p align=\"right\">Username:</p></body></html>"))
        self.PasswordText.setText(_translate("ResetPasswordScreen", "<html><head/><body><p align=\"right\">Password:</p></body></html>"))
        self.UsernameInput.setPlaceholderText(_translate("ResetPasswordScreen", "Enter Username"))
        self.PasswordInput.setPlaceholderText(_translate("ResetPasswordScreen", "Enter Password"))
        self.SubmitButton.setText(_translate("ResetPasswordScreen", "Submit"))
        self.ShowHideButton.setText(_translate("ResetPasswordScreen", "Show"))
        self.ErrorLabel.setText(_translate("ResetPasswordScreen", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
