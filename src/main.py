"""
main.py
=======

This is the file from which the entire program is run
Includes the entry point into the program
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from program import MainMenu, create_database


def main():
    """ The main entry point to the program """
    app = QtWidgets.QApplication(sys.argv)
    create_database()
    try:
        application = MainMenu()
    except Error as e:
        print(f'Error: {e}\nRestarting Program')
        application = MainMenu()
    sys.exit(app.exec_())


if __name__ == '__main__':
        main()
