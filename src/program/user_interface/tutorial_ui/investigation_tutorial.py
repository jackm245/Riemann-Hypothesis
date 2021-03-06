"""
investigation_tutorial.py
=========================
A GUI for the investigation tutorial page of the tutorial section
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InvestigationTutorialScreen(object):

    def setupUi(self, InvestigationTutorialScreen):
        InvestigationTutorialScreen.setObjectName("InvestigationTutorialScreen")
        InvestigationTutorialScreen.resize(1340, 723)
        InvestigationTutorialScreen.setToolTipDuration(0)
        InvestigationTutorialScreen.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(InvestigationTutorialScreen)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1340, 720))
        self.widget.setStyleSheet("background-color: rgb(69, 69, 69);")
        self.widget.setObjectName("widget")
        self.Title = QtWidgets.QLabel(self.widget)
        self.Title.setGeometry(QtCore.QRect(590, 20, 161, 51))
        self.Title.setStyleSheet("font: 36pt \"Sans Serif\"; color:rgb(239, 239, 239)")
        self.Title.setObjectName("Title")
        self.TabBar = QtWidgets.QWidget(self.widget)
        self.TabBar.setGeometry(QtCore.QRect(0, 80, 1340, 80))
        self.TabBar.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.TabBar.setObjectName("TabBar")
        self.TutorialTab = QtWidgets.QPushButton(self.TabBar)
        self.TutorialTab.setGeometry(QtCore.QRect(10, 5, 200, 70))
        self.TutorialTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TutorialTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.TutorialTab.setObjectName("TutorialTab")
        self.LoginTab = QtWidgets.QPushButton(self.TabBar)
        self.LoginTab.setGeometry(QtCore.QRect(430, 5, 221, 70))
        self.LoginTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LoginTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.LoginTab.setObjectName("LoginTab")
        self.IntroductionTab = QtWidgets.QPushButton(self.TabBar)
        self.IntroductionTab.setGeometry(QtCore.QRect(660, 5, 200, 70))
        self.IntroductionTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.IntroductionTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.IntroductionTab.setObjectName("IntroductionTab")
        self.InvestigationTab = QtWidgets.QPushButton(self.TabBar)
        self.InvestigationTab.setGeometry(QtCore.QRect(870, 5, 200, 70))
        self.InvestigationTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.InvestigationTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239);\n"
"font: 18pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"")
        self.InvestigationTab.setObjectName("InvestigationTab")
        self.SummaryTab = QtWidgets.QPushButton(self.TabBar)
        self.SummaryTab.setGeometry(QtCore.QRect(1080, 5, 200, 70))
        self.SummaryTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SummaryTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.SummaryTab.setObjectName("SummaryTab")
        self.ProgramStructureTab = QtWidgets.QPushButton(self.TabBar)
        self.ProgramStructureTab.setGeometry(QtCore.QRect(220, 5, 200, 70))
        self.ProgramStructureTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ProgramStructureTab.setStyleSheet("border-radius: 20px;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font: 18pt \"Sans Serif\";\n"
"")
        self.ProgramStructureTab.setText("")
        self.ProgramStructureTab.setObjectName("ProgramStructureTab")
        self.ProgramStructureLabel = QtWidgets.QLabel(self.TabBar)
        self.ProgramStructureLabel.setGeometry(QtCore.QRect(220, 5, 200, 70))
        self.ProgramStructureLabel.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.ProgramStructureLabel.setObjectName("ProgramStructureLabel")
        self.TutorialTab.raise_()
        self.LoginTab.raise_()
        self.IntroductionTab.raise_()
        self.InvestigationTab.raise_()
        self.SummaryTab.raise_()
        self.ProgramStructureLabel.raise_()
        self.ProgramStructureTab.raise_()
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
        self.SubTitleText.setGeometry(QtCore.QRect(40, 20, 311, 51))
        self.SubTitleText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.SubTitleText.setObjectName("SubTitleText")
        self.MSlider = QtWidgets.QSlider(self.MainWidget)
        self.MSlider.setGeometry(QtCore.QRect(400, 250, 181, 31))
        self.MSlider.setMinimum(-10)
        self.MSlider.setMaximum(10)
        self.MSlider.setOrientation(QtCore.Qt.Horizontal)
        self.MSlider.setInvertedAppearance(False)
        self.MSlider.setInvertedControls(False)
        self.MSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.MSlider.setObjectName("MSlider")
        self.MainText = QtWidgets.QLabel(self.MainWidget)
        self.MainText.setGeometry(QtCore.QRect(40, 70, 1251, 111))
        self.MainText.setStyleSheet("font: 13pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.MainText.setWordWrap(True)
        self.MainText.setObjectName("MainText")
        self.GraphText = QtWidgets.QLabel(self.MainWidget)
        self.GraphText.setGeometry(QtCore.QRect(600, 170, 151, 61))
        self.GraphText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.GraphText.setObjectName("GraphText")
        self.CSlider = QtWidgets.QSlider(self.MainWidget)
        self.CSlider.setGeometry(QtCore.QRect(760, 250, 181, 31))
        self.CSlider.setMinimum(-10)
        self.CSlider.setMaximum(10)
        self.CSlider.setOrientation(QtCore.Qt.Horizontal)
        self.CSlider.setInvertedAppearance(False)
        self.CSlider.setInvertedControls(False)
        self.CSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.CSlider.setObjectName("CSlider")
        self.MText = QtWidgets.QLabel(self.MainWidget)
        self.MText.setGeometry(QtCore.QRect(330, 220, 61, 61))
        self.MText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.MText.setObjectName("MText")
        self.CText = QtWidgets.QLabel(self.MainWidget)
        self.CText.setGeometry(QtCore.QRect(690, 220, 61, 61))
        self.CText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.CText.setObjectName("CText")
        self.GraphButton = QtWidgets.QPushButton(self.MainWidget)
        self.GraphButton.setGeometry(QtCore.QRect(610, 280, 131, 51))
        self.GraphButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GraphButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.GraphButton.setObjectName("GraphButton")
        self.MainText_2 = QtWidgets.QLabel(self.MainWidget)
        self.MainText_2.setGeometry(QtCore.QRect(20, 350, 861, 31))
        self.MainText_2.setStyleSheet("font: 13pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.MainText_2.setWordWrap(True)
        self.MainText_2.setObjectName("MainText_2")
        self.QuestionInput = QtWidgets.QLineEdit(self.MainWidget)
        self.QuestionInput.setGeometry(QtCore.QRect(540, 420, 111, 60))
        self.QuestionInput.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\";\n"
"border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);")
        self.QuestionInput.setText("")
        self.QuestionInput.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.QuestionInput.setCursorPosition(0)
        self.QuestionInput.setAlignment(QtCore.Qt.AlignCenter)
        self.QuestionInput.setObjectName("QuestionInput")
        self.SubmitButton = QtWidgets.QPushButton(self.MainWidget)
        self.SubmitButton.setGeometry(QtCore.QRect(690, 420, 131, 60))
        self.SubmitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SubmitButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.SubmitButton.setObjectName("SubmitButton")
        self.MessageLabel = QtWidgets.QLabel(self.MainWidget)
        self.MessageLabel.setGeometry(QtCore.QRect(440, 480, 461, 41))
        self.MessageLabel.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 18pt \"Sans Serif\";")
        self.MessageLabel.setObjectName("MessageLabel")
        self.MDisplay = QtWidgets.QLabel(self.MainWidget)
        self.MDisplay.setGeometry(QtCore.QRect(430, 200, 120, 51))
        self.MDisplay.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239);\n"
"font: 18pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"")
        self.MDisplay.setObjectName("MDisplay")
        self.CDisplay = QtWidgets.QLabel(self.MainWidget)
        self.CDisplay.setGeometry(QtCore.QRect(790, 200, 120, 51))
        self.CDisplay.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239);\n"
"font: 18pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"")
        self.CDisplay.setObjectName("CDisplay")
        self.QuestionText = QtWidgets.QLabel(self.MainWidget)
        self.QuestionText.setGeometry(QtCore.QRect(590, 380, 161, 31))
        self.QuestionText.setStyleSheet("font: 13pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.QuestionText.setWordWrap(True)
        self.QuestionText.setObjectName("QuestionText")
        self.SubTitleText.raise_()
        self.PrevButton.raise_()
        self.NextButton.raise_()
        self.MSlider.raise_()
        self.MainText.raise_()
        self.GraphText.raise_()
        self.CSlider.raise_()
        self.MText.raise_()
        self.CText.raise_()
        self.GraphButton.raise_()
        self.MainText_2.raise_()
        self.QuestionInput.raise_()
        self.SubmitButton.raise_()
        self.MessageLabel.raise_()
        self.MDisplay.raise_()
        self.CDisplay.raise_()
        self.QuestionText.raise_()

        self.retranslateUi(InvestigationTutorialScreen)
        QtCore.QMetaObject.connectSlotsByName(InvestigationTutorialScreen)

    def retranslateUi(self, InvestigationTutorialScreen):
        _translate = QtCore.QCoreApplication.translate
        InvestigationTutorialScreen.setWindowTitle(_translate("InvestigationTutorialScreen", "Visualising the Riemann Hypothesis - Tutorial"))
        self.Title.setText(_translate("InvestigationTutorialScreen", "Tutorial"))
        self.TutorialTab.setText(_translate("InvestigationTutorialScreen", "Tutorial"))
        self.LoginTab.setText(_translate("InvestigationTutorialScreen", "Login"))
        self.IntroductionTab.setText(_translate("InvestigationTutorialScreen", "Introduction"))
        self.InvestigationTab.setText(_translate("InvestigationTutorialScreen", "Investigation"))
        self.SummaryTab.setText(_translate("InvestigationTutorialScreen", "Summary"))
        self.ProgramStructureLabel.setText(_translate("InvestigationTutorialScreen", "<html><head/><body><p align=\"center\">Program<br/>Structure</p></body></html>"))
        self.PrevButton.setText(_translate("InvestigationTutorialScreen", "Prev"))
        self.NextButton.setText(_translate("InvestigationTutorialScreen", "Next"))
        self.SubTitleText.setText(_translate("InvestigationTutorialScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Investigation</span></p></body></html>"))
        self.MainText.setText(_translate("InvestigationTutorialScreen", "<html><head/><body><p>The Investigation Section is the main part of this program. It will allow you to conduct your own investigation into the Riemann Hypothesis and let you record your results, while asking you questions along the way</p><p>Lets get some practice with how this program will work. Slide the slides to adjust the equation, then press graph to display the graph. Change these values to see what happens.</p></body></html>"))
        self.GraphText.setText(_translate("InvestigationTutorialScreen", "<html><head/><body><p><span style=\" font-weight:600;\">y=mx+c</span></p></body></html>"))
        self.MText.setText(_translate("InvestigationTutorialScreen", "<html><head/><body><p><span style=\" font-weight:600;\">M:</span></p></body></html>"))
        self.CText.setText(_translate("InvestigationTutorialScreen", "<html><head/><body><p><span style=\" font-weight:600;\">C:</span></p></body></html>"))
        self.GraphButton.setText(_translate("InvestigationTutorialScreen", "Graph"))
        self.MainText_2.setText(_translate("InvestigationTutorialScreen", "<html><head/><body><p>There will also be many opportunities to answer questions during this section. Have a go at the one below!</p></body></html>"))
        self.QuestionInput.setPlaceholderText(_translate("InvestigationTutorialScreen", "Answer"))
        self.SubmitButton.setText(_translate("InvestigationTutorialScreen", "Submit"))
        self.MessageLabel.setText(_translate("InvestigationTutorialScreen", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.MDisplay.setText(_translate("InvestigationTutorialScreen", "<html><head/><body><p align=\"center\">0</p></body></html>"))
        self.CDisplay.setText(_translate("InvestigationTutorialScreen", "<html><head/><body><p align=\"center\">0</p></body></html>"))
        self.QuestionText.setText(_translate("InvestigationTutorialScreen", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Question</span></p></body></html>"))
