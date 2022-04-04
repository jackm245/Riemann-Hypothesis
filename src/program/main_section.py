"""
main_section.py
===============

Contains the class used to interact with the GUI for the
main menu in the project

Includes the Main Menu screen only
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem, QHeaderView
from .user_interface import Ui_MainMenu, Ui_ProgressScreen
from .login_section import Login
from .introduction_section import Introduction
from .investigation_section import GraphPlot
from .tutorial_section import Tutorial
from .summary_section import Summary
from .notes import TutorialNotes
from .utils import User, Screen, database_select, database_query
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
        if User.GetSignedIn():
            self.ui.UsernameButton.setText(User.GetUsername())
            self.ui.UsernameButton.show()
        else:
            self.ui.UsernameButton.hide()
        self.ui.LogInButton.clicked.connect(self.goto_login)
        self.ui.TutorialButton.clicked.connect(self.goto_tutorial)
        self.ui.IntroductionButton.clicked.connect(self.goto_introduction)
        self.ui.InvestigationButton.clicked.connect(self.goto_investigation)
        self.ui.SummaryButton.clicked.connect(self.goto_summary)
        self.ui.ExitButton.clicked.connect(self.exit)
        self.ui.UsernameButton.clicked.connect(self.goto_progress)
        self.show()

    def goto_login(self):
        self.login = Login()
        self.hide()

    def goto_tutorial(self):
        self.tutorial = Tutorial()
        self.hide()

    def goto_introduction(self):
        self.introduction = Introduction()
        self.hide()

    def goto_investigation(self):
        self.investigation = GraphPlot()
        self.hide()

    def goto_summary(self):
        self.summary = Summary()
        self.hide()

    def goto_progress(self):
        self.progress = Progress()
        self.hide()

    def exit(self):
        sys.exit()


class Progress(Screen):

    """
    Progress
    """

    def __init__(self):
        super(Progress, self).__init__()
        self.ui = Ui_ProgressScreen()
        self.ui.setupUi(self)
        if User.GetSignedIn():
            self.ui.SubTitleText.setText(f'User: {User.GetUsername()}')
            self.setup_table()
        else:
            pass
        self.ui.BackButton.clicked.connect(self.goto_mainmenu)
        self.ui.NotesButton.clicked.connect(self.goto_notes)
        self.show()

    def goto_notes(self):
        self.notes = TutorialNotes()

    def setup_table(self):
        self.questions = database_select(['*'], ['Questions'])
        self.correct_answers = database_select(['*'], ['CorrectAnswers'])
        self.users_answers = database_query("SELECT Question_No, UsersAnswer FROM UsersAnswers WHERE Username=?", User.GetUsername())
        self.table_values = []
        for question_no, question in self.questions:
            if question_no == 0:
                continue
            answer = ''.join([str(items[1]) for items in self.users_answers if items[0] == question_no])
            correct_answers = [str(items[1]).lower() for items in self.correct_answers if items[0] == question_no]
            correct = answer in correct_answers
            self.table_values.append((question, answer, correct))
        self.ui.Table.setRowCount(len(self.table_values))
        for i, values in enumerate(self.table_values):
            for j, value in enumerate(values):
                self.ui.Table.setItem(i,j, QTableWidgetItem(str(value)))
        #  self.ui.Table.horizontalHeader().setStretchLastSection(True)
        #  self.ui.Table.horizontalHeader().setSectionResizeMode(
            #  QHeaderView.Stretch)
        header = self.ui.Table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        #  self.ui.Table.setColumnWidth(1, 100)

