import sys
import matplotlib
import numpy as np
import re
from .utils import zeta, sieve_of_eratosthenes, prime_power_function, prime_counting_function_estimation, logarithmic_integral
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from .user_interface import MplWidget, Ui_PolarGraphScreen, Ui_PolarGraphMatPlotScreen, Ui_PrimeCountingFunctionScreen, Ui_PrimeCountingFunctionMatPlotScreen, Ui_GraphPlotsScreen, Ui_ZetaZeroesScreen, Ui_ZetaZeroesMatPlotScreen, Ui_PrimeNumbersScreen, Ui_CalculatorScreen, Ui_SingleCalculatorScreen


class SingleCalculator(QtWidgets.QDialog):

    def __init__(self):
        super(SingleCalculator, self).__init__()
        self.ui = Ui_SingleCalculatorScreen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)

        self.ui.TableTab.clicked.connect(self.goto_table)
        self.ui.PrevButton.clicked.connect(self.goto_calculator)
        self.ui.NextButton.clicked.connect(self.goto_table)
        self.ui.CalculateButton.clicked.connect(self.calculate_zeta)
        self.ui.DatabaseButton.clicked.connect(self.storeto_database)
        self.ui.FileButton.clicked.connect(self.storeto_file)
        self.show()

    def calculate_zeta(self):
        #  self.calculator = Calculator()
        #  self.hide()
        self.zeta_user_input = self.ui.ZetaInput.text()
        # a
        # a.b
        # a+ci
        # a.b+ci
        # a.b+c.di
        # a+c.di
        try:
            self.zeta_input = complex(self.zeta_user_input.replace('i', 'j'))
        except ValueError as e:
            self.ui.ErrorLabel.setText('Input must be a complex number of the form a+bi')
            self.ui.ZetaOutput.setText('')
        else:
            self.zeta_output = zeta(self.zeta_input)
            self.zeta_output_printable = complex(round(self.zeta_output.real, 3), round(self.zeta_output.imag, 3))
            self.ui.ZetaOutput.setText(f'{str(self.zeta_output_printable)[1:-1]}')
            self.ui.ErrorLabel.setText('')

        #  if re.fullmatch(r'^\d+(\.\d+)?(\+\d+(\.\d+)?i)?$', self.zeta_input):
            #  self.zeta_output = zeta(complex(self.zeta_input))
            #  self.zeta_output_printable = complex(round(self.zeta_output.real, 2), round(self.zeta_output.imag, 2))
            #  self.ui.ZetaOutput.setText(f'{str(self.zeta_output_printable)}i')
        #  elif re.fullmatch(r'^(\d+(\.\d+)?\+)?\d+(\.\d+)?i$', self.zeta_input):
        #  else:
            #  self.ui.ErrorLabel.setText("Input must be a complex number of the form a+bi")

    def goto_calculator(self):
        self.calculator = Calculator()
        self.hide()
        #  self.zeta_input = self.ui.ZetaInput.text()
        #  if re.fullmatch(r'^(\d+(\.\d+)?(\+\d+(\.\d+)?i)?)|((\d+(\.\d+)?\+)?\d+(\.\d+)?i)$', self.zeta_input):
            #  self.ui.ErrorLabel.setText("Match")
        #  else:
            #  self.ui.ErrorLabel.setText("Not Match")


    def goto_table(self):
        self.table = TableCalculator()
        self.hide()

    def calculate(self):
        pass

    def storeto_database(self):
        pass

    def storeto_file(self):
        pass

class Calculator(QtWidgets.QDialog):

    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_CalculatorScreen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)

        self.ui.PrevButton.clicked.connect(self.goto_primes)
        self.ui.NextButton.clicked.connect(self.goto_zeroes)
        self.ui.GraphsTab.clicked.connect(self.goto_graph_plots)
        self.ui.PrimesTab.clicked.connect(self.goto_primes)
        self.ui.ZeroesTab.clicked.connect(self.goto_zeroes)
        self.ui.SingleButton.clicked.connect(self.goto_single)
        self.ui.TableButton.clicked.connect(self.goto_table)

        self.show()

    def goto_graph_plots(self):
        self.main_menu = GraphPlot()
        self.hide()

    def goto_primes(self):
        self.primes = PrimeNumbers()
        self.hide()

    def goto_zeroes(self):
        pass
        #  self.zeroes = Zeroes()
        #  self.hide()

    def goto_single(self):
        self.single = SingleCalculator()
        self.hide()

    def goto_table(self):
        self.table = TableCalculator()
        self.hide()


class PrimeNumbers(QtWidgets.QDialog):

    def __init__(self):
        super(PrimeNumbers, self).__init__()
        self.ui = Ui_PrimeNumbersScreen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)

        self.ui.PrevButton.clicked.connect(self.goto_graph_plots)
        self.ui.NextButton.clicked.connect(self.goto_calculator)
        self.ui.GraphsTab.clicked.connect(self.goto_graph_plots)
        self.ui.CalculatorTab.clicked.connect(self.goto_calculator)
        self.ui.ZeroesTab.clicked.connect(self.goto_zeroes)
        self.show()


    def goto_graph_plots(self):
        self.main_menu = GraphPlot()
        self.hide()

    def goto_calculator(self):
        self.calculator = Calculator()
        self.hide()

    def goto_zeroes(self):
        self.zeroes = Zeroes()
        self.hide()


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
        self.ui.ZeroesTab.clicked.connect(self.goto_zeroes)
        self.ui.PrevButton.clicked.connect(self.goto_zeroes)
        self.ui.GraphButton.clicked.connect(self.pcf_graph)
        self.ui.NextButton.clicked.connect(self.goto_graph_plots)
        self.show()

    def goto_polar(self):
        self.polar = PolarGraph()
        self.hide()

    def goto_zeroes(self):
        self.zeroes = ZetaZeroes()
        self.hide()

    def pcf_graph(self):
        self.graph = PrimeCountingFunctionMatPlot()

    def goto_graph_plots(self):
        self.graph_plots = GraphPlot()
        self.hide()


class ZetaZeroesMatPlot(QtWidgets.QDialog):

    def __init__(self):
        super(ZetaZeroesMatPlot, self).__init__()
        self.ui = Ui_ZetaZeroesMatPlotScreen()
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

    def is_root(self):
        zeta_value = zeta(complex(1/2, self.count/self.accuracy))
        return abs(zeta_value) < 10e-3


    def init_widget(self):
        self.matplotlibwidget = MplWidget()
        self.layoutvertical = QtWidgets.QVBoxLayout(self)
        self.layoutvertical.addWidget(self.matplotlibwidget)


    def update_figure(self):
        self.accuracy = self.count//500 + 100
        if self.is_root():
            self.x_vals.append(1/2)
            self.y_vals.append(self.count/self.accuracy)
        self.matplotlibwidget.axes.cla()

        self.matplotlibwidget.axes.scatter(self.x_vals, self.y_vals)
        #  self.axes.xlabel('Re')
        #  self.axes.ylabel('Im')
        self.matplotlibwidget.axes.set_ylim(0)
        self.matplotlibwidget.axes.set_xlim(0, 1)
        self.matplotlibwidget.canvas.draw()
        self.count += 1

class ZetaZeroes(QtWidgets.QDialog):

    def __init__(self):
        super(ZetaZeroes, self).__init__()
        self.ui = Ui_ZetaZeroesScreen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)

        #  self.ui.PrimeTab.clicked.connect(self.goto_prime)
        self.ui.PolarTab.clicked.connect(self.goto_polar)
        self.ui.PrimeTab.clicked.connect(self.goto_prime)
        self.ui.PrevButton.clicked.connect(self.goto_polar)
        self.ui.GraphButton.clicked.connect(self.goto_zeta_zeroes_graph)
        self.ui.NextButton.clicked.connect(self.goto_prime)
        self.show()

    def goto_polar(self):
        self.polar = PolarGraph()
        self.hide()

    def goto_prime(self):
        self.prime = PrimeCountingFunction()
        self.hide()

    def goto_zeta_zeroes_graph(self):
        self.zeta_zeroes_graph = ZetaZeroesMatPlot()


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

        self.ui.ZeroesTab.clicked.connect(self.goto_zeroes)
        self.ui.PrimeTab.clicked.connect(self.goto_prime)
        self.ui.PrevButton.clicked.connect(self.goto_graph_plots)
        self.ui.GraphButton.clicked.connect(self.polar_graph)
        self.ui.NextButton.clicked.connect(self.goto_zeroes)
        self.show()

    def goto_zeroes(self):
        self.zeroes = ZetaZeroes()
        self.hide()

    def goto_prime(self):
        self.prime = PrimeCountingFunction()
        self.hide()

    def goto_graph_plots(self):
        self.graph_plots = GraphPlot()
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


class GraphPlot(QtWidgets.QDialog):

    def __init__(self):
        super(GraphPlot, self).__init__()
        self.ui = Ui_GraphPlotsScreen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)

        self.ui.PrevButton.clicked.connect(self.goto_main_menu)
        self.ui.NextButton.clicked.connect(self.goto_primes)
        self.ui.GraphPlotsButton.clicked.connect(self.goto_polar)
        self.ui.PrimesTab.clicked.connect(self.goto_primes)
        self.ui.CalculatorTab.clicked.connect(self.goto_calculator)
        self.show()

    def goto_main_menu(self):
        from .main_section import MainMenu
        self.main_menu = MainMenu()
        self.hide()

    def goto_polar(self):
        self.polar = PolarGraph()
        self.hide()

    def goto_primes(self):
        self.primes = PrimeNumbers()
        self.hide()

    def goto_calculator(self):
        self.primes = Calculator()
        self.hide()
