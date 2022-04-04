"""
introduction_notes.py
=====================
A GUI for the introduction notes page of the notes section
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IntroductionNotesScreen(object):

    def setupUi(self, IntroductionNotesScreen):
        IntroductionNotesScreen.setObjectName("IntroductionNotesScreen")
        IntroductionNotesScreen.resize(1340, 723)
        IntroductionNotesScreen.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(IntroductionNotesScreen)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1340, 720))
        self.widget.setStyleSheet("background-color: rgb(69, 69, 69);")
        self.widget.setObjectName("widget")
        self.Title = QtWidgets.QLabel(self.widget)
        self.Title.setGeometry(QtCore.QRect(605, 20, 131, 51))
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
        self.SummaryTab = QtWidgets.QPushButton(self.TabBar)
        self.SummaryTab.setGeometry(QtCore.QRect(640, 5, 200, 70))
        self.SummaryTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SummaryTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.SummaryTab.setObjectName("SummaryTab")
        self.IntroductionTab = QtWidgets.QPushButton(self.TabBar)
        self.IntroductionTab.setGeometry(QtCore.QRect(220, 5, 200, 70))
        self.IntroductionTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.IntroductionTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239);\n"
"font: 18pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"")
        self.IntroductionTab.setObjectName("IntroductionTab")
        self.InvestigationTab = QtWidgets.QPushButton(self.TabBar)
        self.InvestigationTab.setGeometry(QtCore.QRect(430, 5, 200, 70))
        self.InvestigationTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.InvestigationTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.InvestigationTab.setObjectName("InvestigationTab")
        self.MainWidget = QtWidgets.QWidget(self.widget)
        self.MainWidget.setGeometry(QtCore.QRect(10, 170, 1320, 540))
        self.MainWidget.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius: 20px;")
        self.MainWidget.setObjectName("MainWidget")
        self.BackButton = QtWidgets.QPushButton(self.MainWidget)
        self.BackButton.setGeometry(QtCore.QRect(10, 460, 200, 70))
        self.BackButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BackButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.BackButton.setObjectName("BackButton")
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
        self.SubTitleText.setGeometry(QtCore.QRect(40, 20, 231, 41))
        self.SubTitleText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.SubTitleText.setObjectName("SubTitleText")
        self.NotesText = QtWidgets.QTextEdit(self.MainWidget)
        self.NotesText.setGeometry(QtCore.QRect(50, 80, 1211, 371))
        self.NotesText.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.NotesText.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\";\n"
"border: 2px solid;\n"
"border-color:rgb(69, 69, 69);\n"
"border-radius: 0px;")
        self.NotesText.setReadOnly(False)
        self.NotesText.setObjectName("NotesText")
        self.SaveButton = QtWidgets.QPushButton(self.MainWidget)
        self.SaveButton.setGeometry(QtCore.QRect(470, 460, 200, 70))
        self.SaveButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SaveButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.SaveButton.setObjectName("SaveButton")
        self.SavedText = QtWidgets.QLabel(self.MainWidget)
        self.SavedText.setGeometry(QtCore.QRect(690, 465, 191, 61))
        self.SavedText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;\n"
"border-radius: 0px")
        self.SavedText.setObjectName("SavedText")

        self.retranslateUi(IntroductionNotesScreen)
        QtCore.QMetaObject.connectSlotsByName(IntroductionNotesScreen)

    def retranslateUi(self, IntroductionNotesScreen):
        _translate = QtCore.QCoreApplication.translate
        IntroductionNotesScreen.setWindowTitle(_translate("IntroductionNotesScreen", "Visualising the Riemann Hypothesis - Notes"))
        self.Title.setText(_translate("IntroductionNotesScreen", "Notes"))
        self.TutorialTab.setText(_translate("IntroductionNotesScreen", "Tutorial"))
        self.SummaryTab.setText(_translate("IntroductionNotesScreen", "Summary"))
        self.IntroductionTab.setText(_translate("IntroductionNotesScreen", "Introduction"))
        self.InvestigationTab.setText(_translate("IntroductionNotesScreen", "Investigation"))
        self.BackButton.setText(_translate("IntroductionNotesScreen", "Back"))
        self.NextButton.setText(_translate("IntroductionNotesScreen", "Next"))
        self.SubTitleText.setText(_translate("IntroductionNotesScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Introduction</span></p></body></html>"))
        self.NotesText.setHtml(_translate("IntroductionNotesScreen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.SaveButton.setText(_translate("IntroductionNotesScreen", "Save"))
        self.SavedText.setText(_translate("IntroductionNotesScreen", "<html><head/><body><p><br/></p></body></html>"))
