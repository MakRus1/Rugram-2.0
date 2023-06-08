# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RegisterPage.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_RegisterPage(object):
    def setupUi(self, RegisterPage):
        if not RegisterPage.objectName():
            RegisterPage.setObjectName(u"RegisterPage")
        RegisterPage.resize(800, 600)
        RegisterPage.setStyleSheet(u"background-color: gray")
        self.centralwidget = QWidget(RegisterPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(50, 50, 681, 461))
        self.frame.setStyleSheet(u"background-color: white;\nborder-radius: 10px")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lTitle = QLabel(self.frame)
        self.lTitle.setObjectName(u"lTitle")
        self.lTitle.setGeometry(QRect(290, 30, 55, 16))
        self.lTitle.setAlignment(Qt.AlignCenter)
        self.leUsername = QLineEdit(self.frame)
        self.leUsername.setObjectName(u"leUsername")
        self.leUsername.setGeometry(QRect(260, 120, 113, 22))
        self.leUsername.setStyleSheet("border: 3px solid lightgray")
        self.lePassword = QLineEdit(self.frame)
        self.lePassword.setObjectName(u"lePassword")
        self.lePassword.setGeometry(QRect(260, 160, 113, 22))
        self.lePassword.setStyleSheet("border: 3px solid lightgray")
        self.teBio = QTextEdit(self.frame)
        self.teBio.setObjectName(u"teBio")
        self.teBio.setGeometry(QRect(260, 200, 104, 87))
        self.teBio.setStyleSheet("border: 3px solid lightgray")
        self.pbRegister = QPushButton(self.frame)
        self.pbRegister.setObjectName(u"pbRegister")
        self.pbRegister.setGeometry(QRect(260, 310, 93, 28))
        self.lQuestion = QLabel(self.frame)
        self.lQuestion.setObjectName(u"lQuestion")
        self.lQuestion.setGeometry(QRect(230, 350, 55, 16))
        self.lQuestion.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pbLogIn = QPushButton(self.frame)
        self.pbLogIn.setObjectName(u"pbLogIn")
        self.pbLogIn.setGeometry(QRect(300, 340, 93, 28))
        self.pbSetImage = QPushButton(self.frame)
        self.pbSetImage.setObjectName(u"pbSetImage")
        self.pbSetImage.setGeometry(QRect(270, 70, 93, 28))
        self.fSideBar = QFrame(self.centralwidget)
        self.fSideBar.setObjectName(u"fSideBar")
        self.fSideBar.setGeometry(QRect(0, 0, 801, 31))
        self.fSideBar.setStyleSheet(u"background-color: white")
        self.fSideBar.setFrameShape(QFrame.StyledPanel)
        self.fSideBar.setFrameShadow(QFrame.Raised)
        self.pbCloseWindow = QPushButton(self.fSideBar)
        self.pbCloseWindow.setObjectName(u"pbCloseWindow")
        self.pbCloseWindow.setGeometry(QRect(690, 0, 93, 28))
        icon = QIcon()
        icon.addFile(u"res/close-window-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pbCloseWindow.setIcon(icon)
        self.pbMinimizeWindow = QPushButton(self.fSideBar)
        self.pbMinimizeWindow.setObjectName(u"pbMinimizeWindow")
        self.pbMinimizeWindow.setGeometry(QRect(580, 0, 93, 28))
        icon1 = QIcon()
        icon1.addFile(u"res/minimize-window-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pbMinimizeWindow.setIcon(icon1)
        RegisterPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegisterPage)

        QMetaObject.connectSlotsByName(RegisterPage)
    # setupUi

    def retranslateUi(self, RegisterPage):
        RegisterPage.setWindowTitle(QCoreApplication.translate("RegisterPage", u"Rugram", None))
        self.lTitle.setText(QCoreApplication.translate("RegisterPage", u"TextLabel", None))
        self.leUsername.setPlaceholderText(QCoreApplication.translate("RegisterPage", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.lePassword.setPlaceholderText(QCoreApplication.translate("RegisterPage", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.teBio.setPlaceholderText(QCoreApplication.translate("RegisterPage", u"\u041e \u0441\u0435\u0431\u0435", None))
        self.pbRegister.setText(QCoreApplication.translate("RegisterPage", u"\u0437\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.lQuestion.setText(QCoreApplication.translate("RegisterPage", u"\u0423\u0436\u0435 \u0435\u0441\u0442\u044c \u0430\u043a\u043a\u0430\u0443\u043d\u0442?", None))
        self.pbLogIn.setText(QCoreApplication.translate("RegisterPage", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.pbSetImage.setText(QCoreApplication.translate("RegisterPage", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u043e\u0442\u043e", None))
        self.pbCloseWindow.setText("")
        self.pbMinimizeWindow.setText("")
    # retranslateUi

