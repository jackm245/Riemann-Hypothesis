"""
historical_background.py
========================
A GUI for the historical background page of the introduction section
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HistoricalBackgroundScreen(object):

    def setupUi(self, HistoricalBackgroundScreen):
        HistoricalBackgroundScreen.setObjectName("HistoricalBackgroundScreen")
        HistoricalBackgroundScreen.resize(1340, 723)
        HistoricalBackgroundScreen.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(HistoricalBackgroundScreen)
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
                "background-color: rgb(239, 239, 239);\n"
                "font: 18pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
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
                "background-color: rgb(69, 69, 69);\n"
                "font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
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
        self.SubTitleText.setGeometry(QtCore.QRect(40, 20, 381, 41))
        self.SubTitleText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
                "background-color: rgb(239, 239, 239); padding: 5px;")
        self.SubTitleText.setObjectName("SubTitleText")
        self.MainText = QtWidgets.QLabel(self.MainWidget)
        self.MainText.setGeometry(QtCore.QRect(40, 60, 1251, 401))
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
        self.SubTitleText.raise_()
        self.MainText.raise_()
        self.PrevButton.raise_()
        self.NextButton.raise_()
        self.NotesButton.raise_()

        self.retranslateUi(HistoricalBackgroundScreen)
        QtCore.QMetaObject.connectSlotsByName(HistoricalBackgroundScreen)

    def retranslateUi(self, HistoricalBackgroundScreen):
        _translate = QtCore.QCoreApplication.translate
        HistoricalBackgroundScreen.setWindowTitle(_translate("HistoricalBackgroundScreen", "Visualising the Riemann Hypothesis - Introduction"))
        self.Title.setText(_translate("HistoricalBackgroundScreen", "Introduction"))
        self.IntroductionTab.setText(_translate("HistoricalBackgroundScreen", "Introduction"))
        self.HistoricalBackgroundLabel.setText(_translate("HistoricalBackgroundScreen", "<html><head/><body><p align=\"center\">Historical<br>Background</p></body></html>"))
        self.WhatIsTheRHLabel.setText(_translate("HistoricalBackgroundScreen", "<html><head/><body><p align=\"center\">What is the<br>Riemann Hypothesis</p></body></html>"))
        self.PracticalApplicationsLabel.setText(_translate("HistoricalBackgroundScreen", "<html><head/><body><p align=\"center\">Practical<br>Applications</p></body></html>"))
        self.PrevButton.setText(_translate("HistoricalBackgroundScreen", "Prev"))
        self.NextButton.setText(_translate("HistoricalBackgroundScreen", "Next"))
        self.SubTitleText.setText(_translate("HistoricalBackgroundScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Historical Background</span></p></body></html>"))
        self.MainText.setText(_translate("HistoricalBackgroundScreen", "<html><head/><body><p>The Riemann Hypothesis originates from a mathematical problem from hundreds of years back. In the 1730\'s, Leonhard Euler (A very smart mathematician), has been investigating the function that went on to be known as the Riemann Zeta Function. In 1737, Euler was able to prove that this function could be written as a product of prime numbers, this is known as Euler\'s product formula.</p><p>In 1859, Bernhard Riemann publsihed a paper \'On the Number of Primes Less Than a Given Magnitude\'. In this paper, he investigates the function previously looked at by Euler, but extends its definition to include Complex Numbers, as well as Real Numbers. It is in this paper that the Riemann Hypothesis was born. The Riemann Hypothesis states that the Riemann zeta function has its zeros only at the negative even integers and complex numbers with real part 0.5.</p><p>In 1900, the mathematician David Hibert released a list of mathematical problems that were all unsolved at the time. He called for other mathematicians to try and solve these problems. These problems included the a Proof of the Riemann Hypothesis, and many problems relating to it; many of which are still unsolved to this day</p><p>In 1915, GH Hardy managed to prove that there were an inifinite amount of numbers for which the Riemann Hypothesis was true, this showed that proving the Riemann Hypothesis would require a full proof, rather than a proof by exhaustion. </p><p>In 1986 van de Lune, te Riele &amp; Winter managed to find values for 1500000001 Zeta Zeroes.</p><p>Then in 2000, the Clay Mathematics Institure named the Riemann Hypothesis as one of their \'Millenium Problems\', with a reward of $1,000,000 for anyone who manages to prove it.</p></body></html>"))
        self.NotesButton.setText(_translate("HistoricalBackgroundScreen", "Notes"))
