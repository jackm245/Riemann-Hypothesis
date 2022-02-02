import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from .user_interface import MplWidget, Ui_PolarGraphScreen, Ui_PolarGraphMatPlotScreen
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from itertools import islice, count


def binom(n, k):
    v = 1
    for i in range(k):
        v *= (n - i) / (i + 1)
    return v


def zeta(s, t=100):
    if s == 1: return float("inf")
    term = (1 / 2 ** (n + 1) * sum((-1) ** k * binom(n, k) * (k + 1) ** -s
                                   for k in range(n + 1)) for n in count(0))
    return sum(islice(term, t)) / (1 - 2 ** (1 - s))


class PolarGraphMatPlot(QtWidgets.QDialog):

    def __init__(self, real_input):
        super(PolarGraphMatPlot, self).__init__()
        self.real_input = real_input
        self.ui = Ui_PolarGraphMatPlotScreen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)
        self.init_widget()

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_figure)
        self.timer.start(100)
        self.x_vals = []
        self.y_vals = []
        self.count = 0

        self.show()

    def init_widget(self):
        self.matplotlibwidget = MplWidget()
        self.layoutvertical = QtWidgets.QVBoxLayout(self)
        self.layoutvertical.addWidget(self.matplotlibwidget)


    def update_figure(self):
        new_zeta = zeta(complex(self.real_input, self.count/25))
        self.x_vals.append(new_zeta.real)
        self.y_vals.append(new_zeta.imag)
        self.matplotlibwidget.axes.cla()
        self.matplotlibwidget.axes.plot(self.x_vals, self.y_vals, 'r')
        #  self.axes.xlabel('Re')
        #  self.axes.ylabel('Im')
        self.matplotlibwidget.canvas.draw()
        self.count += 1


class PolarGraph(QtWidgets.QDialog):

    def __init__(self):
        super(PolarGraph, self).__init__()
        self.ui = Ui_PolarGraphScreen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)



        self.ui.PrevButton.clicked.connect(self.goto_main_menu)
        self.ui.GraphButton.clicked.connect(self.polar_graph)
        self.show()

    def goto_main_menu(self):
        from .main_section import MainMenu
        self.main_menu = MainMenu()
        self.hide()


    def polar_graph(self):
        self.real_input = self.ui.GraphInput.text()
        try:
            self.real_input = float(self.real_input)
        except ValueError:
            self.ui.ErrorLabel.setText("Error: Input must be whole number or a decimal")
        else:
            if self.real_input == 1:
                self.ui.ErrorLabel.setText("Error: Input must not be equal to 1")
            else:
                self.graph = PolarGraphMatPlot(self.real_input)

