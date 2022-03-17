"""
introduction_section.py
=======================

Contains all of the classes used to interact with the GUI for the
introduction section of the project

Includes the ...
"""

from PyQt5 import QtWidgets
from .user_interface import Ui_IntroductionScreen
from .utils import User, Screen


class IntroductionSection(Screen):

    """
    A class inherited by all of the Screens/Page classes in the introduction
    section of the program

    The functions defined in this class allow for different pages to be loaded
    and hidden, so that the user is able to navigate to different parts of the
    program using the GUI
    """

    def __init__(self):
        super(IntroductionSection, self).__init__()

    def goto_introduction(self):
        self.introduction= Introduction()
        self.hide()


class Introduction(IntroductionSection):

    """
    The Introduction Screen is the main entry point ot the introduction section of the
    program

    This class displays said screen to the user
    """

    def __init__(self):
        super(Introduction, self).__init__()
        self.ui = Ui_IntroductionScreen()
        self.ui.setupUi(self)
        self.ui.PrevButton.clicked.connect(self.goto_mainmenu)
        #  self.ui.NextButton.clicked.connect(self.goto_program_structure)
        self.show()
