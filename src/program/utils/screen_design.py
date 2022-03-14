from PyQt5 import QtCore, QtGui, QtWidgets


class Screen(QtWidgets.QDialog):

    def __init__(self):
        super(Screen, self).__init__()
        self.setFixedWidth(1340)
        self.setFixedHeight(720)

    def goto_mainmenu(self):
        from ..main_section import MainMenu
        self.main_menu = MainMenu()
        self.hide()
