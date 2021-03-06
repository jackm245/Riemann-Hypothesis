"""
progress.py
============
A GUI for the progress page
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProgressScreen(object):

    def setupUi(self, ProgressScreen):
        ProgressScreen.setObjectName("ProgressScreen")
        ProgressScreen.resize(1340, 723)
        ProgressScreen.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(ProgressScreen)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1340, 720))
        self.widget.setStyleSheet("background-color: rgb(69, 69, 69);")
        self.widget.setObjectName("widget")
        self.Title = QtWidgets.QLabel(self.widget)
        self.Title.setGeometry(QtCore.QRect(575, 20, 191, 51))
        self.Title.setStyleSheet("font: 36pt \"Sans Serif\"; color:rgb(239, 239, 239)")
        self.Title.setObjectName("Title")
        self.TabBar = QtWidgets.QWidget(self.widget)
        self.TabBar.setGeometry(QtCore.QRect(0, 80, 1340, 80))
        self.TabBar.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.TabBar.setObjectName("TabBar")
        self.ProgressTab = QtWidgets.QPushButton(self.TabBar)
        self.ProgressTab.setGeometry(QtCore.QRect(10, 5, 200, 70))
        self.ProgressTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ProgressTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239);\n"
"font: 18pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"")
        self.ProgressTab.setObjectName("ProgressTab")
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
        self.SubTitleText = QtWidgets.QLabel(self.MainWidget)
        self.SubTitleText.setGeometry(QtCore.QRect(40, 20, 251, 51))
        self.SubTitleText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.SubTitleText.setObjectName("SubTitleText")
        self.MessageLabel = QtWidgets.QLabel(self.MainWidget)
        self.MessageLabel.setGeometry(QtCore.QRect(410, 470, 530, 41))
        self.MessageLabel.setStyleSheet("color: rgb(0, 140, 0);\n"
"font: 18pt \"Sans Serif\";")
        self.MessageLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.MessageLabel.setObjectName("MessageLabel")
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
        self.Table = QtWidgets.QTableWidget(self.MainWidget)
        self.Table.setGeometry(QtCore.QRect(30, 70, 1261, 371))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Table.setFont(font)
        self.Table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Table.setAlternatingRowColors(True)
        self.Table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.Table.setObjectName("Table")
        self.Table.setColumnCount(3)
        self.Table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Table.setHorizontalHeaderItem(2, item)

        self.retranslateUi(ProgressScreen)
        QtCore.QMetaObject.connectSlotsByName(ProgressScreen)

    def retranslateUi(self, ProgressScreen):
        _translate = QtCore.QCoreApplication.translate
        ProgressScreen.setWindowTitle(_translate("ProgressScreen", "Visualising the Riemann Hypothesis - Progress"))
        self.Title.setText(_translate("ProgressScreen", "Progress"))
        self.ProgressTab.setText(_translate("ProgressScreen", "Progress"))
        self.BackButton.setText(_translate("ProgressScreen", "Back"))
        self.SubTitleText.setText(_translate("ProgressScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Username</span></p></body></html>"))
        self.MessageLabel.setText(_translate("ProgressScreen", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.NotesButton.setText(_translate("ProgressScreen", "Notes"))
        item = self.Table.horizontalHeaderItem(0)
        item.setText(_translate("ProgressScreen", "Question"))
        item = self.Table.horizontalHeaderItem(1)
        item.setText(_translate("ProgressScreen", "Answer"))
        item = self.Table.horizontalHeaderItem(2)
        item.setText(_translate("ProgressScreen", "Correct"))
