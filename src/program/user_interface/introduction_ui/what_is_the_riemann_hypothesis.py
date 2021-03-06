"""
what_is_the_riemann_hypothesis.py
=================================
A GUI for the what is the riemann hypothesis page of the introduction section
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WhatIsTheRiemannHypothesisScreen(object):

    def setupUi(self, WhatIsTheRiemannHypothesisScreen):
        WhatIsTheRiemannHypothesisScreen.setObjectName("WhatIsTheRiemannHypothesisScreen")
        WhatIsTheRiemannHypothesisScreen.resize(1340, 723)
        WhatIsTheRiemannHypothesisScreen.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(WhatIsTheRiemannHypothesisScreen)
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
                "background-color: rgb(239, 239, 239);\n"
                "font: 18pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
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
        self.SubTitleText.setGeometry(QtCore.QRect(40, 20, 561, 41))
        self.SubTitleText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
                "background-color: rgb(239, 239, 239); padding: 5px;")
        self.SubTitleText.setObjectName("SubTitleText")
        self.MainText = QtWidgets.QLabel(self.MainWidget)
        self.MainText.setGeometry(QtCore.QRect(40, 60, 1251, 281))
        self.MainText.setStyleSheet("font: 13pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
                "background-color: rgb(239, 239, 239); padding: 5px;")
        self.MainText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.MainText.setWordWrap(True)
        self.MainText.setObjectName("MainText")
        self.QuestionText = QtWidgets.QLabel(self.MainWidget)
        self.QuestionText.setGeometry(QtCore.QRect(390, 360, 561, 31))
        self.QuestionText.setStyleSheet("font: 13pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
                "background-color: rgb(239, 239, 239); padding: 5px;")
        self.QuestionText.setWordWrap(True)
        self.QuestionText.setObjectName("QuestionText")
        self.QuestionInput = QtWidgets.QLineEdit(self.MainWidget)
        self.QuestionInput.setGeometry(QtCore.QRect(540, 400, 101, 60))
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
        self.SubmitButton.setGeometry(QtCore.QRect(690, 400, 131, 60))
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
        self.SubTitleText.raise_()
        self.MainText.raise_()
        self.PrevButton.raise_()
        self.NextButton.raise_()
        self.QuestionText.raise_()
        self.QuestionInput.raise_()
        self.SubmitButton.raise_()
        self.MessageLabel.raise_()

        self.retranslateUi(WhatIsTheRiemannHypothesisScreen)
        QtCore.QMetaObject.connectSlotsByName(WhatIsTheRiemannHypothesisScreen)

    def retranslateUi(self, WhatIsTheRiemannHypothesisScreen):
        _translate = QtCore.QCoreApplication.translate
        WhatIsTheRiemannHypothesisScreen.setWindowTitle(_translate("WhatIsTheRiemannHypothesisScreen", "Visualising the Riemann Hypothesis - Introduction"))
        self.Title.setText(_translate("WhatIsTheRiemannHypothesisScreen", "Introduction"))
        self.IntroductionTab.setText(_translate("WhatIsTheRiemannHypothesisScreen", "Introduction"))
        self.HistoricalBackgroundLabel.setText(_translate("WhatIsTheRiemannHypothesisScreen", "<html><head/><body><p align=\"center\">Historical<br>Background</p></body></html>"))
        self.WhatIsTheRHLabel.setText(_translate("WhatIsTheRiemannHypothesisScreen", "<html><head/><body><p align=\"center\">What is the<br>Riemann Hypothesis</p></body></html>"))
        self.PracticalApplicationsLabel.setText(_translate("WhatIsTheRiemannHypothesisScreen", "<html><head/><body><p align=\"center\">Practical<br>Applications</p></body></html>"))
        self.PrevButton.setText(_translate("WhatIsTheRiemannHypothesisScreen", "Prev"))
        self.NextButton.setText(_translate("WhatIsTheRiemannHypothesisScreen", "Next"))
        self.SubTitleText.setText(_translate("WhatIsTheRiemannHypothesisScreen", "<html><head/><body><p><span style=\" font-weight:600;\">What is the Riemann Hypothesis</span></p></body></html>"))
        self.MainText.setText(_translate("WhatIsTheRiemannHypothesisScreen", "<html><head/><body><p>In his 1859 Paper \'On the Number of Primes Less Than a Given Magnitude\', Bernhard Riemann explored and researched the prime numbers. He did this using the riemann zeta function, which is the sum from 1 to infinity of n to the power -s, where s is the input to the function. </p><p>Riemann used a process called analytic continuation to allow this function to be true for not just all real numbers, but also imaginary and complex numbers. Imaginary numbers are denoted by the imaginary unit i, where i is the square root of -1, a number that is undefined using just the real numbers. A complex number is one that has a real part and an imaginary part. <br/>Riemann used complex numbers in the Riemann Zeta function and found something very interesting. First was that whenever the input to the function was a negative even integer, then the function always output 0. Second, was that the function will also output Zero when the imaginary part of the input is between zero and one. The first point was relatively easy to explain as to why it happened, leading to the negative even integers being known as the trivial zeroes for this function. However, the second point was a little bit harder to explain. Riemann managed to prove this point, but also noticed that these zeroes only occur when the imaginary part of the input is 1/2. This was not so easy to prove, and thus these zeroes were known as the nontrivial zeroes.</p><p>The Riemann Hypothesis states that \'the real part of every nontrivial zero of the Riemann Zeta Function is 1/2\'. </p></body></html>"))
        self.QuestionText.setText(_translate("WhatIsTheRiemannHypothesisScreen", "<html><head/><body><p><br/></p></body></html>"))
        self.QuestionInput.setPlaceholderText(_translate("WhatIsTheRiemannHypothesisScreen", "Answer"))
        self.SubmitButton.setText(_translate("WhatIsTheRiemannHypothesisScreen", "Submit"))
        self.MessageLabel.setText(_translate("WhatIsTheRiemannHypothesisScreen", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
