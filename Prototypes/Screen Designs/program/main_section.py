from PyQt5 import QtWidgets
from .user_interface import Ui_MainMenu
from .login_section import Login
import sys

class MainMenu(QtWidgets.QMainWindow):


    def __init__(self):
        super(MainMenu, self).__init__()
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
