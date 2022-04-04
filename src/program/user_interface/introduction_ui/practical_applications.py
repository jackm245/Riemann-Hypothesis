"""
practical_applications.py
=========================
A GUI for the practical applications page of the introduction section
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PracticalApplicationsScreen(object):

    def setupUi(self, PracticalApplicationsScreen):
        PracticalApplicationsScreen.setObjectName("PracticalApplicationsScreen")
        PracticalApplicationsScreen.resize(1340, 723)
        PracticalApplicationsScreen.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(PracticalApplicationsScreen)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1340, 720))
        self.widget.setStyleSheet("background-color: rgb(69, 69, 69);")
        self.widget.setObjectName("widget")
        self.Title = QtWidgets.QLabel(self.widget)
        self.Title.setGeometry(QtCore.QRect(545, 20, 251, 51))
        self.Title.setStyleSheet("font: 36pt \"Sans Serif\"; color:rgb(239, 239, 239)")
        self.Title.setObjectName("Title")
        self.TabBar = QtWidgets.QWidget(self.widget)
        self.TabBar.setGeometry(QtCore.QRect(0, 80, 1340, 80))
        self.TabBar.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.TabBar.setObjectName("TabBar")
        self.IntroductionTab = QtWidgets.QPushButton(self.TabBar)
        self.IntroductionTab.setGeometry(QtCore.QRect(10, 5, 200, 70))
        self.IntroductionTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.IntroductionTab.setStyleSheet("border: 2px solid;\n"
                "border-radius: 20px;\n"
                "border-color:rgb(69, 69, 69);\n"
                "background-color: rgb(69, 69, 69);\n"
                "font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
                "")
        self.IntroductionTab.setObjectName("IntroductionTab")
        self.HistoricalBackgroundLabel = QtWidgets.QLabel(self.TabBar)
        self.HistoricalBackgroundLabel.setGeometry(QtCore.QRect(220, 5, 200, 70))
        self.HistoricalBackgroundLabel.setStyleSheet("border: 2px solid;\n"
                "border-radius: 20px;\n"
                "border-color:rgb(69, 69, 69);\n"
                "background-color: rgb(69, 69, 69);\n"
                "font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
                "")
        self.HistoricalBackgroundLabel.setObjectName("HistoricalBackgroundLabel")
        self.HistoricalBackgroundTab = QtWidgets.QPushButton(self.TabBar)
        self.HistoricalBackgroundTab.setGeometry(QtCore.QRect(220, 5, 200, 70))
        self.HistoricalBackgroundTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.HistoricalBackgroundTab.setStyleSheet("border-radius: 20px;\n"
                "background-color: rgba(0, 0, 0, 0);\n"
                "font: 18pt \"Sans Serif\";\n"
                "")
        self.HistoricalBackgroundTab.setText("")
        self.HistoricalBackgroundTab.setObjectName("HistoricalBackgroundTab")
        self.WhatIsTheRHTab = QtWidgets.QPushButton(self.TabBar)
        self.WhatIsTheRHTab.setGeometry(QtCore.QRect(430, 5, 240, 70))
        self.WhatIsTheRHTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.WhatIsTheRHTab.setStyleSheet("border-radius: 20px;\n"
                "background-color: rgba(0, 0, 0, 0);\n"
                "font: 18pt \"Sans Serif\";\n"
                "")
        self.WhatIsTheRHTab.setText("")
        self.WhatIsTheRHTab.setObjectName("WhatIsTheRHTab")
        self.WhatIsTheRHLabel = QtWidgets.QLabel(self.TabBar)
        self.WhatIsTheRHLabel.setGeometry(QtCore.QRect(430, 5, 241, 70))
        self.WhatIsTheRHLabel.setStyleSheet("border: 2px solid;\n"
                "border-radius: 20px;\n"
                "border-color:rgb(69, 69, 69);\n"
                "background-color: rgb(69, 69, 69);\n"
                "font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
                "")
        self.WhatIsTheRHLabel.setObjectName("WhatIsTheRHLabel")
        self.PracticalApplicationsLabel = QtWidgets.QLabel(self.TabBar)
        self.PracticalApplicationsLabel.setGeometry(QtCore.QRect(680, 5, 200, 70))
        self.PracticalApplicationsLabel.setStyleSheet("border: 2px solid;\n"
                "border-radius: 20px;\n"
                "border-color:rgb(69, 69, 69);\n"
                "background-color: rgb(239, 239, 239);\n"
                "font: 18pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
                "")
        self.PracticalApplicationsLabel.setObjectName("PracticalApplicationsLabel")
        self.PracticalApplicationsTab = QtWidgets.QPushButton(self.TabBar)
        self.PracticalApplicationsTab.setGeometry(QtCore.QRect(680, 5, 201, 70))
        self.PracticalApplicationsTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PracticalApplicationsTab.setStyleSheet("border-radius: 20px;\n"
                "background-color: rgba(0, 0, 0, 0);\n"
                "font: 18pt \"Sans Serif\";\n"
                "")
        self.PracticalApplicationsTab.setText("")
        self.PracticalApplicationsTab.setObjectName("PracticalApplicationsTab")
        self.WhatIsTheRHLabel.raise_()
        self.IntroductionTab.raise_()
        self.HistoricalBackgroundLabel.raise_()
        self.HistoricalBackgroundTab.raise_()
        self.WhatIsTheRHTab.raise_()
        self.PracticalApplicationsLabel.raise_()
        self.PracticalApplicationsTab.raise_()
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
        self.SubTitleText.setGeometry(QtCore.QRect(40, 20, 561, 41))
        self.SubTitleText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
                "background-color: rgb(239, 239, 239); padding: 5px;")
        self.SubTitleText.setObjectName("SubTitleText")
        self.MainText = QtWidgets.QLabel(self.MainWidget)
        self.MainText.setGeometry(QtCore.QRect(40, 60, 1251, 401))
        self.MainText.setStyleSheet("font: 13pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
                "background-color: rgb(239, 239, 239); padding: 5px;")
        self.MainText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
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
        self.QuestionText.setGeometry(QtCore.QRect(390, 290, 561, 51))
        self.QuestionText.setStyleSheet("font: 13pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
                "background-color: rgb(239, 239, 239); padding: 5px;")
        self.QuestionText.setWordWrap(True)
        self.QuestionText.setObjectName("QuestionText")
        self.QuestionInput = QtWidgets.QLineEdit(self.MainWidget)
        self.QuestionInput.setGeometry(QtCore.QRect(410, 350, 231, 60))
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
        self.SubmitButton.setGeometry(QtCore.QRect(690, 350, 131, 60))
        self.SubmitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SubmitButton.setStyleSheet("border: 2px solid;\n"
                "border-radius: 20px;\n"
                "border-color:rgb(69, 69, 69);\n"
                "background-color: rgb(69, 69, 69);\n"
                "font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
                "")
        self.SubmitButton.setObjectName("SubmitButton")
        self.MessageLabel = QtWidgets.QLabel(self.MainWidget)
        self.MessageLabel.setGeometry(QtCore.QRect(440, 410, 461, 41))
        self.MessageLabel.setStyleSheet("color: rgb(255, 0, 0);\n"
                "font: 18pt \"Sans Serif\";")
        self.MessageLabel.setObjectName("MessageLabel")
        self.SubTitleText.raise_()
        self.MainText.raise_()
        self.PrevButton.raise_()
        self.NextButton.raise_()
        self.NotesButton.raise_()
        self.QuestionInput.raise_()
        self.SubmitButton.raise_()
        self.QuestionText.raise_()
        self.MessageLabel.raise_()

        self.retranslateUi(PracticalApplicationsScreen)
        QtCore.QMetaObject.connectSlotsByName(PracticalApplicationsScreen)

    def retranslateUi(self, PracticalApplicationsScreen):
        _translate = QtCore.QCoreApplication.translate
        PracticalApplicationsScreen.setWindowTitle(_translate("PracticalApplicationsScreen", "Visualising the Riemann Hypothesis - Introduction"))
        self.Title.setText(_translate("PracticalApplicationsScreen", "Introduction"))
        self.IntroductionTab.setText(_translate("PracticalApplicationsScreen", "Introduction"))
        self.HistoricalBackgroundLabel.setText(_translate("PracticalApplicationsScreen", "<html><head/><body><p align=\"center\">Historical<br>Background</p></body></html>"))
        self.WhatIsTheRHLabel.setText(_translate("PracticalApplicationsScreen", "<html><head/><body><p align=\"center\">What is the<br>Riemann Hypothesis</p></body></html>"))
        self.PracticalApplicationsLabel.setText(_translate("PracticalApplicationsScreen", "<html><head/><body><p align=\"center\">Practical<br>Applications</p></body></html>"))
        self.PrevButton.setText(_translate("PracticalApplicationsScreen", "Prev"))
        self.NextButton.setText(_translate("PracticalApplicationsScreen", "Next"))
        self.SubTitleText.setText(_translate("PracticalApplicationsScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Practical Applications</span></p></body></html>"))
        self.MainText.setText(_translate("PracticalApplicationsScreen", "<html><head/><body><p>Although the Riemann Hypothesis uses a lot of theoretical mathematics, that isn\'t to say that it doesnt have any practical applications.</p><p>If the Riemann Hypothesis was proven to be true, then that would mean that many of theories and conjectures would alwasys be true. For example: The weak Goldbach conjecture - stating that all integers greater than 5 are the sum of three primes; Mills’ constants - numbers that allow you to generate prime numbers, The theory that there will always be at least one prime between consecutive cubes; and the theory that there is a maximum bound between consecutive prime numbers.</p><p>All of these conjectures involve prime numbers, and their distribution. If the Riemann Hypothesis and thus these conjectures were true, then very large prime numbers would be very easy to generate. This would make fields such as crypotography - that heavily rely on large prime numbers being hard to compute - change. Current crypotgraphy algorithms would become obsolete and would have to be replaced with more secure ones.</p><p>The Riemann Hypothesis also has a very interesting correlation to quantum physics. It was discovered in 1996 that the arrangement of the zeta zeroes exhibits the same pattern as the possible values of energy in a quantum chaotic system. </p></body></html>"))
        self.NotesButton.setText(_translate("PracticalApplicationsScreen", "Notes"))
        self.QuestionText.setText(_translate("PracticalApplicationsScreen", "<html><head/><body><p><br/></p></body></html>"))
        self.QuestionInput.setPlaceholderText(_translate("PracticalApplicationsScreen", "Answer"))
        self.SubmitButton.setText(_translate("PracticalApplicationsScreen", "Submit"))
        self.MessageLabel.setText(_translate("PracticalApplicationsScreen", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
