"""
summary.py
==========
A GUI for the summary page of the summary section
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SummaryScreen(object):

    def setupUi(self, SummaryScreen):
        SummaryScreen.setObjectName("SummaryScreen")
        SummaryScreen.resize(1340, 723)
        SummaryScreen.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(SummaryScreen)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1340, 720))
        self.widget.setStyleSheet("background-color: rgb(69, 69, 69);")
        self.widget.setObjectName("widget")
        self.Title = QtWidgets.QLabel(self.widget)
        self.Title.setGeometry(QtCore.QRect(565, 20, 211, 51))
        self.Title.setStyleSheet("font: 36pt \"Sans Serif\"; color:rgb(239, 239, 239)")
        self.Title.setObjectName("Title")
        self.TabBar = QtWidgets.QWidget(self.widget)
        self.TabBar.setGeometry(QtCore.QRect(0, 80, 1340, 80))
        self.TabBar.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.TabBar.setObjectName("TabBar")
        self.SummaryTab = QtWidgets.QPushButton(self.TabBar)
        self.SummaryTab.setGeometry(QtCore.QRect(10, 5, 200, 70))
        self.SummaryTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SummaryTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239);\n"
"font: 18pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"")
        self.SummaryTab.setObjectName("SummaryTab")
        self.TheoryRecapTab = QtWidgets.QPushButton(self.TabBar)
        self.TheoryRecapTab.setGeometry(QtCore.QRect(220, 5, 200, 70))
        self.TheoryRecapTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TheoryRecapTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.TheoryRecapTab.setObjectName("TheoryRecapTab")
        self.InvestigationResultsLabel = QtWidgets.QLabel(self.TabBar)
        self.InvestigationResultsLabel.setGeometry(QtCore.QRect(430, 5, 200, 70))
        self.InvestigationResultsLabel.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.InvestigationResultsLabel.setObjectName("InvestigationResultsLabel")
        self.InvestigationResultsTab = QtWidgets.QPushButton(self.TabBar)
        self.InvestigationResultsTab.setGeometry(QtCore.QRect(430, 5, 200, 70))
        self.InvestigationResultsTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.InvestigationResultsTab.setStyleSheet("border-radius: 20px;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font: 18pt \"Sans Serif\";\n"
"")
        self.InvestigationResultsTab.setText("")
        self.InvestigationResultsTab.setObjectName("InvestigationResultsTab")
        self.ConclusionLabel = QtWidgets.QLabel(self.TabBar)
        self.ConclusionLabel.setGeometry(QtCore.QRect(640, 5, 200, 70))
        self.ConclusionLabel.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.ConclusionLabel.setObjectName("ConclusionLabel")
        self.ImpactLabel = QtWidgets.QLabel(self.TabBar)
        self.ImpactLabel.setGeometry(QtCore.QRect(850, 5, 241, 70))
        self.ImpactLabel.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.ImpactLabel.setObjectName("ImpactLabel")
        self.ConclusionTab = QtWidgets.QPushButton(self.TabBar)
        self.ConclusionTab.setGeometry(QtCore.QRect(640, 5, 200, 70))
        self.ConclusionTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ConclusionTab.setStyleSheet("border-radius: 20px;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font: 18pt \"Sans Serif\";\n"
"")
        self.ConclusionTab.setText("")
        self.ConclusionTab.setObjectName("ConclusionTab")
        self.ImpactTab = QtWidgets.QPushButton(self.TabBar)
        self.ImpactTab.setGeometry(QtCore.QRect(850, 5, 241, 70))
        self.ImpactTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ImpactTab.setStyleSheet("border-radius: 20px;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font: 18pt \"Sans Serif\";\n"
"")
        self.ImpactTab.setText("")
        self.ImpactTab.setObjectName("ImpactTab")
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
        self.SubTitleText.setGeometry(QtCore.QRect(40, 20, 171, 51))
        self.SubTitleText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.SubTitleText.setObjectName("SubTitleText")
        self.MainText = QtWidgets.QLabel(self.MainWidget)
        self.MainText.setGeometry(QtCore.QRect(40, 80, 1251, 141))
        self.MainText.setStyleSheet("font: 13pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.MainText.setWordWrap(True)
        self.MainText.setObjectName("MainText")
        self.NotesButton = QtWidgets.QPushButton(self.MainWidget)
        self.NotesButton.setGeometry(QtCore.QRect(570, 460, 200, 70))
        self.NotesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NotesButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.NotesButton.setObjectName("NotesButton")
        self.QuestionText = QtWidgets.QLabel(self.MainWidget)
        self.QuestionText.setGeometry(QtCore.QRect(420, 210, 501, 101))
        self.QuestionText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.QuestionText.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.QuestionText.setWordWrap(True)
        self.QuestionText.setObjectName("QuestionText")
        self.QuestionInput = QtWidgets.QLineEdit(self.MainWidget)
        self.QuestionInput.setGeometry(QtCore.QRect(410, 330, 230, 60))
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
        self.SubmitButton.setGeometry(QtCore.QRect(700, 330, 121, 61))
        self.SubmitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SubmitButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.SubmitButton.setObjectName("SubmitButton")
        self.MessageLabel = QtWidgets.QLabel(self.MainWidget)
        self.MessageLabel.setGeometry(QtCore.QRect(410, 400, 530, 41))
        self.MessageLabel.setStyleSheet("color: rgb(0, 140, 0);\n"
"font: 18pt \"Sans Serif\";")
        self.MessageLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.MessageLabel.setObjectName("MessageLabel")

        self.retranslateUi(SummaryScreen)
        QtCore.QMetaObject.connectSlotsByName(SummaryScreen)

    def retranslateUi(self, SummaryScreen):
        _translate = QtCore.QCoreApplication.translate
        SummaryScreen.setWindowTitle(_translate("SummaryScreen", "Visualising the Riemann Hypothesis - Summary"))
        self.Title.setText(_translate("SummaryScreen", "Summary"))
        self.SummaryTab.setText(_translate("SummaryScreen", "Summary"))
        self.TheoryRecapTab.setText(_translate("SummaryScreen", "Theory Recap"))
        self.InvestigationResultsLabel.setText(_translate("SummaryScreen", "<html><head/><body><p align=\"center\">Investigation<br/>Results</p></body></html>"))
        self.ConclusionLabel.setText(_translate("SummaryScreen", "<html><head/><body><p align=\"center\">Conclusion & <br/>Evaluation</p></body></html>"))
        self.ImpactLabel.setText(_translate("SummaryScreen", "<html><head/><body><p align=\"center\">Impact of the <br/>Riemann Hypothesis</p></body></html>"))
        self.PrevButton.setText(_translate("SummaryScreen", "Prev"))
        self.NextButton.setText(_translate("SummaryScreen", "Next"))
        self.SubTitleText.setText(_translate("SummaryScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Summary</span></p></body></html>"))
        self.MainText.setText(_translate("SummaryScreen", "<html><head/><body><p>The summary section is the final part of this program.</p><p><br/></p><p>Use this section to compare your results to the expected results, make any notes you need to, learn about the significance of the results that you have obtained, and answer the remaining questions.</p></body></html>"))
        self.NotesButton.setText(_translate("SummaryScreen", "Notes"))
        self.QuestionText.setText(_translate("SummaryScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Question</span></p></body></html>"))
        self.QuestionInput.setPlaceholderText(_translate("SummaryScreen", "Answer"))
        self.SubmitButton.setText(_translate("SummaryScreen", "Submit"))
        self.MessageLabel.setText(_translate("SummaryScreen", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
