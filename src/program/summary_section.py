"""
summary_section.py
==================

Contains all of the classes used to interact with the GUI for the
summary section of the project

Includes the main SummarySection class which is inherited by the Summary,
TheoryRecap, InvestigationResults, Conclusion, Impact
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem, QHeaderView
from .user_interface import Ui_SummaryScreen, Ui_TheoryRecapScreen, Ui_InvestigationResultsScreen, Ui_ConclusionScreen, Ui_ImpactScreen
from .utils import User, Screen, database_select, Complex
from .notes import SummaryNotes


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

        """
        Allows the tabs and buttons to run a function once clicked, if they
        exists on the web page that the tab/button was clicked on
        """

        self.ui.SummaryTab.clicked.connect(self.goto_summary)
        self.ui.TheoryRecapTab.clicked.connect(self.goto_theory_recap)
        self.ui.InvestigationResultsTab.clicked.connect(self.goto_investigation_results)
        self.ui.ConclusionTab.clicked.connect(self.goto_conclusion)
        self.ui.ImpactTab.clicked.connect(self.goto_impact)
        try:
            self.ui.NotesButton.clicked.connect(self.goto_summary_notes)
        except AttributeError:
            pass

    """
    The goto functions are run when a tab is clicked. They load a new page,
    and hide the old page.
    """

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

    def goto_summary_notes(self):
        self.summary_notes = SummaryNotes()


class Summary(SummarySection):

    """
    The Summary Screen is the main entry point ot the summary section of the
    program. This class displays the summary screen to the user.
    """

    def __init__(self):
        super(Summary, self).__init__()
        self.question_no = 8
        self.ui = Ui_SummaryScreen()
        self.ui.setupUi(self)
        self.setup_tabs()
        self.setup_question()
        self.ui.PrevButton.clicked.connect(self.goto_mainmenu)
        self.ui.NextButton.clicked.connect(self.goto_theory_recap)
        self.show()


class TheoryRecap(SummarySection):

    """
    Theory Recap Screen class displays this screen to the user as part
    of the sumary section of this program
    """

    def __init__(self):
        super(TheoryRecap, self).__init__()
        self.question_no = 9
        self.ui = Ui_TheoryRecapScreen()
        self.ui.setupUi(self)
        self.setup_tabs()
        self.setup_question()
        self.ui.PrevButton.clicked.connect(self.goto_summary)
        self.ui.NextButton.clicked.connect(self.goto_investigation_results)
        self.show()


class InvestigationResults(SummarySection):

    """
    The Investigation Results Screen class displays this screen to the user as part
    of the sumary section of this program
    """

    def __init__(self):
        super(InvestigationResults, self).__init__()
        self.ui = Ui_InvestigationResultsScreen()
        self.ui.setupUi(self)
        self.ui.PrevButton.clicked.connect(self.goto_theory_recap)
        self.ui.NextButton.clicked.connect(self.goto_conclusion)
        self.setup_tabs()
        self.setup_table()
        self.show()

    def setup_table(self):
        """
        Populates the table on this screen with a list of inputs and
        outputs of the zeta function
        """
        self.values = database_select(['*'], ['Zeta'])
        self.table_values = [(Complex(value[1], value[2]), Complex(value[3], value[4])) for value in self.values]
        self.ui.ZetaTable.setRowCount(len(self.table_values))
        for i, values in enumerate(self.table_values):
            for j in range(len(values)):
                self.ui.ZetaTable.setItem(i,j, QTableWidgetItem(str(values[j])))
        self.ui.ZetaTable.horizontalHeader().setStretchLastSection(True)
        self.ui.ZetaTable.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        self.ui.ZetaTable.setColumnWidth(1, 100)


class Conclusion(SummarySection):

    """
    The Conclusion Screen class displays this screen to the user as part
    of the sumary section of this program
    """

    def __init__(self):
        super(Conclusion, self).__init__()
        self.ui = Ui_ConclusionScreen()
        self.ui.setupUi(self)
        self.setup_tabs()
        self.ui.PrevButton.clicked.connect(self.goto_investigation_results)
        self.ui.NextButton.clicked.connect(self.goto_impact)
        self.show()


class Impact(SummarySection):

    """
    The Impact Screen class displays this screen to the user as part
    of the sumary section of this program
    """

    def __init__(self):
        super(Impact, self).__init__()
        self.question_no = 10
        self.ui = Ui_ImpactScreen()
        self.ui.setupUi(self)
        self.setup_tabs()
        self.setup_question()
        self.ui.PrevButton.clicked.connect(self.goto_conclusion)
        self.ui.NextButton.clicked.connect(self.goto_mainmenu)
        self.show()
