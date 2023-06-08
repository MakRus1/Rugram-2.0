# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainPage(object):
    def setupUi(self, MainPage):
        if not MainPage.objectName():
            MainPage.setObjectName(u"MainPage")
        MainPage.resize(800, 600)
        MainPage.setLayoutDirection(Qt.LeftToRight)
        MainPage.setStyleSheet(u"background-color: gray")
        MainPage.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.centralwidget = QWidget(MainPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(100, 100, 600, 400))
        self.frame.setStyleSheet(u"background-color: white;\n"
"\n"
"border-radius: 10px\n")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.fSideBar = QFrame(self.centralwidget)
        self.fSideBar.setObjectName(u"fSideBar")
        self.fSideBar.setGeometry(QRect(0, 0, 800, 20))
        self.fSideBar.setStyleSheet(u"background-color: white")
        self.fSideBar.setFrameShape(QFrame.StyledPanel)
        self.fSideBar.setFrameShadow(QFrame.Raised)
        self.pbCloseWindow = QPushButton(self.fSideBar)
        self.pbCloseWindow.setObjectName(u"pbCloseWindow")
        self.pbCloseWindow.setGeometry(QRect(780, 0, 20, 20))
        icon = QIcon()
        icon.addFile(u"res/close-window-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pbCloseWindow.setIcon(icon)
        self.pbMinimizeWindow = QPushButton(self.fSideBar)
        self.pbMinimizeWindow.setObjectName(u"pbMinimizeWindow")
        self.pbMinimizeWindow.setGeometry(QRect(760, 0, 20, 20))
        icon1 = QIcon()
        icon1.addFile(u"res/minimize-window-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pbMinimizeWindow.setIcon(icon1)
        MainPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainPage)

        QMetaObject.connectSlotsByName(MainPage)
    # setupUi

    def retranslateUi(self, MainPage):
        MainPage.setWindowTitle(QCoreApplication.translate("MainPage", u"Rugram", None))
        self.pbCloseWindow.setText("")
        self.pbMinimizeWindow.setText("")
    # retranslateUi

