from PyQt5 import QtWidgets
from .user_interface import Ui_MainMenu
from .login_section import Login
from .investigation_section import GraphPlot
import sys

class MainMenu(QtWidgets.QMainWindow):


    def __init__(self, username=''):
        super(MainMenu, self).__init__()
        self.username = username
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)

        if self.username:
            self.ui.LoginLabel.setText(f"<html><head/><body><p align=\"center\">{self.username}</p></body></html>")
            self.ui.LoginLabel.show()
        else:
            self.ui.LoginLabel.hide()

        self.ui.LogInButton.clicked.connect(self.goto_login)
        self.ui.InvestigationButton.clicked.connect(self.goto_investigation)
        self.ui.ExitButton.clicked.connect(self.exit)

        self.show()


    def goto_login(self):
        self.login = Login()
        self.hide()


    def goto_investigation(self):
        self.login = GraphPlot()
        self.hide()


    def exit(self):
        sys.exit()
