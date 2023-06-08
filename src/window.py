import os

from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ico_path = os.path.join(BASE_DIR[:-3], "forms/res/")

class Window(QMainWindow):
    def __init__(self, ui, parent=None):
        super(Window, self).__init__(parent)
        self.ui = ui
        self.SetUp()

    def SetUp(self):
        self.ui.setupUi(self)
        self.setWindowTitle("Rugram")

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.setFixedSize(QtGui.QScreen.size(QApplication.primaryScreen()).width(),
                          QtGui.QScreen.size(QApplication.primaryScreen()).height())

        self.ui.fSideBar.setFixedSize(self.screen().size().width(), 25)
        self.ui.fSideBar.move(0, 0)
        self.ui.pbCloseWindow.move(self.screen().size().width() - 40, 0)
        self.ui.pbCloseWindow.setFixedSize(40, 25)
        self.ui.pbCloseWindow.setIcon(QtGui.QPixmap(ico_path + "/close-window-50.png"))
        self.ui.pbCloseWindow.setStyleSheet("QPushButton\n{\nborder: none\n}\n"
                                            "QPushButton:hover\n{\nbackground-color: red\n}\n")
        self.ui.pbMinimizeWindow.move(self.screen().size().width() - 80, 0)
        self.ui.pbMinimizeWindow.setFixedSize(40, 25)
        self.ui.pbMinimizeWindow.setIcon(QtGui.QPixmap(ico_path + "/minimize-window-50.png"))
        self.ui.pbMinimizeWindow.setStyleSheet("QPushButton\n{\nborder: none\n}\n"
                                            "QPushButton:hover\n{\nbackground-color: lightgray\n}\n")

        self.ui.frame.setFixedSize(self.screen().size().width() - 400, self.screen().size().height() - 200)
        self.ui.frame.move(200, 100)

        self.ui.pbCloseWindow.clicked.connect(self.close)
        self.ui.pbMinimizeWindow.clicked.connect(self.showMinimized)