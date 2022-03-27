"""
tutorial_section.py
===================

Contains all of the classes used to interact with the GUI for the
tutorial section of the project

Includes the Program Structure, Login, Introduction, Investigation
and Summary Tutorial Screens
"""

from PyQt5 import QtWidgets, QtCore
from .user_interface import Ui_TutorialScreen, Ui_ProgramStructureTutorialScreen, Ui_IntroductionTutorialScreen, Ui_InvestigationTutorialScreen, Ui_LoginTutorialScreen, Ui_SummaryTutorialScreen, Ui_GraphMatPlotScreen
from .utils import User, Screen, StaticGraphScreen, database_query
from .notes import TutorialNotes


class TutorialSection(Screen):

    """
    A class inherited by all of the Screens/Page classes in the tutorial section
    of the program

    The functions defined in this class allow for different pages to be loaded
    and hidden, so that the user is able to navigate to different parts of the
    program using the GUI
    """

    def __init__(self):
        super(TutorialSection, self).__init__()

    def goto_tutorial(self):
        self.tutorial= Tutorial()
        self.hide()

    def goto_program_structure(self):
        self.program_structure = ProgramStructure()
        self.hide()

    def goto_login(self):
        self.login = LoginTutorial()
        self.hide()

    def goto_introduction(self):
        self.introduction = IntroductionTutorial()
        self.hide()

    def goto_investigation(self):
        self.investigation = InvestigationTutorial()
        self.hide()

    def goto_summary(self):
        self.summary = SummaryTutorial()
        self.hide()

    def goto_tutorial_notes(self):
        self.tutorial_notes = TutorialNotes()


class Tutorial(TutorialSection):

    """
    The Tutorial Screen is the main entry point ot the tutorial section of the
    program

    This class displays said screen to the user
    """

    def __init__(self):
        super(Tutorial, self).__init__()
        self.ui = Ui_TutorialScreen()
        self.ui.setupUi(self)
        self.ui.ProgramStructureTab.clicked.connect(self.goto_program_structure)
        self.ui.LoginTab.clicked.connect(self.goto_login)
        self.ui.IntroductionTab.clicked.connect(self.goto_introduction)
        self.ui.InvestigationTab.clicked.connect(self.goto_investigation)
        self.ui.SummaryTab.clicked.connect(self.goto_summary)
        self.ui.PrevButton.clicked.connect(self.goto_mainmenu)
        self.ui.NextButton.clicked.connect(self.goto_program_structure)
        self.show()


class ProgramStructure(TutorialSection):

    """
    This class displays the second screen in the tutorial section: the program
    structure tutorial
    """

    def __init__(self):
        super(ProgramStructure, self).__init__()
        self.ui = Ui_ProgramStructureTutorialScreen()
        self.ui.setupUi(self)
        self.ui.TutorialTab.clicked.connect(self.goto_tutorial)
        self.ui.LoginTab.clicked.connect(self.goto_login)
        self.ui.IntroductionTab.clicked.connect(self.goto_introduction)
        self.ui.InvestigationTab.clicked.connect(self.goto_investigation)
        self.ui.SummaryTab.clicked.connect(self.goto_summary)
        self.ui.PrevButton.clicked.connect(self.goto_tutorial)
        self.ui.NextButton.clicked.connect(self.goto_login)
        self.show()


class LoginTutorial(TutorialSection):

    """
    This class displays the third screen in the tutorial section: the
    login tutorial
    """

    def __init__(self):
        super(LoginTutorial, self).__init__()
        self.ui = Ui_LoginTutorialScreen()
        self.ui.setupUi(self)
        self.ui.TutorialTab.clicked.connect(self.goto_tutorial)
        self.ui.ProgramStructureTab.clicked.connect(self.goto_program_structure)
        self.ui.IntroductionTab.clicked.connect(self.goto_introduction)
        self.ui.InvestigationTab.clicked.connect(self.goto_investigation)
        self.ui.SummaryTab.clicked.connect(self.goto_summary)
        self.ui.PrevButton.clicked.connect(self.goto_program_structure)
        self.ui.NextButton.clicked.connect(self.goto_introduction)
        self.show()


class IntroductionTutorial(TutorialSection):

    """
    This class displays the fourth screen in the tutorial section: the
    introduction tutorial
    """

    def __init__(self):
        super(IntroductionTutorial, self).__init__()
        self.ui = Ui_IntroductionTutorialScreen()
        self.ui.setupUi(self)
        self.ui.TutorialTab.clicked.connect(self.goto_tutorial)
        self.ui.ProgramStructureTab.clicked.connect(self.goto_program_structure)
        self.ui.LoginTab.clicked.connect(self.goto_login)
        self.ui.InvestigationTab.clicked.connect(self.goto_investigation)
        self.ui.SummaryTab.clicked.connect(self.goto_summary)
        self.ui.PrevButton.clicked.connect(self.goto_login)
        self.ui.NextButton.clicked.connect(self.goto_investigation)
        self.show()


class InvestigationTutorial(TutorialSection):

    """
    This class displays the fifth screen in the tutorial section: the
    investigation tutorial
    """

    def __init__(self):
        super(InvestigationTutorial, self).__init__()
        self.gradient = 0
        self.y_intercept = 0
        self.question_no = 0
        self.ui = Ui_InvestigationTutorialScreen()
        self.ui.setupUi(self)
        self.ui.QuestionText.setStyleSheet("font-size: 16pt; font-weight: 600;")
        self.text = database_query("SELECT Question FROM Questions WHERE Question_No=?", [self.question_no])[0][0]
        self.ui.QuestionText.setText(self.center_text(self.text))
        self.ui.TutorialTab.clicked.connect(self.goto_tutorial)
        self.ui.ProgramStructureTab.clicked.connect(self.goto_program_structure)
        self.ui.LoginTab.clicked.connect(self.goto_login)
        self.ui.IntroductionTab.clicked.connect(self.goto_introduction)
        self.ui.SummaryTab.clicked.connect(self.goto_summary)
        self.ui.PrevButton.clicked.connect(self.goto_introduction)
        self.ui.NextButton.clicked.connect(self.goto_summary)
        self.ui.MSlider.valueChanged.connect(self.M_value_changed)
        self.ui.CSlider.valueChanged.connect(self.C_value_changed)
        self.ui.GraphButton.clicked.connect(self.graph)
        self.ui.SubmitButton.clicked.connect(self.submit)
        self.show()

    def M_value_changed(self):
        self.gradient = self.ui.MSlider.value()
        self.ui.MDisplay.setText(self.center_text(str(self.gradient)))

    def C_value_changed(self):
        self.y_intercept = self.ui.CSlider.value()
        self.ui.CDisplay.setText(self.center_text(str(self.y_intercept)))

    def graph(self):
        self.plot = GraphMatPlot(self.gradient, self.y_intercept)

    def submit(self):
        self.answer = self.ui.QuestionInput.text()
        if self.answer == '2':
            self.ui.MessageLabel.setStyleSheet("color: rgb(0, 140, 0);\n"
                    "font: 18pt \"Sans Serif\";")
            self.ui.MessageLabel.setText(self.center_text('Correct!'))
        else:
            self.ui.MessageLabel.setStyleSheet("color: rgb(255, 0, 0);\n"
                    "font: 18pt \"Sans Serif\";")
            self.ui.MessageLabel.setText(self.center_text('That is incorrect, try again'))


class GraphMatPlot(StaticGraphScreen):

    """
    Graph Mat Plot
    """

    def __init__(self, gradient, y_intercept):
        super(GraphMatPlot, self).__init__()
        self.y_intercept = y_intercept
        self.gradient = gradient
        self.ui = Ui_GraphMatPlotScreen()
        self.init_widget()
        self.x_vals = list(range(21))
        self.y_vals= [self.gradient * num + self.y_intercept for num in self.x_vals]
        self.count = 0
        self.show()
        self.graph()

    def get_label(self, value, gradient=False):
        if gradient:
            match value:
                case -1:
                    return '-x'
                case 0:
                    return ''
                case 1:
                    return 'x'
                case _:
                    return f'{value}x'
        elif value == 0:
            if self.gradient == 0:
                return '0'
            else:
                return ''
        elif value > 0 and self.gradient != 0:
            return f'+{value}'
        else:
            return str(value)

    def graph(self):
        self.gradient_label = self.get_label(self.gradient, True)
        self.intercept_label = self.get_label(self.y_intercept, False)
        self.matplotlibwidget.axes.cla()
        self.matplotlibwidget.axes.plot(
                self.x_vals, self.y_vals,
                label=f'y={self.gradient_label}{self.intercept_label}',
                color='blue')
        self.matplotlibwidget.axes.legend(loc='upper left')
        self.matplotlibwidget.canvas.draw()


class SummaryTutorial(TutorialSection):

    """
    This class displays the sixth and last screen in the tutorial section: the
    summary tutorial
    """

    def __init__(self):
        super(SummaryTutorial, self).__init__()
        self.ui = Ui_SummaryTutorialScreen()
        self.ui.setupUi(self)
        self.ui.TutorialTab.clicked.connect(self.goto_tutorial)
        self.ui.ProgramStructureTab.clicked.connect(self.goto_program_structure)
        self.ui.LoginTab.clicked.connect(self.goto_login)
        self.ui.IntroductionTab.clicked.connect(self.goto_introduction)
        self.ui.InvestigationTab.clicked.connect(self.goto_investigation)
        self.ui.PrevButton.clicked.connect(self.goto_investigation)
        self.ui.NextButton.clicked.connect(self.goto_mainmenu)
        self.ui.NotesButton.clicked.connect(self.goto_tutorial_notes)
        self.show()
