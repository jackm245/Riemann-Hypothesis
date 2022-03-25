"""
introduction_section.py
=======================

Contains all of the classes used to interact with the GUI for the
introduction section of the project

Includes the ...
"""

from PyQt5 import QtWidgets
from .user_interface import Ui_IntroductionScreen, Ui_HistoricalBackgroundScreen, Ui_WhatIsTheRiemannHypothesisScreen, Ui_PracticalApplicationsScreen
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
        self.ui.NextButton.clicked.connect(self.goto_historical_background)
        self.ui.HistoricalBackgroundTab.clicked.connect(self.goto_historical_background)
        self.ui.WhatIsTheRHTab.clicked.connect(self.goto_what_is_the_riemann_hypothesis)
        self.ui.PracticalApplicationsTab.clicked.connect(self.goto_practical_applications)
        self.show()


class HistoricalBackground(IntroductionSection):

    """
    Historical Background
    """

    def __init__(self):
        super(HistoricalBackground, self).__init__()
        self.ui = Ui_HistoricalBackgroundScreen()
        self.ui.setupUi(self)
        self.ui.PrevButton.clicked.connect(self.goto_introduction)
        self.ui.NextButton.clicked.connect(self.goto_what_is_the_riemann_hypothesis)
        self.ui.IntroductionTab.clicked.connect(self.goto_introduction)
        self.ui.WhatIsTheRHTab.clicked.connect(self.goto_what_is_the_riemann_hypothesis)
        self.ui.PracticalApplicationsTab.clicked.connect(self.goto_practical_applications)
        self.show()


class WhatIsTheRiemannHypothesis(IntroductionSection):

    """
    What is the RH
    """

    def __init__(self):
        super(WhatIsTheRiemannHypothesis, self).__init__()
        self.ui = Ui_WhatIsTheRiemannHypothesisScreen()
        self.ui.setupUi(self)
        self.ui.PrevButton.clicked.connect(self.goto_historical_background)
        self.ui.NextButton.clicked.connect(self.goto_practical_applications)
        self.ui.PracticalApplicationsTab.clicked.connect(self.goto_practical_applications)
        self.ui.IntroductionTab.clicked.connect(self.goto_introduction)
        self.ui.HistoricalBackgroundTab.clicked.connect(self.goto_historical_background)
        self.show()


class PracticalApplications(IntroductionSection):

    """
    Practical Applications
    """

    def __init__(self):
        super(PracticalApplications, self).__init__()
        self.ui = Ui_PracticalApplicationsScreen()
        self.ui.setupUi(self)
        self.ui.PrevButton.clicked.connect(self.goto_what_is_the_riemann_hypothesis)
        self.ui.NextButton.clicked.connect(self.goto_mainmenu)
        self.ui.IntroductionTab.clicked.connect(self.goto_introduction)
        self.ui.HistoricalBackgroundTab.clicked.connect(self.goto_historical_background)
        self.ui.WhatIsTheRHTab.clicked.connect(self.goto_what_is_the_riemann_hypothesis)
        self.show()
