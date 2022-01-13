import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from homescreen import Ui_MainMenu
from login import Ui_Dialog


#  Main Entry Point to the Program
#  if __name__ == '__main__':
    #  app = QtWidgets.QApplication(sys.argv)
    #  MainMenu = QtWidgets.QDialog()
    #  ui = Ui_MainMenu()
    #  ui.setupUi(MainMenu)
    #  MainMenu.show()
    #  sys.exit(app.exec_())

class Login(QtWidgets.QDialog):

    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)
        self.show()


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.MainMenu = Ui_MainMenu()
        self.MainMenu.setupUi(self)
        self.setFixedWidth(1340)
        self.setFixedHeight(720)
        self.MainMenu.LogInButton.clicked.connect(self.gotologin)
        self.show()


    def gotologin(self):
        self.login = Login()
        self.hide()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = Main()
    sys.exit(app.exec())
