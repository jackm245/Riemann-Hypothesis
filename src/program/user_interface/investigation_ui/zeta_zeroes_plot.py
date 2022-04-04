"""
zeta_zeroes_plot.py
===================
A GUI for the zeta zeroes plot page of the investigation section
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ZetaZeroesPlotScreen(object):

    def setupUi(self, ZetaZeroesPlotScreen):
        ZetaZeroesPlotScreen.setObjectName("ZetaZeroesPlotScreen")
        ZetaZeroesPlotScreen.resize(1340, 722)
        ZetaZeroesPlotScreen.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(ZetaZeroesPlotScreen)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1340, 720))
        self.widget.setStyleSheet("background-color: rgb(69, 69, 69);")
        self.widget.setObjectName("widget")
        self.Title = QtWidgets.QLabel(self.widget)
        self.Title.setGeometry(QtCore.QRect(550, 20, 271, 51))
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
"background-color: rgb(239, 239, 239);\n"
"font: 18pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
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
        self.ZetaApproximationTab = QtWidgets.QPushButton(self.TabBar)
        self.ZetaApproximationTab.setGeometry(QtCore.QRect(640, 5, 200, 70))
        self.ZetaApproximationTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ZetaApproximationTab.setStyleSheet("border-radius: 20px;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font: 18pt \"Sans Serif\";\n"
"")
        self.ZetaApproximationTab.setText("")
        self.ZetaApproximationTab.setObjectName("ZetaApproximationTab")
        self.ZetaApproximationLabel = QtWidgets.QLabel(self.TabBar)
        self.ZetaApproximationLabel.setGeometry(QtCore.QRect(640, 5, 200, 70))
        self.ZetaApproximationLabel.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.ZetaApproximationLabel.setObjectName("ZetaApproximationLabel")
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
        self.GraphButton.setGeometry(QtCore.QRect(570, 460, 200, 70))
        self.GraphButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GraphButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.GraphButton.setObjectName("GraphButton")
        self.SubTitleText = QtWidgets.QLabel(self.MainWidget)
        self.SubTitleText.setGeometry(QtCore.QRect(40, 20, 681, 41))
        self.SubTitleText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.SubTitleText.setObjectName("SubTitleText")
        self.MainText = QtWidgets.QLabel(self.MainWidget)
        self.MainText.setGeometry(QtCore.QRect(40, 80, 1251, 141))
        self.MainText.setStyleSheet("font: 13pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.MainText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.MainText.setWordWrap(True)
        self.MainText.setObjectName("MainText")
        self.ZeroesTab = QtWidgets.QPushButton(self.MainWidget)
        self.ZeroesTab.setGeometry(QtCore.QRect(640, 70, 171, 51))
        self.ZeroesTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ZeroesTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 12pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.ZeroesTab.setObjectName("ZeroesTab")
        self.QuestionText = QtWidgets.QLabel(self.MainWidget)
        self.QuestionText.setGeometry(QtCore.QRect(420, 230, 501, 101))
        self.QuestionText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.QuestionText.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.QuestionText.setWordWrap(True)
        self.QuestionText.setObjectName("QuestionText")
        self.QuestionInput = QtWidgets.QLineEdit(self.MainWidget)
        self.QuestionInput.setGeometry(QtCore.QRect(390, 350, 230, 60))
        self.QuestionInput.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\";\n"
"border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);")
        self.QuestionInput.setText("")
        self.QuestionInput.setCursorPosition(0)
        self.QuestionInput.setAlignment(QtCore.Qt.AlignCenter)
        self.QuestionInput.setObjectName("QuestionInput")
        self.SubmitButton = QtWidgets.QPushButton(self.MainWidget)
        self.SubmitButton.setGeometry(QtCore.QRect(720, 350, 121, 61))
        self.SubmitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SubmitButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.SubmitButton.setObjectName("SubmitButton")
        self.MessageLabel = QtWidgets.QLabel(self.MainWidget)
        self.MessageLabel.setGeometry(QtCore.QRect(410, 410, 530, 41))
        self.MessageLabel.setStyleSheet("color: rgb(0, 140, 0);\n"
"font: 18pt \"Sans Serif\";")
        self.MessageLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.MessageLabel.setObjectName("MessageLabel")
        self.PrevButton.raise_()
        self.NextButton.raise_()
        self.GraphButton.raise_()
        self.SubTitleText.raise_()
        self.MainText.raise_()
        self.ZeroesTab.raise_()
        self.QuestionText.raise_()
        self.QuestionInput.raise_()
        self.MessageLabel.raise_()
        self.SubmitButton.raise_()

        self.retranslateUi(ZetaZeroesPlotScreen)
        QtCore.QMetaObject.connectSlotsByName(ZetaZeroesPlotScreen)

    def retranslateUi(self, ZetaZeroesPlotScreen):
        _translate = QtCore.QCoreApplication.translate
        ZetaZeroesPlotScreen.setWindowTitle(_translate("ZetaZeroesPlotScreen", "Visualising the Riemann Hypothesis - Investigation"))
        self.Title.setText(_translate("ZetaZeroesPlotScreen", "Graph Plots"))
        self.PolarTab.setText(_translate("ZetaZeroesPlotScreen", "Polar"))
        self.ZetaZeroesPlotTab.setText(_translate("ZetaZeroesPlotScreen", "Zeroes"))
        self.PrimeTab.setText(_translate("ZetaZeroesPlotScreen", "Prime"))
        self.ZetaApproximationLabel.setText(_translate("ZetaZeroesPlotScreen", "<html><head/><body><p align=\"center\">Zeta<br/>Approximation</p></body></html>"))
        self.PrevButton.setText(_translate("ZetaZeroesPlotScreen", "Prev"))
        self.NextButton.setText(_translate("ZetaZeroesPlotScreen", "Next"))
        self.GraphButton.setText(_translate("ZetaZeroesPlotScreen", "Graph"))
        self.SubTitleText.setText(_translate("ZetaZeroesPlotScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Zeroes of the Riemann Zeta Function</span></p></body></html>"))
        self.MainText.setText(_translate("ZetaZeroesPlotScreen", "<html><head/><body><p>As also mentioned in the zeroes calculator section of the investigation --&gt;<br/></p><p>The non-trivial zeroes of the riemann zeta function are input values between 0 and 1, for which the output of the function is zero.</p><p>This graph will aim to calculate each zeta zero, and then plot them on a graph; allowing you to see the distribution of the non-trivial zeta zeroes along the critical line.</p></body></html>"))
        self.ZeroesTab.setText(_translate("ZetaZeroesPlotScreen", "Zeroes Calculator"))
        self.QuestionText.setText(_translate("ZetaZeroesPlotScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Question</span></p></body></html>"))
        self.QuestionInput.setPlaceholderText(_translate("ZetaZeroesPlotScreen", "Answer"))
        self.SubmitButton.setText(_translate("ZetaZeroesPlotScreen", "Submit"))
        self.MessageLabel.setText(_translate("ZetaZeroesPlotScreen", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
