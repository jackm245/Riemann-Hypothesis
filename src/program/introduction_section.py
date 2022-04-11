"""
introduction_section.py
=======================

Contains all of the classes used to interact with the GUI for the
introduction section of the project

Includes the classes:
    - IntroductionSection
    - Introduction
    - HistoricalBackground
    - WhatIsTheRiemannHypothesis
    - PracticalApplications

Objectives completed in this file:
    1(a)
    3 3.(a) 3.(b) 3.(c) 3.(d)
"""

from PyQt5 import QtWidgets
from .user_interface import Ui_IntroductionScreen, Ui_HistoricalBackgroundScreen, Ui_WhatIsTheRiemannHypothesisScreen, Ui_PracticalApplicationsScreen
from .utils import User, Screen
from .notes import IntroductionNotes


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

    def setup_tabs(self):
        """ Allows the screen to change when the tabs are clicked """
        try:
            self.ui.IntroductionTab.clicked.connect(self.goto_introduction)
        except AttributeError:
            pass
        try:
            self.ui.HistoricalBackgroundTab.clicked.connect(self.goto_historical_background)
        except AttributeError:
            pass
        try:
            self.ui.WhatIsTheRHTab.clicked.connect(self.goto_what_is_the_riemann_hypothesis)
        except AttributeError:
            pass
        try:
            self.ui.PracticalApplicationsTab.clicked.connect(self.goto_practical_applications)
        except AttributeError:
            pass
        try:
            self.ui.NotesButton.clicked.connect(self.goto_introduction_notes)
        except AttributeError:
            pass

    """ goto functions load a new screen and hide the old one"""

    def goto_introduction(self):
        self.introduction = Introduction()
        self.hide()

    def goto_historical_background(self):
        self.historical_background = HistoricalBackground()
        self.hide()

    def goto_what_is_the_riemann_hypothesis(self):
        self.what_is_the_rh = WhatIsTheRiemannHypothesis()
        self.hide()

    def goto_practical_applications(self):
        self.practical_applications = PracticalApplications()
        self.hide()

    def goto_introduction_notes(self):
        self.introduction_notes = IntroductionNotes()


class Introduction(IntroductionSection):

    """
    The Introduction Screen is the main entry point ot the introduction section of the
    program
    """

    def __init__(self):
        super(Introduction, self).__init__()
        self.ui = Ui_IntroductionScreen()
        self.ui.setupUi(self)
        self.setup_tabs()
        self.ui.PrevButton.clicked.connect(self.goto_mainmenu)
        self.ui.NextButton.clicked.connect(self.goto_historical_background)
        self.show()


class HistoricalBackground(IntroductionSection):

    """
    A class used to interact with the Historical Background GUI screen
    Completes objective 3(a)
    """

    def __init__(self):
        super(HistoricalBackground, self).__init__()
        self.ui = Ui_HistoricalBackgroundScreen()
        self.ui.setupUi(self)
        self.setup_tabs()
        self.ui.PrevButton.clicked.connect(self.goto_introduction)
        self.ui.NextButton.clicked.connect(self.goto_what_is_the_riemann_hypothesis)
        self.show()


class WhatIsTheRiemannHypothesis(IntroductionSection):

    """
    A class used to interact with the What Is The Riemann Hypothesis GUI screen
    Completes objective 3(b)
    """

    def __init__(self):
        super(WhatIsTheRiemannHypothesis, self).__init__()
        self.question_no = 3
        self.ui = Ui_WhatIsTheRiemannHypothesisScreen()
        self.ui.setupUi(self)
        self.setup_tabs()
        self.setup_question()
        self.ui.PrevButton.clicked.connect(self.goto_historical_background)
        self.ui.NextButton.clicked.connect(self.goto_practical_applications)
        self.show()


class PracticalApplications(IntroductionSection):

    """
    A class used to interact with the Practical Applications GUI screen
    Completes objective 3(c)
    """

    def __init__(self):
        super(PracticalApplications, self).__init__()
        self.question_no = 4
        self.ui = Ui_PracticalApplicationsScreen()
        self.ui.setupUi(self)
        self.setup_tabs()
        self.setup_question()
        self.ui.PrevButton.clicked.connect(self.goto_what_is_the_riemann_hypothesis)
        self.ui.NextButton.clicked.connect(self.goto_mainmenu)
        self.show()
