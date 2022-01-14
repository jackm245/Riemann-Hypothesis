import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from homescreen import Ui_MainMenu
from login import Ui_LoginScreen
from signup import Ui_SignUpScreen
from ForgottenPassword import Ui_ForgottenPasswordScreen

class ForgottenPassword(QtWidgets.QDialog):

    def __init__(self):
        super(ForgottenPassword, self).__init__()
        self.ui = Ui_ForgottenPasswordScreen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)
        self.ui.LoginTab.clicked.connect(self.goto_login)
        self.ui.SignUpTab.clicked.connect(self.goto_signup)
        self.show()

    def goto_login(self):
        self.login = Login()
        self.hide()

    def goto_signup(self):
        self.singup = SignUp()
        self.hide()

class SignUp(QtWidgets.QDialog):

    def __init__(self):
        super(SignUp, self).__init__()
        self.ui = Ui_SignUpScreen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)
        self.ui.LoginTab.clicked.connect(self.goto_login)
        self.ui.ForgottenPasswordTab.clicked.connect(self.goto_forgotten_password)
        self.show()

    def goto_login(self):
        self.login = Login()
        self.hide()

    def goto_forgotten_password(self):
        self.forgotten_password = ForgottenPassword()
        self.hide()


class Login(QtWidgets.QDialog):

    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)
        self.ui.SignUpTab.clicked.connect(self.goto_signup)
        self.ui.ForgottenPasswordTab.clicked.connect(self.goto_forgotten_password)
        self.ui.SubmitButton.clicked.connect(self.submit)
        self.show()

    def goto_signup(self):
        self.singup = SignUp()
        self.hide()

    def goto_forgotten_password(self):
        self.forgotten_password = ForgottenPassword()
        self.hide()

    def submit(self):
        pass


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)
        self.ui.LogInButton.clicked.connect(self.goto_login)
        self.ui.ExitButton.clicked.connect(self.exit)
        self.show()

    def goto_login(self):
        self.login = Login()
        self.hide()

    def exit(self):
        sys.exit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = Main()
    sys.exit(app.exec())
