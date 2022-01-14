import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from homescreen import Ui_MainMenu
from login import Ui_LoginScreen
from signup import Ui_SignUpScreen


class SignUp(QtWidgets.QDialog):

    def __init__(self):
        super(SignUp, self).__init__()
        self.ui = Ui_SignUpScreen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)
        self.ui.LoginTab.clicked.connect(self.gotologin)
        self.show()

    def gotologin(self):
        self.login = Login()
        self.hide()


class Login(QtWidgets.QDialog):

    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)
        self.ui.SignUpTab.clicked.connect(self.gotosignup)
        self.show()

    def gotosignup(self):
        self.singup = SignUp()
        self.hide()


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)
        self.ui.LogInButton.clicked.connect(self.gotologin)
        self.ui.ExitButton.clicked.connect(self.exit)
        self.show()

    def gotologin(self):
        self.login = Login()
        self.hide()

    def exit(self):
        sys.exit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = Main()
    sys.exit(app.exec())
