import sys

from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from src.frame import Frame

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Frame(app)

    window.showFullScreen()

    sys.exit(app.exec())
