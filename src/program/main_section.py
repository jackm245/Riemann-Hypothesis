"""
main_section.py
===============

Contains the class used to interact with the GUI for the
main menu in the project

Includes the Main Menu screen only
"""

from PyQt5 import QtWidgets
from .user_interface import Ui_MainMenu
from .login_section import Login
from .investigation_section import GraphPlot
from .tutorial_section import Tutorial
from .utils import User, Screen
import sys

class MainMenu(Screen):

    """
    This class configures the GUI for the main menu, and allows the user
    to interact wih the GUI for this page
    """

    def __init__(self):
        super(MainMenu, self).__init__()
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        if User.username:
            self.ui.LoginLabel.setText(f"<html><head/><body><p align=\"center\">{User.username}</p></body></html>")
            self.ui.LoginLabel.show()
        else:
            self.ui.LoginLabel.hide()
        self.ui.LogInButton.clicked.connect(self.goto_login)
        self.ui.TutorialButton.clicked.connect(self.goto_tutorial)
        self.ui.InvestigationButton.clicked.connect(self.goto_investigation)
        self.ui.ExitButton.clicked.connect(self.exit)
        self.show()

    def goto_login(self):
        self.login = Login()
        self.hide()

    def goto_tutorial(self):
        self.tutorial = Tutorial()
        self.hide()

    def goto_investigation(self):
        self.login = GraphPlot()
        self.hide()

    def exit(self):
        sys.exit()
