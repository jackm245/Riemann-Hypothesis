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
        self.ui.SubmitButton.clicked.connect(self.check_answer)
        self.ui.QuestionText.setStyleSheet("font-size: 16pt; font-weight: 600;")
        self.text, self.correct_answer_id = database_query("SELECT Question, Answer_ID FROM Questions WHERE Question_No=?", [self.question_no])[0]
        self.correct_answer = database_query("SELECT Answer From Answers WHERE Answer_ID=?", [self.correct_answer_id])[0][0]
        self.ui.QuestionText.setText(self.center_text(self.text))
        if User.GetSignedIn():
            # if already got correct, display answer, correct, and make read only
            # if user_id in useranswers
            self.user_ids = [id[0] for id in database_query("SELECT User_ID FROM UserAnswer WHERE Question_ID=?", [self.question_no])]
            #  print('uid ', self.user_ids)
            if User.GetUserID() in self.user_ids:
                # if user has already answered the quetsion
                self.answer_id = database_query("SELECT Answer_ID FROM UserAnswer WHERE User_ID=? AND Question_ID=?", [User.GetUserID(), self.question_no])[0][0]
                #  self.users_answers = database_query("SELECT Answer FROM Answers WHERE Answer_ID=?", [self.answer_id])
                self.users_answer = database_query("SELECT Answer FROM Answers WHERE Answer_ID=?", [self.answer_id])[0][0]
                #  print(self.users_answers)
                #  print(self.users_answer.lower(), self.correct_answer.lower())
                if self.users_answer.lower() == self.correct_answer.lower():
                    self.ui.QuestionInput.setText(self.correct_answer)
                    self.set_label_correct()

    def check_answer(self):
        self.answer = self.ui.QuestionInput.text().lower()
        if self.answer == self.correct_answer.lower():
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
        # also need to add to UserAnswer //
        # so will need to be signed in //
        # also if they are signed in and have the q already right, autocomplete and say correct so dont add it again //
        # also need to remove old entries so dont have repeats if they got it wrong //
        # potentially get rid of either question_id or question_no as repeated

        # add answer if not already in answers
        self.answers = [answer[0].lower() for answer in database_select(['Answer'], ['Answers'])]
        #  print(self.answers)
        if self.answer not in self.answers:
            database_insert('Answers', [get_id('Answer_ID', 'Answers'), self.answer])
        self.answer_id = database_query('SELECT Answer_ID FROM Answers WHERE LOWER(Answer)=?', [self.answer])[0][0]
        # remove userid's record if already in and replace with new one
        #  self.user_ids = database_select(['User_IDs'], ['UserAnswer'])
        #  if User.GetUserID() in self.user_ids:
        database_query("DELETE FROM UserAnswer WHERE User_ID=? AND Question_ID=?", [User.GetUserID(), self.question_no])
        database_insert('UserAnswer', [User.GetUserID(), self.question_no, self.answer_id])

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
