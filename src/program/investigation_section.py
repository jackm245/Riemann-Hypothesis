import sys
import matplotlib
import numpy as np
from .utils import zeta, sieve_of_eratosthenes, prime_power_function, prime_counting_function_estimation, logarithmic_integral, binary_insertion_sort, save_zeta_zeroes_to_file, save_zeta_values_to_file, make_int, make_complex, is_zeta_zero
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem, QHeaderView
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from .user_interface import MplWidget, Ui_PolarGraphScreen, Ui_PolarGraphMatPlotScreen, Ui_PrimeCountingFunctionScreen, Ui_PrimeCountingFunctionMatPlotScreen, Ui_GraphPlotsScreen, Ui_ZetaZeroesScreen, Ui_ZetaZeroesMatPlotScreen, Ui_PrimeNumbersScreen, Ui_CalculatorScreen, Ui_SingleCalculatorScreen, Ui_TableCalculatorScreen, Ui_TableCalculator2Screen, Ui_ZeroesScreen, Ui_CalculateZeroesScreen, Ui_CalculateZeroes2Screen


# the one with the table
class CalculateZeroes2(QtWidgets.QDialog):

    def __init__(self, zeroes):
        super(CalculateZeroes2, self).__init__()
        self.zeroes = zeroes
        self.ui = Ui_CalculateZeroes2Screen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)

        self.ui.PrevButton.clicked.connect(self.goto_calculate_zeroes)
        self.ui.NextButton.clicked.connect(self.goto_zeroes)

        self.ui.DatabaseButton.clicked.connect(self.saveto_database)
        self.ui.FileButton.clicked.connect(self.saveto_file)

        self.ui.ZetaTable.setRowCount(len(self.zeroes))

        for i, values in enumerate(self.zeroes):
            for j in range(len(values)):
                self.ui.ZetaTable.setItem(i,j, QTableWidgetItem(str(values[j])))
        self.ui.ZetaTable.horizontalHeader().setStretchLastSection(True)
        self.ui.ZetaTable.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        self.ui.ZetaTable.setColumnWidth(1, 100)

        self.show()

    def goto_calculate_zeroes(self):
        self.calculate_zeroes = CalculateZeroes()
        self.hide()

    def goto_zeroes(self):
        self.zeroes = ZeroesScreen()
        self.hide()

    def saveto_database(self):
        pass

    def saveto_file(self):
        filepath = 'files/zeta_zeroes.csv'
        fieldnames = ['InputReal', 'InputImag']
        save_zeta_zeroes_to_file(self.zeroes, filepath, fieldnames=fieldnames)
        self.ui.ErrorLabel.setText(f'Table contents written to {filepath}')

class CalculateZeroes(QtWidgets.QDialog):

    def __init__(self):
        super(CalculateZeroes, self).__init__()
        self.ui = Ui_CalculateZeroesScreen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)

        self.ui.PrevButton.clicked.connect(self.goto_zeroes)
        self.ui.NextButton.clicked.connect(self.goto_zeroes)
        self.ui.CalculateButton.clicked.connect(self.goto_calculate_zeroes_2)
        self.show()

    def calculate_zeroes(self):
        self.no_of_zeroes_input = self.ui.NoOfZeroesInput.text()
        self.no_of_zeroes = make_int(self.no_of_zeroes_input)
        if self.no_of_zeroes:
            if 0 < self.no_of_zeroes <= 100:
                self.ui.ErrorLabel.setText(f'Calculated {self.no_of_zeroes} zeroes')
                self.zeroes = []
                count = 0
                while len(self.zeroes) < self.no_of_zeroes:
                    accuracy = count // 500 + 100
                    real = 1/2
                    imag = count / accuracy
                    if is_zeta_zero(real, imag) and (real, round(imag, 1)) not in self.zeroes:
                        self.zeroes.append((real, round(imag, 1)))
                    count += 1
                print(self.zeroes)
            else:
                self.ui.ErrorLabel.setText('No. of Zeroes must be between 1 and 100')
        else:
                self.ui.ErrorLabel.setText('No. Of Zeroes must be a positive integer between 1 and 100')

    def goto_calculate_zeroes_2(self):
        self.calculate_zeroes()
        self.calculate_zeroes_2 = CalculateZeroes2(self.zeroes)
        self.hide()

    def goto_zeroes(self):
        self.zeroes = ZeroesScreen()
        self.hide()


class ZeroesScreen(QtWidgets.QDialog):

    def __init__(self):
        super(ZeroesScreen, self).__init__()
        self.ui = Ui_ZeroesScreen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)

        self.ui.PrevButton.clicked.connect(self.goto_calculator)
        self.ui.NextButton.clicked.connect(self.goto_main_menu)
        self.ui.GraphsTab.clicked.connect(self.goto_graph_plots)
        self.ui.PrimesTab.clicked.connect(self.goto_primes)
        self.ui.CalculatorTab.clicked.connect(self.goto_calculator)
        self.ui.CalculateButton.clicked.connect(self.goto_calculate_zeroes)
        self.show()

    def goto_main_menu(self):
        from .main_section import MainMenu
        self.main_menu = MainMenu()
        self.hide()

    def goto_graph_plots(self):
        self.polar = GraphPlot()
        self.hide()

    def goto_primes(self):
        self.primes = PrimeNumbers()
        self.hide()

    def goto_calculator(self):
        self.calculator = Calculator()
        self.hide()

    def goto_calculate_zeroes(self):
        self.zeroes = CalculateZeroes()
        self.hide()


class TableCalculator2(QtWidgets.QDialog):

    def __init__(self, table_values):
        super(TableCalculator2, self).__init__()
        self.table_values = table_values
        self.ui = Ui_TableCalculator2Screen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)

        self.ui.SingleTab.clicked.connect(self.goto_single)
        self.ui.PrevButton.clicked.connect(self.goto_table_calculator)
        self.ui.NextButton.clicked.connect(self.goto_calculator)
        self.ui.DatabaseButton.clicked.connect(self.saveto_database)
        self.ui.FileButton.clicked.connect(self.saveto_file)

        self.ui.ZetaTable.setRowCount(len(self.table_values))

        for i, values in enumerate(self.table_values):
            for j in range(len(values)):
                self.ui.ZetaTable.setItem(i,j, QTableWidgetItem(str(values[j])))
                # .setTextAlignment(QtCore.Qt.AlignCenter)

        #  self.ui.ZetaTable.resizeColumnsToContents()
        #  self.ui.ZetaTable.resizeRowsToContents()
        self.ui.ZetaTable.horizontalHeader().setStretchLastSection(True)
        self.ui.ZetaTable.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        self.ui.ZetaTable.setColumnWidth(1, 100)

        self.show()

    def goto_single(self):
        self.single = SingleCalculator()
        self.hide()

    def goto_table_calculator(self):
        self.tale_calculator = TableCalculator()
        self.hide()

    def goto_calculator(self):
        self.primes = Calculator()
        self.hide()

    def saveto_database(self):
        pass

    def saveto_file(self):
        filepath = 'files/zeta_values.csv'
        save_zeta_values_to_file(self.table_values, filepath)
        self.ui.ErrorLabel.setText(f'Table contents written to {filepath}')


class TableCalculator(QtWidgets.QDialog):

    def __init__(self):
        super(TableCalculator, self).__init__()
        self.ui = Ui_TableCalculatorScreen()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)

        self.ui.SingleTab.clicked.connect(self.goto_single)
        self.ui.PrevButton.clicked.connect(self.goto_single)
        self.ui.NextButton.clicked.connect(self.goto_calculator)
        self.ui.CalculateButton.clicked.connect(self.goto_table_calculator_2)
        self.show()


    def calculate_zeta(self):
        self.start_input = self.ui.StartInput.text()
        self.step_input = self.ui.StepInput.text()
        self.range_input = self.ui.NoOfValuesInput.text()
        self.start_complex = make_complex(self.start_input)
        self.step_complex = make_complex(self.step_input)
        self.range = make_int(self.range_input)
        if self.start_complex and self.step_complex:
            if 1 <= self.range <= 100:
                self.ui.ErrorLabel.setText('')
                self.input_values = [self.start_complex + self.step_complex * i for i in range(self.range)]
                zetas = [zeta(i) for i in self.input_values]
                self.output_values = [complex(round(i.real, 3), round(i.imag, 3)) for i in zetas]
                self.table_values =  list(zip(self.input_values, self.output_values))
            else:
                self.ui.ErrorLabel.setText('No. Of Values must be a positive integer between 1 and 100')
                self.table_values = False
        else:
            self.ui.ErrorLabel.setText('Start Value and Step must be complex numbers of the form a+bi')
            self.table_values = False

    def goto_table_calculator_2(self):
        self.calculate_zeta()
        if self.table_values:
            self.table_calculator_2 = TableCalculator2(self.table_values)
            self.hide()

    def goto_single(self):
        self.single = SingleCalculator()
        self.hide()

    def goto_calculator(self):
        self.calculator = Calculator()
        self.hide()


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
        self.ui.DatabaseButton.clicked.connect(self.saveto_database)
        self.ui.FileButton.clicked.connect(self.saveto_file)
        self.show()

    def calculate_zeta(self):
        self.zeta_user_input = self.ui.ZetaInput.text()
        try:
            self.zeta_input = complex(self.zeta_user_input.replace('i', 'j'))
        except ValueError as e:
            self.ui.ErrorLabel.setText('Input must be a complex number of the form a+bi')
            self.ui.ZetaOutput.setText('')
        else:
            self.zeta_output = zeta(self.zeta_input)
            self.zeta_output_printable = complex(round(self.zeta_output.real, 3), round(self.zeta_output.imag, 3))
            self.zeta_value = [(self.zeta_input, self.zeta_output_printable)]
            self.ui.ZetaOutput.setText(f'{str(self.zeta_output_printable)[1:-2]}i')
            self.ui.ErrorLabel.setText('')

    def goto_calculator(self):
        self.calculator = Calculator()
        self.hide()

    def goto_table(self):
        self.table = TableCalculator()
        self.hide()

    def saveto_database(self):
        pass

    def saveto_file(self):
        filepath = 'files/zeta_values.csv'
        save_zeta_values_to_file(self.zeta_value, filepath)
        self.ui.ErrorLabel.setText(f'Values written to {filepath}')


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
        self.zeroes = ZeroesScreen()
        self.hide()

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
        self.zeroes = ZeroesScreen()
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
        self.ui.ZeroesTab.clicked.connect(self.goto_zeroes)
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

    def goto_zeroes(self):
        self.primes = ZeroesScreen()
        self.hide()
