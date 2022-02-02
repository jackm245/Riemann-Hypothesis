from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MplWidget(QtWidgets.QDialog):
    """ A Matplotlib Widget """

    def __init__(self, parent=None):
        super(MplWidget, self).__init__(parent)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.axes = self.figure.add_subplot(111)
        self.layoutvertical = QtWidgets.QVBoxLayout(self)
        self.layoutvertical.setGeometry(QtCore.QRect(500, 500, 500,500))
        self.layoutvertical.addWidget(self.canvas)
