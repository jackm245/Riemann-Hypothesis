"""
screen_design.py
================

Contains the Screen class
"""


from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


__all__ = ['Screen']


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
        self.layoutvertical.setGeometry(QtCore.QRect(500, 500, 500,500))
        self.layoutvertical.addWidget(self.canvas)


class StaticGraphScreen(Screen):

    """
    Graph Screen
    """

    def __init__(self):
        super(StaticGraphScreen, self).__init__()
        #  self.init_widget()
        self.x_vals = []
        self.y_vals= []

    def init_widget(self):
        self.matplotlibwidget = MplWidget()
        self.layoutvertical = QtWidgets.QVBoxLayout(self)
        self.layoutvertical.addWidget(self.matplotlibwidget)

class DynamicGraphScreen(StaticGraphScreen):

    """
    Graph Screen
    """

    def __init__(self):
        super(DynamicGraphScreen, self).__init__()
        #  self.init_widget()
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
