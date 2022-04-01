"""
screen_design.py
================

Contains the Screen class
"""


from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from ..user_interface import Ui_MatPlotScreen
from .database_functions import database_query, database_insert, database_select, get_id
from .user import User


class Screen(QtWidgets.QDialog):

    """
    The Screen Class is inherited by all of the other classes that are used
    to interact witht the GUI

    The prupose of this class is to set some default values, and automatically
    run functions that are common to every class that inherits it

    It also contains some functions which are commonly run by classes that
    inherit it
    """

    def __init__(self):
        super(Screen, self).__init__()
        self.setFixedWidth(1340)
        self.setFixedHeight(720)

    def goto_mainmenu(self):
        from ..main_section import MainMenu
        self.main_menu = MainMenu()
        self.hide()

    def setup_question(self):
        """
        This function is only called if there is a question that the user can answer on that page

        This function will set the QuestionText label in the gui to the question that is being asked, and if the user is signed in, and has previously answered the question correctly, then their previous answer will be displayed
        """
        self.ui.SubmitButton.clicked.connect(self.check_answer)
        self.ui.QuestionText.setStyleSheet("font-size: 16pt; font-weight: 600;")
        self.text = database_query("SELECT Question FROM Questions WHERE Question_No=?", self.question_no)[0][0]
        self.correct_answers = [answer[0] for answer in database_query("SELECT CorrectAnswer From CorrectAnswers WHERE Question_No=?", self.question_no)]
        self.lowercase_correct_answers = list(map(lambda answer : answer.lower(), self.correct_answers))
        self.ui.QuestionText.setText(self.center_text(self.text))
        if User.GetSignedIn():
            self.usernames = [username[0] for username in database_query("SELECT Username FROM UsersAnswers WHERE Question_No=?", self.question_no)]
            if User.GetUsername() in self.usernames:
                self.users_answer = str(database_query("SELECT UsersAnswer FROM UsersAnswers WHERE Question_No=? AND Username=?", self.question_no, User.GetUsername())[0][0])
                if self.users_answer.lower() in self.lowercase_correct_answers:
                    self.ui.QuestionInput.setText(self.users_answer)
                    self.set_label_correct()

    def check_answer(self):
        self.users_answer = self.ui.QuestionInput.text().lower()
        if self.users_answer.lower() in self.lowercase_correct_answers:
            self.set_label_correct()
        else:
            self.set_label_incorrect()
        if User.GetSignedIn():
            self.add_answer_to_db()

    def set_label_correct(self):
        self.ui.MessageLabel.setStyleSheet("color: rgb(0, 140, 0);\n"
                "font: 18pt \"Sans Serif\";")
        self.ui.MessageLabel.setText(self.center_text('Correct!'))
        self.ui.QuestionInput.setReadOnly(True)

    def set_label_incorrect(self):
        self.ui.MessageLabel.setStyleSheet("color: rgb(255, 0, 0);\n"
                "font: 18pt \"Sans Serif\";")
        self.ui.MessageLabel.setText(self.center_text('Incorrect, try again'))

    def add_answer_to_db(self):
        """
        This function is only run if the user is already signed in
        Add the User's Answer to the question to the database, whether it's
        right or wrong

        Will add the user's answer to UserAnswer table
        If User had already answered the question, the record in the database
        will need to be deleted before the new one is inserted.
        """
        database_query("DELETE FROM UsersAnswers WHERE Username=? AND Question_No=?", User.GetUsername(), self.question_no)
        database_insert('UsersAnswers', self.question_no, User.GetUsername(), self.users_answer)

    def center_text(self, text):
        return f'<html><head/><body><p align=\"center\">{text}</p></body></html>'


class MplWidget(Screen):
    """ A Matplotlib Widget """

    def __init__(self, parent=None):
        super(MplWidget, self).__init__()
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.axes = self.figure.add_subplot(111)
        self.layoutvertical = QtWidgets.QVBoxLayout(self)
        self.layoutvertical.addWidget(self.canvas)


class StaticGraphScreen(Screen):

    """
    Static Graph Screen
    """

    def __init__(self):
        super(StaticGraphScreen, self).__init__()
        self.ui = Ui_MatPlotScreen()
        self.ui.setupUi(self)
        self.init_widget()
        self.x_vals = []
        self.y_vals= []

    def init_widget(self):
        self.matplotlibwidget = MplWidget()
        self.layoutvertical = QtWidgets.QVBoxLayout(self)
        self.layoutvertical.addWidget(self.matplotlibwidget)


class DynamicGraphScreen(StaticGraphScreen):

    """
    Dynamic Graph Screen
    """

    def __init__(self):
        super(DynamicGraphScreen, self).__init__()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_figure)
        self.timer.start(100)
        self.count = 0

    def update_figure(self):
        self.x_vals.append(self.count)
        self.y_vals.append(self.count)
        self.matplotlibwidget.axes.cla()
        self.matplotlibwidget.axes.plot(self.x_vals, self.y_vals, label=f'y=x', color='blue')
        self.matplotlibwidget.axes.legend(loc='upper left')
        self.matplotlibwidget.canvas.draw()
        self.count += 1
