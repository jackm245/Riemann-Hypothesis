"""
graph_plots.py
==============
A GUI for the graph plots page of the investigation section
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GraphPlotsScreen(object):

    def setupUi(self, GraphPlotsScreen):
        GraphPlotsScreen.setObjectName("GraphPlotsScreen")
        GraphPlotsScreen.resize(1340, 720)
        GraphPlotsScreen.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(GraphPlotsScreen)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1340, 720))
        self.widget.setStyleSheet("background-color: rgb(69, 69, 69);")
        self.widget.setObjectName("widget")
        self.Title = QtWidgets.QLabel(self.widget)
        self.Title.setGeometry(QtCore.QRect(540, 20, 271, 51))
        self.Title.setStyleSheet("font: 36pt \"Sans Serif\"; color:rgb(239, 239, 239)")
        self.Title.setObjectName("Title")
        self.TabBar = QtWidgets.QWidget(self.widget)
        self.TabBar.setGeometry(QtCore.QRect(0, 80, 1340, 80))
        self.TabBar.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.TabBar.setObjectName("TabBar")
        self.GraphsTab = QtWidgets.QPushButton(self.TabBar)
        self.GraphsTab.setGeometry(QtCore.QRect(10, 5, 200, 70))
        self.GraphsTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GraphsTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239);\n"
"font: 18pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"")
        self.GraphsTab.setObjectName("GraphsTab")
        self.PrimesTab = QtWidgets.QPushButton(self.TabBar)
        self.PrimesTab.setGeometry(QtCore.QRect(220, 5, 200, 70))
        self.PrimesTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PrimesTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.PrimesTab.setObjectName("PrimesTab")
        self.CalculatorTab = QtWidgets.QPushButton(self.TabBar)
        self.CalculatorTab.setGeometry(QtCore.QRect(430, 5, 200, 70))
        self.CalculatorTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CalculatorTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.CalculatorTab.setObjectName("CalculatorTab")
        self.ZeroesTab = QtWidgets.QPushButton(self.TabBar)
        self.ZeroesTab.setGeometry(QtCore.QRect(640, 5, 200, 70))
        self.ZeroesTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ZeroesTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.ZeroesTab.setObjectName("ZeroesTab")
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
        self.GraphPlotsButton = QtWidgets.QPushButton(self.MainWidget)
        self.GraphPlotsButton.setGeometry(QtCore.QRect(440, 460, 200, 70))
        self.GraphPlotsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GraphPlotsButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.GraphPlotsButton.setObjectName("GraphPlotsButton")
        self.SubTitleText = QtWidgets.QLabel(self.MainWidget)
        self.SubTitleText.setGeometry(QtCore.QRect(40, 20, 681, 51))
        self.SubTitleText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.SubTitleText.setObjectName("SubTitleText")
        self.MainText = QtWidgets.QLabel(self.MainWidget)
        self.MainText.setGeometry(QtCore.QRect(40, 80, 1251, 341))
        self.MainText.setStyleSheet("font: 13pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.MainText.setWordWrap(True)
        self.MainText.setObjectName("MainText")
        self.ErrorLabel = QtWidgets.QLabel(self.MainWidget)
        self.ErrorLabel.setGeometry(QtCore.QRect(450, 410, 461, 41))
        self.ErrorLabel.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 12pt \"Sans Serif\";")
        self.ErrorLabel.setObjectName("ErrorLabel")
        self.NotesButton = QtWidgets.QPushButton(self.MainWidget)
        self.NotesButton.setGeometry(QtCore.QRect(700, 460, 200, 70))
        self.NotesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NotesButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.NotesButton.setObjectName("NotesButton")

        self.retranslateUi(GraphPlotsScreen)
        QtCore.QMetaObject.connectSlotsByName(GraphPlotsScreen)

    def retranslateUi(self, GraphPlotsScreen):
        _translate = QtCore.QCoreApplication.translate
        GraphPlotsScreen.setWindowTitle(_translate("GraphPlotsScreen", "Visualising the Riemann Hypothesis - Investigation"))
        self.Title.setText(_translate("GraphPlotsScreen", "Investigation"))
        self.GraphsTab.setText(_translate("GraphPlotsScreen", "Graphs"))
        self.PrimesTab.setText(_translate("GraphPlotsScreen", "Primes"))
        self.CalculatorTab.setText(_translate("GraphPlotsScreen", "Calculator"))
        self.ZeroesTab.setText(_translate("GraphPlotsScreen", "Zeroes"))
        self.PrevButton.setText(_translate("GraphPlotsScreen", "Prev"))
        self.NextButton.setText(_translate("GraphPlotsScreen", "Next"))
        self.GraphPlotsButton.setText(_translate("GraphPlotsScreen", "Graphs Plots"))
        self.SubTitleText.setText(_translate("GraphPlotsScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Visualising the Riemann Hypothesis</span></p></body></html>"))
        self.MainText.setText(_translate("GraphPlotsScreen", "<html><head/><body><p>As mentioned in the Investigation Section, there are numerous ways that the Riemann Hypothesiscan be visualised.</p><p>The main way of visualsing the Riemann Hypothesis is through the use of graphs, allowing for a visual representation of many different mathematical functions.</p><p>One of the most famous graphs of the Riemann Hypothesis is the polar graph of the Riemann Zeta Function, along the line Re(s) = 0.5. Polar Graphs allow for complex (2 dimensional) numbers to be represented visually. Unlike usual graphs where the x axis is the input to the function, and the y-axis is the output, the polar graph is only capable of displaying the output of the function, however, if the input domain is already defined and known, then this is not an issue<br/></p><p>Another graph used is the graph of the zeta zeroes. This graph plots complex numbers on an argand diagram, where these complex numbers are the roots, or zeroes of the Riemann Zeta Function. If that input is passed into the Riemann Zeta Function, and produces a result of 0, then that point is plotted onto the Graph.</p><p><br/></p><p>The last graph I am using to visualise the Riemann Hypothesis is the graph of the Prime Counting Function, and other functions that are used to approximate this. This allows you to visualsie Carl Gauss\' Prime Number Theorem, describing the distribution of prime numbers - A theorem that was proved using the Riemann Hypthesis</p><p><br/></p></body></html>"))
        self.ErrorLabel.setText(_translate("GraphPlotsScreen", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.NotesButton.setText(_translate("GraphPlotsScreen", "Notes"))
