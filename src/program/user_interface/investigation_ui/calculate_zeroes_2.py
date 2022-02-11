# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/investigation_screens/calculate_zeroes_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CalculateZeroes2Screen(object):
    def setupUi(self, CalculateZeroes2Screen):
        CalculateZeroes2Screen.setObjectName("CalculateZeroes2Screen")
        CalculateZeroes2Screen.resize(1340, 720)
        CalculateZeroes2Screen.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(CalculateZeroes2Screen)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1340, 720))
        self.widget.setStyleSheet("background-color: rgb(69, 69, 69);")
        self.widget.setObjectName("widget")
        self.Title = QtWidgets.QLabel(self.widget)
        self.Title.setGeometry(QtCore.QRect(540, 20, 261, 51))
        self.Title.setStyleSheet("font: 36pt \"Sans Serif\"; color:rgb(239, 239, 239)")
        self.Title.setObjectName("Title")
        self.TabBar = QtWidgets.QWidget(self.widget)
        self.TabBar.setGeometry(QtCore.QRect(0, 80, 1340, 80))
        self.TabBar.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.TabBar.setObjectName("TabBar")
        self.ZeroesTab = QtWidgets.QPushButton(self.TabBar)
        self.ZeroesTab.setGeometry(QtCore.QRect(10, 5, 401, 70))
        self.ZeroesTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ZeroesTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239,239);\n"
"font: 36pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
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
"font: 36pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.PrevButton.setObjectName("PrevButton")
        self.NextButton = QtWidgets.QPushButton(self.MainWidget)
        self.NextButton.setGeometry(QtCore.QRect(1110, 460, 200, 70))
        self.NextButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NextButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 36pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.NextButton.setObjectName("NextButton")
        self.SubTitleText = QtWidgets.QLabel(self.MainWidget)
        self.SubTitleText.setGeometry(QtCore.QRect(40, 20, 381, 41))
        self.SubTitleText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.SubTitleText.setObjectName("SubTitleText")
        self.ErrorLabel = QtWidgets.QLabel(self.MainWidget)
        self.ErrorLabel.setGeometry(QtCore.QRect(400, 400, 541, 61))
        self.ErrorLabel.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 18pt \"Sans Serif\";")
        self.ErrorLabel.setObjectName("ErrorLabel")
        self.ZetaTable = QtWidgets.QTableWidget(self.MainWidget)
        self.ZetaTable.setGeometry(QtCore.QRect(510, 30, 300, 351))
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
        self.DatabaseButton = QtWidgets.QPushButton(self.MainWidget)
        self.DatabaseButton.setGeometry(QtCore.QRect(270, 460, 391, 70))
        self.DatabaseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DatabaseButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 36pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.DatabaseButton.setObjectName("DatabaseButton")
        self.FileButton = QtWidgets.QPushButton(self.MainWidget)
        self.FileButton.setGeometry(QtCore.QRect(680, 460, 391, 70))
        self.FileButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FileButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 36pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.FileButton.setObjectName("FileButton")

        self.retranslateUi(CalculateZeroes2Screen)
        QtCore.QMetaObject.connectSlotsByName(CalculateZeroes2Screen)

    def retranslateUi(self, CalculateZeroes2Screen):
        _translate = QtCore.QCoreApplication.translate
        CalculateZeroes2Screen.setWindowTitle(_translate("CalculateZeroes2Screen", "Visualising the Riemann Hypothesis - Zeta Zeroes"))
        self.Title.setText(_translate("CalculateZeroes2Screen", "Zeta Zeroes"))
        self.ZeroesTab.setText(_translate("CalculateZeroes2Screen", "Zeroes Calculator"))
        self.PrevButton.setText(_translate("CalculateZeroes2Screen", "Prev"))
        self.NextButton.setText(_translate("CalculateZeroes2Screen", "Next"))
        self.SubTitleText.setText(_translate("CalculateZeroes2Screen", "<html><head/><body><p><span style=\" font-weight:600;\">Zeta Zeroes</span></p></body></html>"))
        self.ErrorLabel.setText(_translate("CalculateZeroes2Screen", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        item = self.ZetaTable.horizontalHeaderItem(0)
        item.setText(_translate("CalculateZeroes2Screen", "Re(s)"))
        item = self.ZetaTable.horizontalHeaderItem(1)
        item.setText(_translate("CalculateZeroes2Screen", "Im(s)"))
        self.DatabaseButton.setText(_translate("CalculateZeroes2Screen", "Save to database"))
        self.FileButton.setText(_translate("CalculateZeroes2Screen", "Save to file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CalculateZeroes2Screen = QtWidgets.QDialog()
    ui = Ui_CalculateZeroes2Screen()
    ui.setupUi(CalculateZeroes2Screen)
    CalculateZeroes2Screen.show()
    sys.exit(app.exec_())
