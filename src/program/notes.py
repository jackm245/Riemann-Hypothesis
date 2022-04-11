"""
notes.py
========

Contains all of the classes used to interact with the GUI for the
user to be able to take notes in the program

Includes notes screens for the tutorial, introduction, investigation and summary
screens

Objectives completed in this file:
    1 1(b)
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from .utils import Screen, database_query, database_insert, User, get_id
from .user_interface import Ui_TutorialNotesScreen, Ui_IntroductionNotesScreen, Ui_InvestigationNotesScreen, Ui_SummaryNotesScreen


class Notes(Screen):

    """
    A class inherited by all of the Screens/Page classes in the notes section
    of the program

    The functions defined in this class allow for different pages to be loaded
    and hidden, so that the user is able to navigate to different parts of the
    program using the GUI
    """

    def __init__(self):
        super(Notes, self).__init__()

    def goto_tutorial_notes(self):
        self.tutorial_notes = TutorialNotes()
        self.hide()

    def goto_introduction_notes(self):
        self.introduction_notes = IntroductionNotes()
        self.hide()

    def goto_investigation_notes(self):
        self.investigation_notes = InvestigationNotes()
        self.hide()

    def goto_summary_notes(self):
        self.summary_notes = SummaryNotes()
        self.hide()

    def exit_notes(self):
        self.hide()

    def saveto_database(self):
        self.text = self.ui.NotesText.toPlainText()
        database_query("DELETE FROM Notes WHERE Section=? AND Username=?", self.section, User.GetUsername())
        database_insert('Notes', User.GetUsername(), self.section, self.text)
        self.set_text_saved()

    def set_text_saved(self):
        self.ui.SavedText.setStyleSheet("color: rgb(0, 140, 0);\n"
                "font: 18pt \"Sans Serif\";")
        self.ui.SavedText.setText('Saved!')

    def set_text_unsaved(self):
        self.ui.SavedText.setStyleSheet("color: rgb(255, 0, 0);\n"
                "font: 18pt \"Sans Serif\";")
        self.ui.SavedText.setText('Unsaved')

    def set_text(self):
        self.db_text = database_query("SELECT Text FROM Notes WHERE Section=? AND Username=?", self.section, User.GetUsername())
        if len(self.db_text) == 0:
            self.text = ''
        else:
            self.text = self.db_text[0][0]
        self.set_note_text(self.text)

    def set_note_text(self, text, color='rgb(69, 69, 69)'):
        note_text = text.replace('\n', '<br>')
        self.ui.NotesText.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        f"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:18pt; font-weight:400; font-style:normal; color:{color};\">\n"
        f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{note_text}</p></body></html>")

    def not_signed_in(self):
        self.set_note_text('You must be signed in to be able to make notes',
                color='rgb(255, 0, 0)')
        self.ui.NotesText.setReadOnly(True)

    def signed_in(self):
        self.ui.NotesText.setReadOnly(False)
        self.set_text()
        self.ui.NotesText.textChanged.connect(self.set_text_unsaved)
        self.ui.TutorialTab.clicked.connect(self.goto_tutorial_notes)
        self.ui.IntroductionTab.clicked.connect(self.goto_introduction_notes)
        self.ui.InvestigationTab.clicked.connect(self.goto_investigation_notes)
        self.ui.SummaryTab.clicked.connect(self.goto_summary_notes)
        self.ui.SaveButton.clicked.connect(self.saveto_database)


class TutorialNotes(Notes):

    """
    The TutorialNotes class is used to allow the user to take notes on the
    tutorial section of the program
    """

    def __init__(self):
        super(TutorialNotes, self).__init__()
        self.section = 'Tutorial'
        self.ui = Ui_TutorialNotesScreen()
        self.ui.setupUi(self)
        self.ui.BackButton.clicked.connect(self.exit_notes)
        if User.GetSignedIn():
            self.signed_in()
            self.ui.NextButton.clicked.connect(self.goto_introduction_notes)
        else:
            self.not_signed_in()
        self.show()


class IntroductionNotes(Notes):

    """
    The IntroductionNotes class is used to allow the user to take notes on the
    introduction section of the program
    """

    def __init__(self):
        super(IntroductionNotes, self).__init__()
        self.section = 'Introduction'
        self.ui = Ui_IntroductionNotesScreen()
        self.ui.setupUi(self)
        self.ui.BackButton.clicked.connect(self.exit_notes)
        if User.GetSignedIn():
            self.signed_in()
            self.ui.NextButton.clicked.connect(self.goto_investigation_notes)
        else:
            self.not_signed_in()
        self.show()


class InvestigationNotes(Notes):

    """
    The InvestigationNotes class is used to allow the user to take notes on the
    investigation section of the program
    """

    def __init__(self):
        super(InvestigationNotes, self).__init__()
        self.section = 'Investigation'
        self.ui = Ui_InvestigationNotesScreen()
        self.ui.setupUi(self)
        self.ui.BackButton.clicked.connect(self.exit_notes)
        if User.GetSignedIn():
            self.signed_in()
            self.ui.NextButton.clicked.connect(self.goto_summary_notes)
        else:
            self.not_signed_in()
        self.show()


class SummaryNotes(Notes):

    """
    The SummaryNotes class is used to allow the user to take notes on the
    summary section of the program
    """

    def __init__(self):
        super(SummaryNotes, self).__init__()
        self.section = 'Summary'
        self.ui = Ui_SummaryNotesScreen()
        self.ui.setupUi(self)
        self.ui.BackButton.clicked.connect(self.exit_notes)
        if User.GetSignedIn():
            self.signed_in()
        else:
            self.not_signed_in()
        self.show()
