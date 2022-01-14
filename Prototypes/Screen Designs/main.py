import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MainMenu import Ui_MainMenu
from Login import Ui_LoginScreen
from SignUp import Ui_SignUpScreen
from ForgottenPassword import Ui_ForgottenPasswordScreen
from ForgottenPassword2 import Ui_ForgottenPassword2Screen
from ResetPassword import Ui_ResetPasswordScreen
from ResetPassword2 import Ui_ResetPassword2Screen


class ResetPassword2(QtWidgets.QDialog):

    def __init__(self):
        super(ResetPassword2, self).__init__()
        self.ui = Ui_ResetPassword2Screen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)

        self.show()


class ResetPassword(QtWidgets.QDialog):

    def __init__(self):
        super(ResetPassword, self).__init__()
        self.ui = Ui_ResetPasswordScreen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)

        self.ui.LoginTab.clicked.connect(self.goto_login)
        self.ui.SignUpTab.clicked.connect(self.goto_signup)
        self.ui.ForgottenPasswordTab.clicked.connect(self.goto_forgotten_password)

        self.ui.SubmitButton.clicked.connect(self.submit)

        self.show()

    def goto_login(self):
        self.login = Login()
        self.hide()

    def goto_signup(self):
        self.signup = SignUp()
        self.hide()

    def goto_forgotten_password(self):
        self.forgotten_password = ForgottenPassword()
        self.hide()

    def submit(self):
        # Confirm Sign In
        self.reset_password_2 = ResetPassword2()
        self.hide()


class ForgottenPassword2(QtWidgets.QDialog):

    def __init__(self):
        super(ForgottenPassword2, self).__init__()
        self.ui = Ui_ForgottenPassword2Screen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)

        self.ui.LoginTab.clicked.connect(self.goto_login)
        self.ui.SignUpTab.clicked.connect(self.goto_signup)
        self.ui.ResetPasswordTab.clicked.connect(self.goto_reset_password)

        self.ui.SubmitButton.clicked.connect(self.submit)

        self.show()

    def goto_login(self):
        self.login = Login()
        self.hide()

    def goto_signup(self):
        self.signup = SignUp()
        self.hide()

    def goto_reset_password(self):
        self.reset_password = ResetPassword()
        self.hide()

    def submit(self):
        # Check verification code
        self.reset_password_2 = ResetPassword2()
        self.hide()


class ForgottenPassword(QtWidgets.QDialog):

    def __init__(self):
        super(ForgottenPassword, self).__init__()
        self.ui = Ui_ForgottenPasswordScreen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)

        self.ui.LoginTab.clicked.connect(self.goto_login)
        self.ui.SignUpTab.clicked.connect(self.goto_signup)
        self.ui.ResetPasswordTab.clicked.connect(self.goto_reset_password)

        self.ui.SubmitButton.clicked.connect(self.submit)

        self.show()

    def goto_login(self):
        self.login = Login()
        self.hide()

    def goto_signup(self):
        self.signup = SignUp()
        self.hide()

    def goto_reset_password(self):
        self.reset_password = ResetPassword()
        self.hide()

    def submit(self):
        # Send Email
        self.forgotten_password_2 = ForgottenPassword2()
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
        self.ui.ResetPasswordTab.clicked.connect(self.goto_reset_password)

        self.show()

    def goto_login(self):
        self.login = Login()
        self.hide()

    def goto_forgotten_password(self):
        self.forgotten_password = ForgottenPassword()
        self.hide()

    def goto_reset_password(self):
        self.reset_password = ResetPassword()
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
        self.ui.ResetPasswordTab.clicked.connect(self.goto_reset_password)

        self.ui.SubmitButton.clicked.connect(self.submit)

        self.show()

    def goto_signup(self):
        self.signup = SignUp()
        self.hide()

    def goto_forgotten_password(self):
        self.forgotten_password = ForgottenPassword()
        self.hide()

    def goto_reset_password(self):
        self.reset_password = ResetPassword()
        self.hide()

    def submit(self):
        username = self.ui.UsernameInput.text()
        password  = self.ui.PasswordInput.text()
        self.ui.ErrorLabel.setText("Error")


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
