# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/investigation_screens/zeta_zeroes_plot_mat_plot.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ZetaZeroesMatPlotScreen(object):
    def setupUi(self, ZetaZeroesMatPlotScreen):
        ZetaZeroesMatPlotScreen.setObjectName("ZetaZeroesMatPlotScreen")
        ZetaZeroesMatPlotScreen.resize(1340, 720)
        ZetaZeroesMatPlotScreen.setSizeGripEnabled(False)

        self.retranslateUi(ZetaZeroesMatPlotScreen)
        QtCore.QMetaObject.connectSlotsByName(ZetaZeroesMatPlotScreen)

    def retranslateUi(self, ZetaZeroesMatPlotScreen):
        _translate = QtCore.QCoreApplication.translate
        ZetaZeroesMatPlotScreen.setWindowTitle(_translate("ZetaZeroesMatPlotScreen", "Visualising the Riemann Hypothesis - Zeta Zeroes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ZetaZeroesMatPlotScreen = QtWidgets.QDialog()
    ui = Ui_ZetaZeroesMatPlotScreen()
    ui.setupUi(ZetaZeroesMatPlotScreen)
    ZetaZeroesMatPlotScreen.show()
    sys.exit(app.exec_())
