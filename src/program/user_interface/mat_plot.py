"""
mat_plot.py
============
A GUI for every mat plot graph page
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MatPlotScreen(object):

    def setupUi(self, MatPlotScreen):
        MatPlotScreen.setObjectName("MatPlotScreen")
        MatPlotScreen.resize(1340, 720)
        MatPlotScreen.setSizeGripEnabled(False)

        self.retranslateUi(MatPlotScreen)
        QtCore.QMetaObject.connectSlotsByName(MatPlotScreen)

    def retranslateUi(self, MatPlotScreen):
        _translate = QtCore.QCoreApplication.translate
        MatPlotScreen.setWindowTitle(_translate("MatPlotScreen", "Visualising the Riemann Hypothesis - Zeta Zeroes"))
