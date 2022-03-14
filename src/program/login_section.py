import sys
import re
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from .user_interface import Ui_LoginScreen, Ui_SignUpScreen, Ui_ForgottenPasswordScreen, Ui_ForgottenPassword2Screen, Ui_ResetPasswordScreen, Ui_ResetPassword2Screen
from .utils import database_insert, database_select, database_query, database_print, hash_password, check_password, send_verification_email, User
from time import sleep


class ResetPassword2(QtWidgets.QDialog):

    def __init__(self):
        super(ResetPassword2, self).__init__()
        self.ui = Ui_ResetPassword2Screen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)

        self.ui.SubmitButton.clicked.connect(self.submit)
        self.show()

    def submit(self):
        self.password1 = self.ui.PasswordInput.text()
        self.password2 = self.ui.ConfirmPasswordInput.text()
        self.pwds_invalid = are_invalid_passwords(self.password1, self.password2)
        if self.pwds_invalid:
            self.ui.ErrorLabel.setText(self.pwds_invalid)
        else:
            database_query("UPDATE Users SET Password=? WHERE User_ID=?",(hash_password(self.password1), User.GetUserID(),))
            from .main_section import MainMenu
            self.main_menu = MainMenu()
            self.hide()


class ResetPassword(QtWidgets.QDialog):

    def __init__(self):
        super(ResetPassword, self).__init__()
        self.ui = Ui_ResetPasswordScreen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)

        self.show_or_hide = 'Show'
        self.ui.LoginTab.clicked.connect(self.goto_login)
        self.ui.SignUpTab.clicked.connect(self.goto_signup)
        self.ui.ForgottenPasswordTab.clicked.connect(self.goto_forgotten_password)
        self.ui.ShowHideButton.clicked.connect(self.show_hide)

        self.ui.SubmitButton.clicked.connect(self.submit)

        self.show()

    def show_hide(self):
        if self.show_or_hide == 'Show':
            self.ui.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.show_or_hide = 'Hide'
        else:
            self.ui.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
            self.show_or_hide = 'Show'
        self.ui.ShowHideButton.setText(self.show_or_hide)

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
        self.username = self.ui.UsernameInput.text()
        self.password  = self.ui.PasswordInput.text()
        self.selection = database_select(['User_ID', 'Username'], ['Users'])
        self.id1 = [row[0] for row in self.selection if row[1] == self.username]
        self.selection = database_select(['User_ID', 'Password'], ['Users'])
        self.id2 = [row[0] for row in self.selection if check_password(self.password, row[1])]
        if len(self.id1) == 0 or self.id1 != self.id2:
            self.ui.ErrorLabel.setText("Username or password is not valid")
        else:
            User.SetSignedIn(True)
            User.SetUsername(self.username)
            User.SetUserID(self.id1[0])
            self.email = database_query("SELECT Email FROM Users WHERE User_ID=?", (self.id1[0],))[0][0]
            User.SetEmail(self.email)
            self.reset_password_2 = ResetPassword2()
            self.hide()


class ForgottenPassword2(QtWidgets.QDialog):

    def __init__(self, verification_code):
        super(ForgottenPassword2, self).__init__()
        self.verification_code = verification_code
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
        self.user_input = self.ui.VerificationCodeInput.text()
        if self.user_input == self.verification_code:
            User.SetSignedIn(True)
            self.reset_password_2 = ResetPassword2()
            self.hide()
        else:
            self.ui.ErrorLabel.setText("Verification Code Incorrect")


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
        self.email  = self.ui.EmailInput.text()
        self.selection = database_query("SELECT Email FROM Users WHERE Email=?", (self.email,))
        if len(self.selection) == 0:
            self.ui.ErrorLabel.setText("Email is not registered")
        else:
            # Send Email
            self.verificaton_code = ''.join(list(map(str, [random.randint(0, 9) for _ in range(6)])))
            self.user_id = database_query("SELECT User_ID FROM Users WHERE Email=?", (self.email,))[0][0]
            self.username = database_query("SELECT Username FROM Users WHERE Email=?", (self.email,))[0][0]
            User.SetUserID(self.user_id)
            User.SetUsername(self.username)
            User.SetEmail(self.email)
            send_verification_email(self.verificaton_code)
            self.forgotten_password_2 = ForgottenPassword2(self.verificaton_code)
            self.hide()


class SignUp(QtWidgets.QDialog):

    def __init__(self):
        super(SignUp, self).__init__()
        self.ui = Ui_SignUpScreen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)
        self.show_or_hide = 'Show'
        self.show_or_hide_2 = 'Show'

        self.ui.LoginTab.clicked.connect(self.goto_login)
        self.ui.ForgottenPasswordTab.clicked.connect(self.goto_forgotten_password)
        self.ui.ResetPasswordTab.clicked.connect(self.goto_reset_password)
        self.ui.ShowHideButton.clicked.connect(self.show_hide)
        self.ui.ShowHideButton_2.clicked.connect(self.show_hide_2)
        self.ui.SubmitButton.clicked.connect(self.submit)

        self.show()

    def show_hide(self):
        if self.show_or_hide == 'Show':
            self.ui.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.show_or_hide = 'Hide'
        else:
            self.ui.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
            self.show_or_hide = 'Show'
        self.ui.ShowHideButton.setText(self.show_or_hide)

    def show_hide_2(self):
        if self.show_or_hide_2 == 'Show':
            self.ui.PasswordInput_2.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.show_or_hide_2 = 'Hide'
        else:
            self.ui.PasswordInput_2.setEchoMode(QtWidgets.QLineEdit.Password)
            self.show_or_hide_2 = 'Show'
        self.ui.ShowHideButton_2.setText(self.show_or_hide_2)

    def submit(self):
        from .main_section import MainMenu
        self.username = self.ui.UsernameInput.text()
        self.email = self.ui.EmailInput.text()
        self.password  = self.ui.PasswordInput.text()
        self.confirm_password  = self.ui.PasswordInput_2.text()
        self.pwds_invalid = are_invalid_passwords(self.password, self.confirm_password)
        # check is of right form
        if not re.fullmatch('\w{1,20}', self.username):
            self.ui.ErrorLabel.setText("Username must be at 1-20 characters long\nand not contain special characters")
        elif not re.fullmatch('.+@.+\..+', self.email):
            self.ui.ErrorLabel.setText("Email address must be valid")
        elif self.pwds_invalid:
            self.ui.ErrorLabel.setText(self.pwds_invalid)
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
                    self.hashed_password = hash_password(self.password)
                    database_insert('Users', [self.User_ID, self.username, self.email, self.hashed_password])
                    User.SetSignedIn(True)
                    User.SetUserID(self.User_ID)
                    User.SetUsername(self.username)
                    User.SetEmail(self.email)
                    self.main_menu = MainMenu()
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

        self.ui.BackButton.clicked.connect(self.goto_mainmenu)
        self.ui.SubmitButton.clicked.connect(self.submit)
        self.ui.ShowHideButton.clicked.connect(self.show_hide)
        self.show_or_hide = 'Show'

        self.show()

    def goto_mainmenu(self):
        from .main_section import MainMenu
        self.main_menu = MainMenu()
        self.hide()

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
            User.SetSignedIn(True)
            User.SetUsername(self.username)
            User.SetUserID(self.id1[0])
            self.email = database_query("SELECT Email FROM Users WHERE User_ID=?", (self.id1[0],))[0][0]
            User.SetEmail(self.email)
            self.main_menu = MainMenu()
            self.hide()

    def show_hide(self):
        if self.show_or_hide == 'Show':
            self.ui.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.show_or_hide = 'Hide'
        else:
            self.ui.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
            self.show_or_hide = 'Show'
        self.ui.ShowHideButton.setText(self.show_or_hide)


def are_invalid_passwords(password1, password2):
    if not re.fullmatch('(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9]).{8,}', password1):
        return "Password must contain lower case, upper case,\na number, and be at least 8 characters long"
    elif password1 != password2:
        return "Passwords do not match"
    else:
        return False
