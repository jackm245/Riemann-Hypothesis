"""
summary_section.py
=======================

Contains all of the classes used to interact with the GUI for the
summary section of the project

Includes the ...
"""

from PyQt5 import QtWidgets
from .user_interface import Ui_SummaryScreen, Ui_TheoryRecapScreen, Ui_InvestigationResultsScreen, Ui_ConclusionScreen, Ui_ImpactScreen
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

    def setup_tabs(self):
        self.ui.SummaryTab.clicked.connect(self.goto_summary)
        self.ui.TheoryRecapTab.clicked.connect(self.goto_theory_recap)
        self.ui.InvestigationResultsTab.clicked.connect(self.goto_investigation_results)
        self.ui.ConclusionTab.clicked.connect(self.goto_conclusion)
        self.ui.ImpactTab.clicked.connect(self.goto_impact)

    def goto_summary(self):
        self.summary = Summary()
        self.hide()

    def goto_theory_recap(self):
        self.theory_recap = TheoryRecap()
        self.hide()

    def goto_investigation_results(self):
        self.investigation_results = InvestigationResults()
        self.hide()

    def goto_conclusion(self):
        self.conclusion = Conclusion()
        self.hide()

    def goto_impact(self):
        self.impact = Impact()
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
        self.ui.NextButton.clicked.connect(self.goto_theory_recap)
        self.setup_tabs()
        self.show()


class TheoryRecap(SummarySection):

    """
    Theory Recap
    """

    def __init__(self):
        super(TheoryRecap, self).__init__()
        self.ui = Ui_TheoryRecapScreen()
        self.ui.setupUi(self)
        self.ui.PrevButton.clicked.connect(self.goto_summary)
        self.ui.NextButton.clicked.connect(self.goto_investigation_results)
        self.setup_tabs()
        self.show()


class InvestigationResults(SummarySection):

    """
    Invsetigation Results
    """

    def __init__(self):
        super(InvestigationResults, self).__init__()
        self.ui = Ui_InvestigationResultsScreen()
        self.ui.setupUi(self)
        self.ui.PrevButton.clicked.connect(self.goto_theory_recap)
        self.ui.NextButton.clicked.connect(self.goto_conclusion)
        self.setup_tabs()
        self.show()


class Conclusion(SummarySection):

    """
    Conclusion
    """

    def __init__(self):
        super(Conclusion, self).__init__()
        self.ui = Ui_ConclusionScreen()
        self.ui.setupUi(self)
        self.ui.PrevButton.clicked.connect(self.goto_investigation_results)
        self.ui.NextButton.clicked.connect(self.goto_impact)
        self.setup_tabs()
        self.show()


class Impact(SummarySection):

    """
    Impact
    """

    def __init__(self):
        super(Impact, self).__init__()
        self.ui = Ui_ImpactScreen()
        self.ui.setupUi(self)
        self.ui.PrevButton.clicked.connect(self.goto_conclusion)
        self.ui.NextButton.clicked.connect(self.goto_mainmenu)
        self.setup_tabs()
        self.show()
