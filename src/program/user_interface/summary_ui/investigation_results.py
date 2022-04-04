"""
investigation_results.py
========================
A GUI for the investigation results page of the summary section
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InvestigationResultsScreen(object):
    def setupUi(self, InvestigationResultsScreen):
        InvestigationResultsScreen.setObjectName("InvestigationResultsScreen")
        InvestigationResultsScreen.resize(1340, 723)
        InvestigationResultsScreen.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(InvestigationResultsScreen)
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
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
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
"background-color: rgb(239, 239, 239);\n"
"font: 18pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
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
        self.SubTitleText.setGeometry(QtCore.QRect(40, 20, 361, 51))
        self.SubTitleText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.SubTitleText.setObjectName("SubTitleText")
        self.MainText = QtWidgets.QLabel(self.MainWidget)
        self.MainText.setGeometry(QtCore.QRect(40, 90, 711, 341))
        self.MainText.setStyleSheet("font: 13pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.MainText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.MainText.setWordWrap(True)
        self.MainText.setObjectName("MainText")
        self.ZetaTable = QtWidgets.QTableWidget(self.MainWidget)
        self.ZetaTable.setGeometry(QtCore.QRect(900, 70, 300, 351))
        self.ZetaTable.setObjectName("ZetaTable")
        self.ZetaTable.setColumnCount(2)
        self.ZetaTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ZetaTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ZetaTable.setHorizontalHeaderItem(1, item)
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

        self.retranslateUi(InvestigationResultsScreen)
        QtCore.QMetaObject.connectSlotsByName(InvestigationResultsScreen)

    def retranslateUi(self, InvestigationResultsScreen):
        _translate = QtCore.QCoreApplication.translate
        InvestigationResultsScreen.setWindowTitle(_translate("InvestigationResultsScreen", "Visualising the Riemann Hypothesis - Summary"))
        self.Title.setText(_translate("InvestigationResultsScreen", "Summary"))
        self.SummaryTab.setText(_translate("InvestigationResultsScreen", "Summary"))
        self.TheoryRecapTab.setText(_translate("InvestigationResultsScreen", "Theory Recap"))
        self.InvestigationResultsLabel.setText(_translate("InvestigationResultsScreen", "<html><head/><body><p align=\"center\">Investigation<br/>Results</p></body></html>"))
        self.ConclusionLabel.setText(_translate("InvestigationResultsScreen", "<html><head/><body><p align=\"center\">Conclusion & <br/>Evaluation</p></body></html>"))
        self.ImpactLabel.setText(_translate("InvestigationResultsScreen", "<html><head/><body><p align=\"center\">Impact of the <br/>Riemann Hypothesis</p></body></html>"))
        self.PrevButton.setText(_translate("InvestigationResultsScreen", "Prev"))
        self.NextButton.setText(_translate("InvestigationResultsScreen", "Next"))
        self.SubTitleText.setText(_translate("InvestigationResultsScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Investigation Results</span></p></body></html>"))
        self.MainText.setText(_translate("InvestigationResultsScreen", "<html><head/><body><p>Hopefully, throuhout this program you have been able to gather and record results from investigating the Riemann Hypothesis.</p><p>You should notice, that the zeroes of the Riemann Zeta function occur only when the real part of the input is 1 half. </p><p>Furthermore, you sghould have noticed the connection between the prime power function and the prime counting function, and how these are able to be approximated using other functions.</p><p>See the table to the right to look at various values of the Zeta Function that have been calculated by users of this program.</p></body></html>"))
        item = self.ZetaTable.horizontalHeaderItem(0)
        item.setText(_translate("InvestigationResultsScreen", "Input (s)"))
        item = self.ZetaTable.horizontalHeaderItem(1)
        item.setText(_translate("InvestigationResultsScreen", "Output ζ(s)"))
        self.NotesButton.setText(_translate("InvestigationResultsScreen", "Notes"))
