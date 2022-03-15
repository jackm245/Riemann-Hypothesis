"""
screen_design.py
================

Contains the Screen class
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Screen(QtWidgets.QDialog):

    """
    The Screen Class is inherited by all of the other classes that are used
    to interact witht the GUI

    The prupose of this class is to set some default values, and automatically
    run functions that are common to every class that inherits it

    It also contains some functions which are commonly run by classes that
    inherit it
    """

    def __init__(self):
        super(Screen, self).__init__()
        self.setFixedWidth(1340)
        self.setFixedHeight(720)

    def goto_mainmenu(self):
        from ..main_section import MainMenu
        self.main_menu = MainMenu()
        self.hide()
