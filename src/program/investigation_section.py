"""
investigation_section.py
========================

Contains all of the classes used to interact with the GUI for the
investigation section of the project

Includes the classes:
    - InvestigationSection
    - CalculateZeroes2
    - CalculateZeroes
    - Zeroes
    - CalculatorLeaderboard
    - TableCalculator2
    - TableCalculator
    - SingleCalculator
    - Calculator
    - PrimeNumbers
    - ZetaApproximationMatPlot
    - ZetaApproximation
    - PrimeCountingFunctionMatPlot
    - PrimeCountingFunction
    - ZetaZeroesMatPlot
    - ZetaZeroesPlot
    - PolarGraphMatPlot
    - PolarGraph
    - GraphPlot

Objectives completed in this file:
    1. 1(a), 1(b), 1(c), 1(d)
    4. 4(a), 4(b), 4(c), 4(d)
    5. 5(a), 5(b), 5(c), 5(d)
    6. 6(a), 6(b), 6(c)
    7(a)i 7(a)ii 7(a)iii
"""

import sys
import matplotlib
import numpy as np
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem, QHeaderView
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from .notes import InvestigationNotes
from .user_interface import Ui_PolarGraphScreen, Ui_PrimeCountingFunctionScreen, Ui_GraphPlotsScreen, Ui_ZetaZeroesPlotScreen, Ui_PrimeNumbersScreen, Ui_CalculatorScreen, Ui_SingleCalculatorScreen, Ui_TableCalculatorScreen, Ui_TableCalculator2Screen, Ui_CalculateZeroesScreen, Ui_CalculateZeroes2Screen, Ui_CalculatorLeaderboardScreen, Ui_MatPlotScreen, Ui_ZeroesScreen, Ui_ZetaApproximationScreen
from .utils import zeta, sieve_of_eratosthenes, prime_power_function, prime_counting_function_estimation, logarithmic_integral, binary_insertion_sort, save_zeta_zeroes_to_file, save_zeta_values_to_file, make_int, make_complex, is_zeta_zero, Screen, User, database_query, database_insert, database_select, get_id, database_print, DynamicGraphScreen, Complex, Queue, round_to_3_sf


class InvestigationSection(Screen):

    """
    A class inherited by all of the Screens/Page classes in the investigation section
    of the program

    The functions defined in this class allow for different pages to be loaded
    and hidden, so that the user is able to navigate to different parts of the
    program using the GUI
    """

    def __init__(self):
        super(InvestigationSection, self).__init__()

    def setup_tabs(self):
        try:
            self.ui.NotesButton.clicked.connect(self.goto_investigation_notes)
        except AttributeError:
            pass
        try:
            self.ui.ZetaZeroesPlotTab.clicked.connect(self.goto_zeta_zeroes_plot)
        except AttributeError:
            pass
        try:
            self.ui.PrimeTab.clicked.connect(self.goto_prime)
        except AttributeError:
            pass
        try:
            self.ui.PrimesTab.clicked.connect(self.goto_primes)
        except AttributeError:
            pass
        try:
            self.ui.CalculatorTab.clicked.connect(self.goto_calculator)
        except AttributeError:
            pass
        try:
            self.ui.ZeroesTab.clicked.connect(self.goto_zeroes)
        except AttributeError:
            pass
        try:
            self.ui.PolarTab.clicked.connect(self.goto_polar)
        except AttributeError:
            pass
        try:
            self.ui.GraphsTab.clicked.connect(self.goto_graph_plots)
        except AttributeError:
            pass
        try:
            self.ui.TableTab.clicked.connect(self.goto_table_calculator)
        except AttributeError:
            pass
        try:
            self.ui.LeaderboardTab.clicked.connect(self.goto_calculator_leaderboard)
        except AttributeError:
            pass
        try:
            self.ui.SingleTab.clicked.connect(self.goto_single)
        except AttributeError:
            pass
        try:
            self.ui.ZetaApproximationTab.clicked.connect(self.goto_zeta_approximation)
        except AttributeError:
            pass

    def goto_polar(self):
        self.polar = PolarGraph()
        self.hide()

    def goto_zeroes(self):
        self.zeroes = Zeroes()
        self.hide()

    def goto_prime(self):
        self.prime = PrimeCountingFunction()
        self.hide()

    def goto_zeta_zeroes_graph(self):
        self.zeta_zeroes_graph = ZetaZeroesMatPlot()

    def goto_pcf_graph(self):
        self.graph = PrimeCountingFunctionMatPlot()

    def goto_graph_plots(self):
        self.polar = GraphPlot()
        self.hide()

    def goto_primes(self):
        self.primes = PrimeNumbers()
        self.hide()

    def goto_calculator(self):
        self.calculator = Calculator()
        self.hide()

    def goto_zeta_zeroes_plot(self):
        self.zeroes_plot = ZetaZeroesPlot()
        self.hide()

    def goto_calculate_zeroes(self):
        self.zeroes = CalculateZeroes()
        self.hide()

    def goto_calculate_zeroes_2(self):
        self.ui.ErrorLabel.setText(self.center_text(f'Calculating...'))
        self.calculate_zeroes()
        if self.zeroes_calculated:
            self.calculate_zeroes_2 = CalculateZeroes2(self.zeroes)
            self.hide()

    def goto_single(self):
        self.single = SingleCalculator()
        self.hide()

    def goto_table_calculator(self):
        self.tale_calculator = TableCalculator()
        self.hide()

    def goto_table_calculator_2(self):
        self.calculate_zeta()
        if self.table_values:
            self.table_calculator_2 = TableCalculator2(self.table_values)
            self.hide()

    def goto_calculator_leaderboard(self):
        self.calculator_leaderboard = CalculatorLeaderboard()
        self.hide()

    def goto_investigation_notes(self):
        self.investigation_notes = InvestigationNotes()

    def goto_zeta_approximation(self):
        self.zeta_approximation = ZetaApproximation()
        self.hide()

    def validate_input(self, complex_user_input, split_char):
        split_input = complex_user_input.split(split_char)
        assert 0 < len(split_input) <= 2
        if len(split_input) == 2:
            assert complex_user_input[-1] in ['i', 'j']
            split_input[1] = split_input[1][:-1]
        return Complex(*split_input)

    def get_valid_complex_input(self, complex_user_input):

        """
        Converts a string of a complex number into type Complex
        string must be of type:
            a
            -a
            bi
            -bi
            a+bi
            a-bi
            -a+bi
            -a-bi
        """

        is_real_negative = False
        try:
            complex_input = self.validate_input(complex_user_input, '+')
        except (AssertionError, ValueError, IndexError):
            try:
                if complex_user_input[0] == '-':
                    complex_user_input = complex_user_input[1:]
                    is_real_negative = True
                complex_input = self.validate_input(complex_user_input, '-')
                if is_real_negative:
                    complex_input = Complex((-1)*complex_input.get_real(), (-1)*complex_input.get_imag())
                else:
                    complex_input = Complex(complex_input.get_real(), (-1)*complex_input.get_imag())
            except (AssertionError, ValueError, IndexError):
                complex_input = None
        return complex_input


class CalculateZeroes2(InvestigationSection):

    """
    The CalculateZeroes2 class is used to display the zeta zeroes that have
    been calculated by the user

    The user then has the option to save these to the database or to a file
    """

    def __init__(self, zeroes):
        super(CalculateZeroes2, self).__init__()
        self.table_zeroes = zeroes
        self.ui = Ui_CalculateZeroes2Screen()
        self.ui.setupUi(self)
        self.setup_tabs()
        self.ui.PrevButton.clicked.connect(self.goto_calculate_zeroes)
        self.ui.NextButton.clicked.connect(self.goto_zeroes)
        self.ui.DatabaseButton.clicked.connect(self.saveto_database)
        self.ui.FileButton.clicked.connect(self.saveto_file)
        self.ui.ZetaTable.setRowCount(self.table_zeroes.get_size())
        self.zeroes = []
        for row_no in range(self.table_zeroes.get_size()):
            row = self.table_zeroes.deQueue()
            for col_no, element in enumerate(row):
                self.ui.ZetaTable.setItem(row_no, col_no, QTableWidgetItem(str(element)))
            self.zeroes.append(row)
        #  for i, values in enumerate(self.zeroes):
            #  for j in range(len(values)):
                #  self.ui.ZetaTable.setItem(i,j, QTableWidgetItem(str(values[j])))
        self.ui.ZetaTable.horizontalHeader().setStretchLastSection(True)
        self.ui.ZetaTable.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        self.ui.ZetaTable.setColumnWidth(1, 100)
        self.show()

    def saveto_database(self):
        if User.GetUsername():
            database_inputs = database_select(['Zero_Real_Input', 'Zero_Imag_Input'], ['Zeroes'])
            for real, imag in self.zeroes:
                # if there is a row with the same real and imag
                in_table = False
                for real_input, imag_input in database_inputs:
                    if real_input == real and imag_input == imag:
                        in_table = True
                # only add to database if not already in database
                if not in_table:
                    self.Zeta_Zero_ID = get_id('Zero_ID', 'Zeroes')
                    database_insert('Zeroes', self.Zeta_Zero_ID, real, imag)
                    database_insert('UserZeroes', self.Zeta_Zero_ID, User.GetUsername())
            self.ui.ErrorLabel.setText(self.center_text('Zeroes saved to database'))
        else:
            self.ui.ErrorLabel.setText(self.center_text(f'You must be signed in to be able to '
                    'save to the database'))

    def saveto_file(self):
        filepath = 'files/zeta_zeroes.csv'
        fieldnames = ['InputReal', 'InputImag']
        save_zeta_zeroes_to_file(self.zeroes, filepath, fieldnames=fieldnames)
        self.ui.ErrorLabel.setText(self.center_text(f'Table contents written to {filepath}'))


class CalculateZeroes(InvestigationSection):

    """
    The CalculateZeroes class is used to ask for input from the user as to how
    many zeta zeroes they want to calculate. It then calculates these values
    and displays them in the CalculateZeroes2 screen
    """

    def __init__(self):
        super(CalculateZeroes, self).__init__()
        self.ui = Ui_CalculateZeroesScreen()
        self.zeroes = []
        self.ui.setupUi(self)
        self.setup_tabs()
        self.ui.PrevButton.clicked.connect(self.goto_zeroes)
        self.ui.NextButton.clicked.connect(self.goto_zeroes)
        self.ui.CalculateButton.clicked.connect(self.goto_calculate_zeroes_2)
        self.show()

    def calculate_zeroes(self):
        self.no_of_zeroes_input = self.ui.NoOfZeroesInput.text()
        self.no_of_zeroes = make_int(self.no_of_zeroes_input)
        self.zeroes_calculated = False
        if self.no_of_zeroes:
            if 0 < self.no_of_zeroes <= 100:
                self.zeroes_calculated = True
                self.zeroes = Queue(max_size=self.no_of_zeroes)
                count = 0
                while self.zeroes.get_size() < self.no_of_zeroes:
                    accuracy = count // 500 + 100
                    real = 1/2
                    imag = count / accuracy
                    if is_zeta_zero(real, imag) and [real, round(imag, 1)] not in self.zeroes.get_queue():
                        self.zeroes.enQueue([real, round(imag, 1)])
                    count += 1
            else:
                self.ui.ErrorLabel.setText(self.center_text('No. of Zeroes must be between 1 and 100'))
        else:
                self.ui.ErrorLabel.setText(self.center_text('No. Of Zeroes must be a positive integer between 1 and 100'))


class Zeroes(InvestigationSection):

    """
    The Zeroes class is used to display the zeroes screen, where the user can
    calculate the non-trivial zeroes of the Riemann Zeta Function
    """

    def __init__(self):
        super(Zeroes, self).__init__()
        self.question_no = 5
        self.ui = Ui_ZeroesScreen()
        self.ui.setupUi(self)
        self.setup_tabs()
        self.setup_question()
        self.ui.PrevButton.clicked.connect(self.goto_calculator)
        self.ui.NextButton.clicked.connect(self.goto_mainmenu)
        self.ui.CalculateButton.clicked.connect(self.goto_calculate_zeroes)
        self.show()


class CalculatorLeaderboard(InvestigationSection):

    """
    The CalculatorLeaderboard class is used to display how many zeta values
    been calculated by each user
    """

    def __init__(self):
        super(CalculatorLeaderboard, self).__init__()
        self.ui = Ui_CalculatorLeaderboardScreen()
        self.ui.setupUi(self)
        self.setup_tabs()
        self.get_rows()
        self.sort_rows()
        self.ui.PrevButton.clicked.connect(self.goto_table_calculator)
        self.ui.NextButton.clicked.connect(self.goto_zeroes)
        self.ui.ZetaTable.setRowCount(len(self.sorted_rows))
        for i, row in enumerate(self.sorted_rows):
            for j in range(len(row)):
                self.ui.ZetaTable.setItem(i,j, QTableWidgetItem(str(row[j])))
        self.ui.ZetaTable.horizontalHeader().setStretchLastSection(True)
        self.ui.ZetaTable.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        self.ui.ZetaTable.setColumnWidth(1, 100)
        self.show()

    def get_rows(self):
        self.rows = []
        self.usernames = [username[0] for username in database_select(['Username'], ['Users'])]
        for username in self.usernames:
            number_of_zeta_values_calculated = len(database_query(
                    'SELECT * FROM UserZeta WHERE Username=?', username))
            self.rows.append((username, number_of_zeta_values_calculated))

    def sort_rows(self):
        # sort rows by number of zeta values calculated
        self.sorted_numbers = binary_insertion_sort(
                set([row[-1] for row in self.rows]), descending=True)
        self.sorted_rows = []
        for _ in range(len(self.rows)):
            for row in self.rows:
                if row[-1] == self.sorted_numbers[0]:
                    self.sorted_rows.append(row)
                    self.rows.remove(row)
                    if self.sorted_numbers[0] not in [row[-1] for row in self.rows]:
                        del self.sorted_numbers[0]


class TableCalculator2(InvestigationSection):

    """
    The TableCalculator2 class is used to display the output values of the zeta
    function for a range of input values, that were entered by the user on the
    previous page

    The user then has the option to save these to the database or to a file
    """

    def __init__(self, table_values):
        super(TableCalculator2, self).__init__()
        self.table_values = table_values
        self.ui = Ui_TableCalculator2Screen()
        self.ui.setupUi(self)
        self.setup_tabs()
        self.ui.PrevButton.clicked.connect(self.goto_table_calculator)
        self.ui.NextButton.clicked.connect(self.goto_calculator_leaderboard)
        self.ui.DatabaseButton.clicked.connect(self.saveto_database)
        self.ui.FileButton.clicked.connect(self.saveto_file)
        self.ui.ZetaTable.setRowCount(len(self.table_values))
        for i, values in enumerate(self.table_values):
            for j in range(len(values)):
                self.ui.ZetaTable.setItem(i,j, QTableWidgetItem(str(values[j])))
        self.ui.ZetaTable.horizontalHeader().setStretchLastSection(True)
        self.ui.ZetaTable.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        self.ui.ZetaTable.setColumnWidth(1, 100)
        self.show()

    def saveto_database(self):
        if User.GetUsername():
            database_inputs = database_select(['Input_Real', 'Input_Imag'], ['Zeta'])
            for input, output in self.table_values:
                if (input.get_real(), input.get_imag()) not in database_inputs:
                    self.Zeta_ID = get_id('Zeta_ID', 'Zeta')
                    database_insert('Zeta', self.Zeta_ID, input.get_real(), input.get_imag(), output.get_real(), output.get_imag())
                    database_insert('UserZeta', self.Zeta_ID, User.GetUsername())
            self.ui.ErrorLabel.setText(self.center_text('Values saved to database'))
        else:
            self.ui.ErrorLabel.setText(self.center_text(f'You must be signed in to be able to '
                    'save to the database'))

    def saveto_file(self):
        FILEPATH = 'files/zeta_values.csv'
        save_zeta_values_to_file(self.table_values, FILEPATH)
        self.ui.ErrorLabel.setText(self.center_text(f'Table contents written to {FILEPATH}'))


class TableCalculator(InvestigationSection):

    """
    The TableCalculator class is used to display a calculator where
    the user is able to calculate the value of the zeta function for a range of
    input values of their choosing
    """

    def __init__(self):
        super(TableCalculator, self).__init__()
        self.ui = Ui_TableCalculatorScreen()
        self.ui.setupUi(self)
        self.setup_tabs()
        self.ui.PrevButton.clicked.connect(self.goto_single)
        self.ui.NextButton.clicked.connect(self.goto_calculator_leaderboard)
        self.ui.CalculateButton.clicked.connect(self.goto_table_calculator_2)
        self.show()

    def calculate_zeta(self):
        self.start_input = self.ui.StartInput.text()
        self.step_input = self.ui.StepInput.text()
        self.range_input = self.ui.NoOfValuesInput.text()
        self.start_complex = self.get_valid_complex_input(self.start_input)
        self.step_complex = self.get_valid_complex_input(self.step_input)
        self.range = make_int(self.range_input)
        if self.start_complex is not None and self.step_complex is not None:
            if 1 <= self.range <= 100:
                self.ui.ErrorLabel.setText('')
                self.input_values = [
                        self.start_complex + self.step_complex * i
                        for i in range(self.range)]
                try:
                    zetas = [zeta(value.get_real(), value.get_imag()) for value in self.input_values]
                except OverflowError:
                    self.ui.ErrorLabel.setText(self.center_text('Complex value \
                            is too large'))
                    self.table_values = False
                else:
                    self.output_values = [
                            Complex(round_to_3_sf(i.get_real()),
                            round_to_3_sf(i.get_imag())) for i in zetas]
                    self.table_values =  list(zip(
                        self.input_values, self.output_values))
            else:
                self.ui.ErrorLabel.setText(self.center_text('No. Of Values must be a positive \
                        integer between 1 and 100'))
                self.table_values = False
        else:
            self.ui.ErrorLabel.setText(self.center_text('Start Value and Step must be complex \
                    numbers of the form a+bi'))
            self.table_values = False


class SingleCalculator(InvestigationSection):

    """
    The SingleCalculator class is used to display a calculator where
    the user is able to calculate the value of the zeta function for a given
    input of their choosing

    The user then has the option to save this values to the database or to a file
    """

    def __init__(self):
        super(SingleCalculator, self).__init__()
        self.ui = Ui_SingleCalculatorScreen()
        self.ui.setupUi(self)
        self.setup_tabs()
        self.zeta_value = []
        self.valid_input = False
        self.ui.PrevButton.clicked.connect(self.goto_calculator)
        self.ui.NextButton.clicked.connect(self.goto_table_calculator)
        self.ui.CalculateButton.clicked.connect(self.calculate_zeta)
        self.ui.DatabaseButton.clicked.connect(self.saveto_database)
        self.ui.FileButton.clicked.connect(self.saveto_file)
        self.show()

    def calculate_zeta(self):
        self.zeta_user_input = str(self.ui.ZetaInput.text()).strip()
        self.zeta_input = self.get_valid_complex_input(self.zeta_user_input)
        if self.zeta_input is not None:
            if abs(self.zeta_input.get_real()) <= 50 and abs(self.zeta_input.get_imag()) <= 50:
                self.zeta_output = zeta(self.zeta_input.get_real(), self.zeta_input.get_imag())
                self.output_real = round_to_3_sf(self.zeta_output.get_real())
                self.output_imag = round_to_3_sf(self.zeta_output.get_imag())
                self.zeta_output_printable = Complex(self.output_real, self.output_imag)
                self.zeta_value = [(self.zeta_input, self.zeta_output_printable)]
                self.ui.ZetaOutput.setText(str(self.zeta_output_printable)[1:-1])
                self.ui.ErrorLabel.setText('')
            else:
                self.ui.ErrorLabel.setText(self.center_text('Real or imag part of input must be less than 50'))
                self.ui.ZetaOutput.setText('')
                self.zeta_input = None
        else:
            self.ui.ErrorLabel.setText(self.center_text('Input must be a complex number of the form a+bi'))
            self.ui.ZetaOutput.setText('')

    def saveto_database(self):
        self.calculate_zeta()
        if self.zeta_input is not None:
            if User.GetSignedIn():
                database_inputs = database_select(['Input_Real', 'Input_Imag'], ['Zeta'])
                self.zeta_input_real = self.zeta_input.get_real()
                self.zeta_input_imag = self.zeta_input.get_imag()
                self.zeta_output_real = self.zeta_output_printable.get_real()
                self.zeta_output_imag = self.zeta_output_printable.get_imag()
                if (self.zeta_input_real, self.zeta_input_imag) not in database_inputs:
                    self.Zeta_ID = get_id('Zeta_ID', 'Zeta')
                    database_insert('Zeta',
                            self.Zeta_ID,
                            self.zeta_input_real,
                            self.zeta_input_imag,
                            self.zeta_output_real,
                            self.zeta_output_imag)
                    database_insert('UserZeta', self.Zeta_ID, User.GetUsername())
                    self.ui.ErrorLabel.setText(self.center_text('Value saved to database'))
                else:
                    self.ui.ErrorLabel.setText(self.center_text('Value has already been recorded in the database'))
            else:
                self.ui.ErrorLabel.setText(
                        self.center_text('You must be signed in to be able to '
                        'save to the database'))
        else:
            self.ui.ErrorLabel.setText(
                    self.center_text('Input value is not valid'))

    def saveto_file(self):
        self.calculate_zeta()
        FILEPATH = 'files/zeta_values.csv'
        save_zeta_values_to_file(self.zeta_value, FILEPATH)
        self.ui.ErrorLabel.setText(self.center_text(f'Values written to {FILEPATH}'))


class Calculator(InvestigationSection):

    """
    The Calculator class is used to display the calculator screen where
    the user can choose to calculate the value of the zeta function for a single
    value or for a table of values
    """

    def __init__(self):
        super(Calculator, self).__init__()
        self.question_no = 7
        self.ui = Ui_CalculatorScreen()
        self.ui.setupUi(self)
        self.setup_tabs()
        self.setup_question()
        self.ui.PrevButton.clicked.connect(self.goto_primes)
        self.ui.NextButton.clicked.connect(self.goto_zeroes)
        self.ui.ZetaCalculatorButton.clicked.connect(self.goto_single)
        self.show()


class PrimeNumbers(InvestigationSection):

    """
    The PrimeNumbers class is used to display the prime numbers screen where
    the user is given information about the prime numbers and how they relate
    to the riemann zeta function
    """

    def __init__(self):
        super(PrimeNumbers, self).__init__()
        self.ui = Ui_PrimeNumbersScreen()
        self.ui.setupUi(self)
        self.setup_tabs()
        self.ui.PrevButton.clicked.connect(self.goto_graph_plots)
        self.ui.NextButton.clicked.connect(self.goto_calculator)
        self.show()


class ZetaApproximationMatPlot(DynamicGraphScreen):

    """
    The ZetaApproximation Mat Plot
    Demonstrates the convergent nature of the Riemann Zeta Function
    """

    def __init__(self, complex_input):
        super(ZetaApproximationMatPlot, self).__init__()
        self.complex_input = complex_input
        self.show()

    def update_figure(self):
        self.zeta_value = zeta(self.complex_input.get_real(), self.complex_input.get_imag(), self.count)
        self.x_vals.append(self.zeta_value.get_real())
        self.y_vals.append(self.zeta_value.get_imag())
        self.matplotlibwidget.axes.cla()
        self.matplotlibwidget.axes.plot(self.x_vals, self.y_vals, color='green')
        self.matplotlibwidget.canvas.draw()
        self.count += 1


class ZetaApproximation(InvestigationSection):

    """
    The ZetaApproximation class displays the zeta approximation screen where the
    user can enter a complex number and is shown a graph of how the algorithm used
    as the zeta function uses series which converge on a single point
    """

    def __init__(self):
        super(ZetaApproximation, self).__init__()
        self.ui = Ui_ZetaApproximationScreen()
        self.ui.setupUi(self)
        self.setup_tabs()
        self.ui.PrevButton.clicked.connect(self.goto_prime)
        self.ui.NextButton.clicked.connect(self.goto_primes)
        self.ui.GraphButton.clicked.connect(self.get_complex_input)
        self.show()

    def get_complex_input(self):
        self.graph_user_input = str(self.ui.GraphInput.text()).strip()
        self.graph_input = self.get_valid_complex_input(self.graph_user_input)
        if self.graph_input is None:
            self.ui.ErrorLabel.setText(self.center_text('Input must be a complex number of the form a+bi'))
        elif abs(self.graph_input.get_real()) > 30 or abs(self.graph_input.get_imag()) > 30:
            self.ui.ErrorLabel.setText(self.center_text('Input is too large, real and imag parts must be between -30 and 30'))
        elif self.graph_input == Complex(1, 0):
            self.ui.ErrorLabel.setText(self.center_text('Input cannot be equal to 1'))
        else:
            self.ui.ErrorLabel.setText(self.center_text(''))
            self.zeta_approximation_graph = ZetaApproximationMatPlot(self.graph_input)


class PrimeCountingFunctionMatPlot(DynamicGraphScreen):

    """
    The PrimeCountingFunction class is used to display a graph of the
    prime coutning function, the prime power function, the logarithmic integral
    function and (x/log x) as an approximation for the prime counting function
    """

    def __init__(self):
        super(PrimeCountingFunctionMatPlot, self).__init__()
        self.y_vals_pcf = []
        self.y_vals_x_logx= []
        self.y_vals_li = []
        self.y_vals_ppf = []
        self.count = 2
        self.show()

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
        self.matplotlibwidget.canvas.draw()
        self.count += 1


class PrimeCountingFunction(InvestigationSection):

    """
    The PrimeCountingFunction class is used to display the prime counting function
    screen
    """

    def __init__(self):
        super(PrimeCountingFunction, self).__init__()
        self.ui = Ui_PrimeCountingFunctionScreen()
        self.ui.setupUi(self)
        self.setup_tabs()
        self.ui.PrevButton.clicked.connect(self.goto_zeta_zeroes_plot)
        self.ui.NextButton.clicked.connect(self.goto_graph_plots)
        self.ui.GraphButton.clicked.connect(self.goto_pcf_graph)
        self.show()


class ZetaZeroesMatPlot(DynamicGraphScreen):

    """
    The ZetaZeroesMatPlot class is used to display a graph of the zeroes of the
    riemann zeta function
    """

    def __init__(self):
        super(ZetaZeroesMatPlot, self).__init__()
        self.show()

    def update_figure(self):
        self.accuracy = self.count//500 + 100
        if is_zeta_zero(1/2, self.count/self.accuracy):
            self.x_vals.append(1/2)
            self.y_vals.append(self.count/self.accuracy)
        self.matplotlibwidget.axes.cla()

        self.matplotlibwidget.axes.scatter(self.x_vals, self.y_vals)
        self.matplotlibwidget.axes.set_ylim(0)
        self.matplotlibwidget.axes.set_xlim(0, 1)
        self.matplotlibwidget.canvas.draw()
        self.count += 1


class ZetaZeroesPlot(InvestigationSection):

    """
    The ZetaZeroes class is used to display the Zeroes screen in the investigation
    section

    This is where the user is able to read about what the zeta zeroes are, and
    be able to display a graph of the zeta zeroes
    """

    def __init__(self):
        super(ZetaZeroesPlot, self).__init__()
        self.question_no=6
        self.ui = Ui_ZetaZeroesPlotScreen()
        self.ui.setupUi(self)
        self.setup_tabs()
        self.setup_question()
        self.ui.PrevButton.clicked.connect(self.goto_polar)
        self.ui.NextButton.clicked.connect(self.goto_prime)
        self.ui.GraphButton.clicked.connect(self.goto_zeta_zeroes_graph)
        self.show()



class PolarGraphMatPlot(DynamicGraphScreen):

    """
    The PolarGraphMatPlot class is used to display the polar graph of the riemann
    zeta function
    """

    def __init__(self, real_input):
        super(PolarGraphMatPlot, self).__init__()
        self.real_input = real_input
        self.show()

    def update_figure(self):
        new_zeta = zeta(self.real_input, self.count/25)
        self.x_vals.append(new_zeta.get_real())
        self.y_vals.append(new_zeta.get_imag())
        self.matplotlibwidget.axes.cla()
        self.matplotlibwidget.axes.plot(self.x_vals, self.y_vals, 'r')
        self.matplotlibwidget.canvas.draw()
        self.count += 1


class PolarGraph(InvestigationSection):

    """
    The PolarGraph class is used to display the Polar Graph Screen

    This is where the user is able to read about polar graphs, and be able to
    display a polar graph of the riemann zeta function
    """

    def __init__(self):
        super(PolarGraph, self).__init__()
        self.ui = Ui_PolarGraphScreen()
        self.ui.setupUi(self)
        self.setup_tabs()
        self.ui.PrevButton.clicked.connect(self.goto_graph_plots)
        self.ui.NextButton.clicked.connect(self.goto_zeta_zeroes_plot)
        self.ui.GraphButton.clicked.connect(self.polar_graph)
        self.show()

    def polar_graph(self):
        self.real_input = self.ui.GraphInput.text()
        try:
            self.real_input = float(self.real_input)
        except ValueError:
            self.ui.ErrorLabel.setText(self.center_text("Error: Input must be whole number or a decimal"))
        else:
            if self.real_input == 1:
                self.ui.ErrorLabel.setText(self.center_text("Error: Input must not be equal to 1"))
            elif not -10 <= self.real_input <= 45:
                self.ui.ErrorLabel.setText(self.center_text("Error: Input value must be between -10 and 45"))
            else:
                self.ui.ErrorLabel.setText('')
                self.graph = PolarGraphMatPlot(self.real_input)


class GraphPlot(InvestigationSection):

    """
    This class is used to display the Graph Plots screen in the investigation section

    This is the first screen that the user will see in the investigation section
    and will allow them to display many different types of graphs
    """

    def __init__(self):
        super(GraphPlot, self).__init__()
        self.ui = Ui_GraphPlotsScreen()
        self.ui.setupUi(self)
        self.setup_tabs()
        self.ui.GraphPlotsButton.clicked.connect(self.goto_polar)
        self.ui.PrevButton.clicked.connect(self.goto_mainmenu)
        self.ui.NextButton.clicked.connect(self.goto_primes)
        self.show()
