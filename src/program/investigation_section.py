import sys
import matplotlib
import numpy as np
from .utils import zeta, sieve_of_eratosthenes, prime_power_function, prime_counting_function_estimation, logarithmic_integral
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from .user_interface import MplWidget, Ui_PolarGraphScreen, Ui_PolarGraphMatPlotScreen, Ui_PrimeCountingFunctionScreen, Ui_PrimeCountingFunctionMatPlotScreen


class PrimeCountingFunctionMatPlot(QtWidgets.QDialog):

    def __init__(self):
        super(PrimeCountingFunctionMatPlot, self).__init__()
        self.ui = Ui_PrimeCountingFunctionMatPlotScreen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)
        self.init_widget()

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_figure)
        self.timer.start(100)
        self.x_vals = []
        self.y_vals_pcf = []
        self.y_vals_x_logx= []
        self.y_vals_li = []
        self.y_vals_ppf = []

        self.count = 2

        self.show()

    def init_widget(self):
        self.matplotlibwidget = MplWidget()
        self.layoutvertical = QtWidgets.QVBoxLayout(self)
        self.layoutvertical.addWidget(self.matplotlibwidget)


    def update_figure(self):
        self.x_vals.append(self.count)
        self.y_vals_pcf.append(sieve_of_eratosthenes(self.count).size)
        self.y_vals_x_logx.append(prime_counting_function_estimation(self.count))
        self.y_vals_li.append(logarithmic_integral(self.count))
        self.y_vals_ppf.append(prime_power_function(self.count))
        self.matplotlibwidget.axes.cla()

        self.matplotlibwidget.axes.scatter(self.x_vals, self.y_vals_pcf, label='Prime Counting Function')
        self.matplotlibwidget.axes.plot(self.x_vals, self.y_vals_x_logx, label='x / log(x)', color='red')
        self.matplotlibwidget.axes.plot(self.x_vals, self.y_vals_li, label='Logarithmic Integral', color='green')
        self.matplotlibwidget.axes.plot(self.x_vals, self.y_vals_ppf, label='Prime Power Function', color='blue')

        self.matplotlibwidget.axes.legend(loc='upper left')


        #  self.axes.xlabel('Re')
        #  self.axes.ylabel('Im')
        self.matplotlibwidget.canvas.draw()
        self.count += 1


class PrimeCountingFunction(QtWidgets.QDialog):

    def __init__(self):
        super(PrimeCountingFunction, self).__init__()
        self.ui = Ui_PrimeCountingFunctionScreen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)

        self.ui.PolarTab.clicked.connect(self.goto_polar)
        self.ui.PrevButton.clicked.connect(self.goto_main_menu)
        self.ui.GraphButton.clicked.connect(self.pcf_graph)
        self.show()


    def goto_polar(self):
        self.polar = PolarGraph()
        self.hide()


    def goto_main_menu(self):
        from .main_section import MainMenu
        self.main_menu = MainMenu()
        self.hide()


    def pcf_graph(self):
        self.graph = PrimeCountingFunctionMatPlot()



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

        self.ui.PrimeTab.clicked.connect(self.goto_prime)
        self.ui.PrevButton.clicked.connect(self.goto_main_menu)
        self.ui.GraphButton.clicked.connect(self.polar_graph)
        self.show()


    def goto_main_menu(self):
        from .main_section import MainMenu
        self.main_menu = MainMenu()
        self.hide()


    def goto_prime(self):
        self.prime = PrimeCountingFunction()
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

