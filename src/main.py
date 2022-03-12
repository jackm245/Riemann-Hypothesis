import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from program import MainMenu


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = MainMenu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
