"""
summary_section.py
=======================

Contains all of the classes used to interact with the GUI for the
summary section of the project

Includes the ...
"""

from PyQt5 import QtWidgets
from .user_interface import Ui_SummaryScreen
from .utils import User, Screen


class SummarySection(Screen):

    """
    A class inherited by all of the Screens/Page classes in the summary
    section of the program

    The functions defined in this class allow for different pages to be loaded
    and hidden, so that the user is able to navigate to different parts of the
    program using the GUI
    """

    def __init__(self):
        super(SummarySection, self).__init__()

    def goto_summary(self):
        self.summary= Summary()
        self.hide()


class Summary(SummarySection):

    """
    The Summary Screen is the main entry point ot the summary section of the
    program

    This class displays said screen to the user
    """

    def __init__(self):
        super(Summary, self).__init__()
        self.ui = Ui_SummaryScreen()
        self.ui.setupUi(self)
        self.ui.PrevButton.clicked.connect(self.goto_mainmenu)
        #  self.ui.NextButton.clicked.connect(self.goto_)
        self.show()
