"""
sign_up.py
==========
A GUI for the sign up page of the login section
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignUpScreen(object):

    def setupUi(self, SignUpScreen):
        SignUpScreen.setObjectName("SignUpScreen")
        SignUpScreen.resize(1340, 720)
        SignUpScreen.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(SignUpScreen)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1340, 720))
        self.widget.setStyleSheet("background-color: rgb(69, 69, 69);")
        self.widget.setObjectName("widget")
        self.Title = QtWidgets.QLabel(self.widget)
        self.Title.setGeometry(QtCore.QRect(612, 20, 121, 51))
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
"background-color: rgb(239, 239, 239);\n"
"font: 18pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
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
        self.UsernameOrEmailText.setGeometry(QtCore.QRect(270, 40, 301, 61))
        self.UsernameOrEmailText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.UsernameOrEmailText.setObjectName("UsernameOrEmailText")
        self.EmailText = QtWidgets.QLabel(self.MainWidget)
        self.EmailText.setGeometry(QtCore.QRect(290, 120, 281, 61))
        self.EmailText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.EmailText.setObjectName("EmailText")
        self.UsernameInput = QtWidgets.QLineEdit(self.MainWidget)
        self.UsernameInput.setGeometry(QtCore.QRect(680, 40, 231, 60))
        self.UsernameInput.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\";\n"
"border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);")
        self.UsernameInput.setText("")
        self.UsernameInput.setCursorPosition(0)
        self.UsernameInput.setObjectName("UsernameInput")
        self.EmailInput = QtWidgets.QLineEdit(self.MainWidget)
        self.EmailInput.setGeometry(QtCore.QRect(680, 120, 231, 60))
        self.EmailInput.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\";\n"
"border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);")
        self.EmailInput.setText("")
        self.EmailInput.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.EmailInput.setCursorPosition(0)
        self.EmailInput.setObjectName("EmailInput")
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
        self.PasswordText = QtWidgets.QLabel(self.MainWidget)
        self.PasswordText.setGeometry(QtCore.QRect(290, 200, 281, 61))
        self.PasswordText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.PasswordText.setObjectName("PasswordText")
        self.PasswordInput = QtWidgets.QLineEdit(self.MainWidget)
        self.PasswordInput.setGeometry(QtCore.QRect(680, 200, 231, 60))
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
        self.PasswordText_2 = QtWidgets.QLabel(self.MainWidget)
        self.PasswordText_2.setGeometry(QtCore.QRect(260, 280, 311, 61))
        self.PasswordText_2.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.PasswordText_2.setObjectName("PasswordText_2")
        self.PasswordInput_2 = QtWidgets.QLineEdit(self.MainWidget)
        self.PasswordInput_2.setGeometry(QtCore.QRect(680, 280, 231, 60))
        self.PasswordInput_2.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\";\n"
"border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);")
        self.PasswordInput_2.setText("")
        self.PasswordInput_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordInput_2.setCursorPosition(0)
        self.PasswordInput_2.setObjectName("PasswordInput_2")
        self.ErrorLabel = QtWidgets.QLabel(self.MainWidget)
        self.ErrorLabel.setGeometry(QtCore.QRect(365, 350, 611, 71))
        self.ErrorLabel.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 18pt \"Sans Serif\";")
        self.ErrorLabel.setObjectName("ErrorLabel")
        self.ShowHideButton_2 = QtWidgets.QPushButton(self.MainWidget)
        self.ShowHideButton_2.setGeometry(QtCore.QRect(940, 290, 111, 41))
        self.ShowHideButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ShowHideButton_2.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.ShowHideButton_2.setObjectName("ShowHideButton_2")
        self.ShowHideButton = QtWidgets.QPushButton(self.MainWidget)
        self.ShowHideButton.setGeometry(QtCore.QRect(940, 210, 111, 41))
        self.ShowHideButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ShowHideButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.ShowHideButton.setObjectName("ShowHideButton")

        self.retranslateUi(SignUpScreen)
        QtCore.QMetaObject.connectSlotsByName(SignUpScreen)

    def retranslateUi(self, SignUpScreen):
        _translate = QtCore.QCoreApplication.translate
        SignUpScreen.setWindowTitle(_translate("SignUpScreen", "Visualising the Riemann Hypothesis - Sign Up"))
        self.Title.setText(_translate("SignUpScreen", "Login"))
        self.LoginTab.setText(_translate("SignUpScreen", "Login"))
        self.SignUpTab.setText(_translate("SignUpScreen", "Sign Up"))
        self.ResetPasswordTab.setText(_translate("SignUpScreen", "Reset Password"))
        self.ForgottenPasswordLabel.setText(_translate("SignUpScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Forgotten<br/>Password</span></p></body></html>"))
        self.UsernameOrEmailText.setText(_translate("SignUpScreen", "<html><head/><body><p align=\"right\">Username:</p></body></html>"))
        self.EmailText.setText(_translate("SignUpScreen", "<html><head/><body><p align=\"right\">Email:</p></body></html>"))
        self.UsernameInput.setPlaceholderText(_translate("SignUpScreen", "Enter Username"))
        self.EmailInput.setPlaceholderText(_translate("SignUpScreen", "Enter Email"))
        self.SubmitButton.setText(_translate("SignUpScreen", "Submit"))
        self.PasswordText.setText(_translate("SignUpScreen", "<html><head/><body><p align=\"right\">Password:</p></body></html>"))
        self.PasswordInput.setPlaceholderText(_translate("SignUpScreen", "Enter Password"))
        self.PasswordText_2.setText(_translate("SignUpScreen", "<html><head/><body><p align=\"right\">Confirm Password:</p></body></html>"))
        self.PasswordInput_2.setPlaceholderText(_translate("SignUpScreen", "Re-enter Password"))
        self.ErrorLabel.setText(_translate("SignUpScreen", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.ShowHideButton_2.setText(_translate("SignUpScreen", "Show"))
        self.ShowHideButton.setText(_translate("SignUpScreen", "Show"))
