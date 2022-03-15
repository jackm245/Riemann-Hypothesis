"""
main.py
=======

This is the file from which the entire program is run
Includes the entry point into the program
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from program import MainMenu


def main():
    """ The main entry point to the program """
    app = QtWidgets.QApplication(sys.argv)
    application = MainMenu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
