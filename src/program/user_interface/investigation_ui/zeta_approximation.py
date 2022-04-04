"""
zeta_approximation.py
=====================
A GUI for the zeta approximation page of the investigation section
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ZetaApproximationScreen(object):

    def setupUi(self, ZetaApproximationScreen):
        ZetaApproximationScreen.setObjectName("ZetaApproximationScreen")
        ZetaApproximationScreen.resize(1340, 720)
        ZetaApproximationScreen.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(ZetaApproximationScreen)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1340, 720))
        self.widget.setStyleSheet("background-color: rgb(69, 69, 69);")
        self.widget.setObjectName("widget")
        self.Title = QtWidgets.QLabel(self.widget)
        self.Title.setGeometry(QtCore.QRect(550, 20, 281, 51))
        self.Title.setStyleSheet("font: 36pt \"Sans Serif\"; color:rgb(239, 239, 239)")
        self.Title.setObjectName("Title")
        self.TabBar = QtWidgets.QWidget(self.widget)
        self.TabBar.setGeometry(QtCore.QRect(0, 80, 1340, 80))
        self.TabBar.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.TabBar.setObjectName("TabBar")
        self.PolarTab = QtWidgets.QPushButton(self.TabBar)
        self.PolarTab.setGeometry(QtCore.QRect(10, 5, 200, 70))
        self.PolarTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PolarTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.PolarTab.setObjectName("PolarTab")
        self.ZetaZeroesPlotTab = QtWidgets.QPushButton(self.TabBar)
        self.ZetaZeroesPlotTab.setGeometry(QtCore.QRect(220, 5, 200, 70))
        self.ZetaZeroesPlotTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ZetaZeroesPlotTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.ZetaZeroesPlotTab.setObjectName("ZetaZeroesPlotTab")
        self.PrimeTab = QtWidgets.QPushButton(self.TabBar)
        self.PrimeTab.setGeometry(QtCore.QRect(430, 5, 200, 70))
        self.PrimeTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PrimeTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.PrimeTab.setObjectName("PrimeTab")
        self.ZetaApproximationLabel = QtWidgets.QLabel(self.TabBar)
        self.ZetaApproximationLabel.setGeometry(QtCore.QRect(640, 5, 200, 70))
        self.ZetaApproximationLabel.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239);\n"
"font: 18pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"")
        self.ZetaApproximationLabel.setObjectName("ZetaApproximationLabel")
        self.ZetaApproximationTab = QtWidgets.QPushButton(self.TabBar)
        self.ZetaApproximationTab.setGeometry(QtCore.QRect(640, 5, 200, 70))
        self.ZetaApproximationTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ZetaApproximationTab.setStyleSheet("border-radius: 20px;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font: 18pt \"Sans Serif\";\n"
"")
        self.ZetaApproximationTab.setText("")
        self.ZetaApproximationTab.setObjectName("ZetaApproximationTab")
        self.MainWidget = QtWidgets.QWidget(self.widget)
        self.MainWidget.setGeometry(QtCore.QRect(10, 170, 1320, 540))
        self.MainWidget.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius: 20px;")
        self.MainWidget.setObjectName("MainWidget")
        self.PrevButton = QtWidgets.QPushButton(self.MainWidget)
        self.PrevButton.setGeometry(QtCore.QRect(10, 460, 200, 70))
        self.PrevButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PrevButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.PrevButton.setObjectName("PrevButton")
        self.NextButton = QtWidgets.QPushButton(self.MainWidget)
        self.NextButton.setGeometry(QtCore.QRect(1110, 460, 200, 70))
        self.NextButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NextButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.NextButton.setObjectName("NextButton")
        self.GraphButton = QtWidgets.QPushButton(self.MainWidget)
        self.GraphButton.setGeometry(QtCore.QRect(680, 460, 200, 70))
        self.GraphButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GraphButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.GraphButton.setObjectName("GraphButton")
        self.GraphInput = QtWidgets.QLineEdit(self.MainWidget)
        self.GraphInput.setGeometry(QtCore.QRect(460, 460, 200, 70))
        self.GraphInput.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\";\n"
"border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"text-align: center;")
        self.GraphInput.setText("")
        self.GraphInput.setCursorPosition(0)
        self.GraphInput.setAlignment(QtCore.Qt.AlignCenter)
        self.GraphInput.setObjectName("GraphInput")
        self.SubTitleText = QtWidgets.QLabel(self.MainWidget)
        self.SubTitleText.setGeometry(QtCore.QRect(40, 20, 821, 41))
        self.SubTitleText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.SubTitleText.setObjectName("SubTitleText")
        self.MainText = QtWidgets.QLabel(self.MainWidget)
        self.MainText.setGeometry(QtCore.QRect(50, 80, 1251, 201))
        self.MainText.setStyleSheet("font: 13pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.MainText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.MainText.setWordWrap(True)
        self.MainText.setObjectName("MainText")
        self.ErrorLabel = QtWidgets.QLabel(self.MainWidget)
        self.ErrorLabel.setGeometry(QtCore.QRect(310, 400, 721, 41))
        self.ErrorLabel.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 12pt \"Sans Serif\";")
        self.ErrorLabel.setObjectName("ErrorLabel")

        self.retranslateUi(ZetaApproximationScreen)
        QtCore.QMetaObject.connectSlotsByName(ZetaApproximationScreen)

    def retranslateUi(self, ZetaApproximationScreen):
        _translate = QtCore.QCoreApplication.translate
        ZetaApproximationScreen.setWindowTitle(_translate("ZetaApproximationScreen", "Visualising the Riemann Hypothesis - Investigation"))
        self.Title.setText(_translate("ZetaApproximationScreen", "Graph Plots"))
        self.PolarTab.setText(_translate("ZetaApproximationScreen", "Polar"))
        self.ZetaZeroesPlotTab.setText(_translate("ZetaApproximationScreen", "Zeroes"))
        self.PrimeTab.setText(_translate("ZetaApproximationScreen", "Prime"))
        self.ZetaApproximationLabel.setText(_translate("ZetaApproximationScreen", "<html><head/><body><p align=\"center\">Zeta<br/>Approximation</p></body></html>"))
        self.PrevButton.setText(_translate("ZetaApproximationScreen", "Prev"))
        self.NextButton.setText(_translate("ZetaApproximationScreen", "Next"))
        self.GraphButton.setText(_translate("ZetaApproximationScreen", "Graph"))
        self.GraphInput.setToolTip(_translate("ZetaApproximationScreen", "<html><head/><body><p align=\"center\"> Re(s)</body></html>"))
        self.GraphInput.setPlaceholderText(_translate("ZetaApproximationScreen", "Input"))
        self.SubTitleText.setText(_translate("ZetaApproximationScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Approximation of the Riemann Zeta Function</span></p></body></html>"))
        self.MainText.setText(_translate("ZetaApproximationScreen", "<html><head/><body><p>Due to the infinite and recursive nature of the zeta function, it would be impossbile to calculate any exact values for the zeta function using a computer program.</p><p><br/></p><p>The aim of this graph, is to demonstrate how the program uses sums with increasing amounts of accuracy to find values of the zeta function.</p><p><br/></p><p>Type any complex number into the box, and click graph!</p></body></html>"))
        self.ErrorLabel.setText(_translate("ZetaApproximationScreen", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
