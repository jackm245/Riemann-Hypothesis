# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ForgottenPassword.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ForgottenPasswordScreen(object):
    def setupUi(self, ForgottenPasswordScreen):
        ForgottenPasswordScreen.setObjectName("ForgottenPasswordScreen")
        ForgottenPasswordScreen.resize(1340, 720)
        ForgottenPasswordScreen.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(ForgottenPasswordScreen)
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
"font: 36pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.LoginTab.setObjectName("LoginTab")
        self.SignUpTab = QtWidgets.QPushButton(self.TabBar)
        self.SignUpTab.setGeometry(QtCore.QRect(220, 5, 200, 70))
        self.SignUpTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SignUpTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 36pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.SignUpTab.setObjectName("SignUpTab")
        self.ForgottenPasswordTab = QtWidgets.QPushButton(self.TabBar)
        self.ForgottenPasswordTab.setGeometry(QtCore.QRect(430, 5, 200, 70))
        self.ForgottenPasswordTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ForgottenPasswordTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239);\n"
"font: 12pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"")
        self.ForgottenPasswordTab.setObjectName("ForgottenPasswordTab")
        self.ResetPasswordTab = QtWidgets.QPushButton(self.TabBar)
        self.ResetPasswordTab.setGeometry(QtCore.QRect(640, 5, 200, 70))
        self.ResetPasswordTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ResetPasswordTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 20pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.ResetPasswordTab.setObjectName("ResetPasswordTab")
        self.MainWidget = QtWidgets.QWidget(self.widget)
        self.MainWidget.setGeometry(QtCore.QRect(10, 170, 1320, 540))
        self.MainWidget.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius: 20px;")
        self.MainWidget.setObjectName("MainWidget")
        self.EmailText = QtWidgets.QLabel(self.MainWidget)
        self.EmailText.setGeometry(QtCore.QRect(300, 130, 301, 61))
        self.EmailText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.EmailText.setObjectName("EmailText")
        self.EmailInput = QtWidgets.QLineEdit(self.MainWidget)
        self.EmailInput.setGeometry(QtCore.QRect(720, 130, 361, 60))
        self.EmailInput.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\";\n"
"border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);")
        self.EmailInput.setText("")
        self.EmailInput.setCursorPosition(0)
        self.EmailInput.setObjectName("EmailInput")
        self.SubmitButton = QtWidgets.QPushButton(self.MainWidget)
        self.SubmitButton.setGeometry(QtCore.QRect(570, 440, 200, 70))
        self.SubmitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SubmitButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 36pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.SubmitButton.setObjectName("SubmitButton")

        self.retranslateUi(ForgottenPasswordScreen)
        QtCore.QMetaObject.connectSlotsByName(ForgottenPasswordScreen)

    def retranslateUi(self, ForgottenPasswordScreen):
        _translate = QtCore.QCoreApplication.translate
        ForgottenPasswordScreen.setWindowTitle(_translate("ForgottenPasswordScreen", "Visualising the Riemann Hypothesis - Forgotten Password"))
        self.Title.setText(_translate("ForgottenPasswordScreen", "Login"))
        self.LoginTab.setText(_translate("ForgottenPasswordScreen", "Login"))
        self.SignUpTab.setText(_translate("ForgottenPasswordScreen", "Sign Up"))
        self.ForgottenPasswordTab.setText(_translate("ForgottenPasswordScreen", "Forgotten Password"))
        self.ResetPasswordTab.setText(_translate("ForgottenPasswordScreen", "Reset Password"))
        self.EmailText.setText(_translate("ForgottenPasswordScreen", "<html><head/><body><p align=\"right\">Email:</p></body></html>"))
        self.EmailInput.setPlaceholderText(_translate("ForgottenPasswordScreen", "Enter Email"))
        self.SubmitButton.setText(_translate("ForgottenPasswordScreen", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ForgottenPasswordScreen = QtWidgets.QDialog()
    ui = Ui_ForgottenPasswordScreen()
    ui.setupUi(ForgottenPasswordScreen)
    ForgottenPasswordScreen.show()
    sys.exit(app.exec_())
