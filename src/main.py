import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from program import MainMenu


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = MainMenu()
    sys.exit(app.exec())