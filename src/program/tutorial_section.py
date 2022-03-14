from PyQt5 import QtWidgets
from .user_interface import Ui_TutorialScreen
from .utils import User

class Tutorial(QtWidgets.QMainWindow):


    def __init__(self):
        super(Tutorial, self).__init__()
        self.ui = Ui_TutorialScreen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)

        self.ui.ProgramStructureTab.clicked.connect(self.goto_program_structure)
        self.ui.LoginTab.clicked.connect(self.goto_login)
        self.ui.IntroductionTab.clicked.connect(self.goto_introduction)
        self.ui.InvestigationTab.clicked.connect(self.goto_investigation)
        self.ui.SummaryTab.clicked.connect(self.goto_summary)
        self.ui.PrevButton.clicked.connect(self.goto_mainmenu)
        self.ui.NextButton.clicked.connect(self.goto_program_structure)
        #  self.ui.InvestigationButton.clicked.connect(self.goto_investigation)
        #  self.ui.ExitButton.clicked.connect(self.exit)

        self.show()

    def goto_mainmenu(self):
        from .main_section import MainMenu
        self.main_menu = MainMenu()
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
