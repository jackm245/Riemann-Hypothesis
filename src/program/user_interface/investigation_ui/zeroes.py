"""
zeroes.py
=========
A GUI for the zeroes page of the investigation section
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ZeroesScreen(object):

    def setupUi(self, ZeroesScreen):
        ZeroesScreen.setObjectName("ZeroesScreen")
        ZeroesScreen.resize(1340, 720)
        ZeroesScreen.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(ZeroesScreen)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1340, 720))
        self.widget.setStyleSheet("background-color: rgb(69, 69, 69);")
        self.widget.setObjectName("widget")
        self.Title = QtWidgets.QLabel(self.widget)
        self.Title.setGeometry(QtCore.QRect(530, 20, 291, 51))
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
"background-color: rgb(69, 69,69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
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
"background-color: rgb(239, 239, 239);\n"
"font: 18pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
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
        self.SubTitleText = QtWidgets.QLabel(self.MainWidget)
        self.SubTitleText.setGeometry(QtCore.QRect(40, 20, 901, 51))
        self.SubTitleText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.SubTitleText.setObjectName("SubTitleText")
        self.MainText = QtWidgets.QLabel(self.MainWidget)
        self.MainText.setGeometry(QtCore.QRect(30, 70, 1251, 211))
        self.MainText.setStyleSheet("font: 13pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.MainText.setWordWrap(True)
        self.MainText.setObjectName("MainText")
        self.CalculateButton = QtWidgets.QPushButton(self.MainWidget)
        self.CalculateButton.setGeometry(QtCore.QRect(440, 460, 200, 70))
        self.CalculateButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CalculateButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.CalculateButton.setObjectName("CalculateButton")
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
        self.QuestionText = QtWidgets.QLabel(self.MainWidget)
        self.QuestionText.setGeometry(QtCore.QRect(420, 270, 501, 71))
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
        self.MainText.raise_()
        self.CalculateButton.raise_()
        self.NotesButton.raise_()
        self.QuestionText.raise_()
        self.QuestionInput.raise_()
        self.MessageLabel.raise_()
        self.SubTitleText.raise_()
        self.SubmitButton.raise_()

        self.retranslateUi(ZeroesScreen)
        QtCore.QMetaObject.connectSlotsByName(ZeroesScreen)

    def retranslateUi(self, ZeroesScreen):
        _translate = QtCore.QCoreApplication.translate
        ZeroesScreen.setWindowTitle(_translate("ZeroesScreen", "Visualising the Riemann Hypothesis - Investigation"))
        self.Title.setText(_translate("ZeroesScreen", "Investigation"))
        self.GraphsTab.setText(_translate("ZeroesScreen", "Graphs"))
        self.PrimesTab.setText(_translate("ZeroesScreen", "Primes"))
        self.CalculatorTab.setText(_translate("ZeroesScreen", "Calculator"))
        self.ZeroesTab.setText(_translate("ZeroesScreen", "Zeroes"))
        self.PrevButton.setText(_translate("ZeroesScreen", "Prev"))
        self.NextButton.setText(_translate("ZeroesScreen", "Next"))
        self.SubTitleText.setText(_translate("ZeroesScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Calculating the Zeroes of the Riemann Zeta Function</span></p></body></html>"))
        self.MainText.setText(_translate("ZeroesScreen", "<html><head/><body><p>The zeroes of the Riemann Zeta Function is where the mystery of the Riemann Hypothesis lies.</p><p>A zero, also called a root, of the function f(x) is the x value such that f(x) = 0. For the zeta function, these roots are in two categories, trival, and non-trivial zeroes. The trivial zeroes, are much simply to understand. These occur when the input to the zeta function, is a negative even integer. There is solid proof for this. However, the non-trivial zeroes are mcuh more complex. The Riemann Hypothesis states that these non-trivial zeroes occur when the real part of the input to the zeta function is equal to 1/2. Although it has been proven that the zeroes must occur when the real part of the input is between 0 and 1, it is no more specific than that. Although all non-trivial zeroes every calculated have had real part 1/2.</p><p>There is no proof for why the non-trivial zeroes occur at 1/2, but we can try to calculate the non-trivial zeroes by setting the real part of our input to the zeta function to be 1/2, and varying the imaginary part. Click Calculate Zeroes to try and find the values of some of the non-trivial zeroes of the zeta function.</p></body></html>"))
        self.CalculateButton.setText(_translate("ZeroesScreen", "Calculate Zeroes"))
        self.NotesButton.setText(_translate("ZeroesScreen", "Notes"))
        self.QuestionText.setText(_translate("ZeroesScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Question</span></p></body></html>"))
        self.QuestionInput.setPlaceholderText(_translate("ZeroesScreen", "Answer"))
        self.SubmitButton.setText(_translate("ZeroesScreen", "Submit"))
        self.MessageLabel.setText(_translate("ZeroesScreen", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
