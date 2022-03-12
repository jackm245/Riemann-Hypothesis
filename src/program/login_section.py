import sys
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from .user_interface import Ui_LoginScreen, Ui_SignUpScreen, Ui_ForgottenPasswordScreen, Ui_ForgottenPassword2Screen, Ui_ResetPasswordScreen, Ui_ResetPassword2Screen
from .utils import database_insert, database_select, encrypt_password, check_password
from time import sleep


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
        self.ui.SubmitButton.clicked.connect(self.submit)

        self.show()

    def submit(self):
        from .main_section import MainMenu
        self.username = self.ui.UsernameInput.text()
        self.email = self.ui.EmailInput.text()
        self.password  = self.ui.PasswordInput.text()
        self.confirm_password  = self.ui.PasswordInput_2.text()
        # check is of right form
        if not re.fullmatch('\w{1,20}', self.username):
            self.ui.ErrorLabel.setText("Username must be at 1-20 characters long\nand not contain special characters")
        elif not re.fullmatch('.+@.+\..+', self.email):
            self.ui.ErrorLabel.setText("Email address must be valid")
        elif not re.fullmatch('(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9]).{8,}', self.password):
            self.ui.ErrorLabel.setText("Password must contain lower case, upper case,\na number, and be at least 8 characters long")
        elif self.password != self.confirm_password:
            self.ui.ErrorLabel.setText("Passwords do not match")
        else:
            self.selection = database_select(['Username'], ['Users'])
            self.Usernames = set([row[0] for row in self.selection])
            if self.username in self.Usernames:
                self.ui.ErrorLabel.setText("Username already taken")
            else:
                self.selection = database_select(['Email'], ['Users'])
                self.Emails = set([row[0] for row in self.selection])
                if self.email in self.Emails:
                    self.ui.ErrorLabel.setText("Email already taken")
                else:
                    self.selection = database_select(['User_ID'], ['Users'])
                    self.User_IDs = set([row[0] for row in self.selection])
                    self.User_ID = self.get_user_id()
                    self.hashed_password = encrypt_password(self.password)
                    database_insert('Users', [self.User_ID, self.username, self.email, self.hashed_password])
                    self.main_menu = MainMenu(self.username)
                    self.hide()


    def get_user_id(self, User_ID=0):
        if User_ID not in self.User_IDs:
            return User_ID
        else:
            return self.get_user_id(User_ID+1)

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
        self.ui.ShowHideButton.clicked.connect(self.show_hide)
        self.show_or_hide = 'Show'

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
        from .main_section import MainMenu
        self.username = self.ui.UsernameInput.text()
        self.password  = self.ui.PasswordInput.text()
        self.selection = database_select(['User_ID', 'Username'], ['Users'])
        self.id1 = [row[0] for row in self.selection if row[1] == self.username]
        self.selection = database_select(['User_ID', 'Password'], ['Users'])
        self.id2 = [row[0] for row in self.selection if check_password(self.password, row[1])]
        if len(self.id1) == 0 or self.id1 != self.id2:
            self.ui.ErrorLabel.setText("Username or password is not valid")
        else:
            self.main_menu = MainMenu(self.username)
            self.hide()

    def show_hide(self):
        if self.show_or_hide == 'Show':
            self.ui.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.show_or_hide = 'Hide'
        else:
            self.ui.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
            self.show_or_hide = 'Show'
        self.ui.ShowHideButton.setText(self.show_or_hide)
