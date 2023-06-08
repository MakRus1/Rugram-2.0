# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginPage.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        if not LoginPage.objectName():
            LoginPage.setObjectName(u"LoginPage")
        LoginPage.resize(800, 600)
        LoginPage.setLayoutDirection(Qt.LeftToRight)
        LoginPage.setStyleSheet(u"background-color: gray")
        LoginPage.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.centralwidget = QWidget(LoginPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(100, 100, 600, 400))
        self.frame.setStyleSheet(u"background-color: white;\n"
"\n"
"border-radius: 10px")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.leLogin = QLineEdit(self.frame)
        self.leLogin.setObjectName(u"leLogin")
        self.leLogin.setGeometry(QRect(125, 150, 350, 30))
        font = QFont()
        font.setFamilies([u"Yu Gothic UI"])
        font.setPointSize(10)
        self.leLogin.setFont(font)
        self.leLogin.setStyleSheet(u"padding: 5px;\nborder: 3px solid lightgray")
        self.lePassword = QLineEdit(self.frame)
        self.lePassword.setObjectName(u"lePassword")
        self.lePassword.setGeometry(QRect(125, 200, 350, 30))
        self.lePassword.setFont(font)
        self.lePassword.setStyleSheet(u"padding: 5px;\nborder: 3px solid lightgray")
        self.pbSignIn = QPushButton(self.frame)
        self.pbSignIn.setObjectName(u"pbSignIn")
        self.pbSignIn.setGeometry(QRect(125, 250, 350, 40))
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic UI"])
        font1.setPointSize(14)
        self.pbSignIn.setFont(font1)
        self.pbSignIn.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: 2px solid gray;\n"
"}\n"
"\n"
"QPushButton:hover \n"
"{\n"
"	background-color: lightgray;\n"
"}")
        self.pbSignUp = QPushButton(self.frame)
        self.pbSignUp.setObjectName(u"pbSignUp")
        self.pbSignUp.setGeometry(QRect(300, 300, 175, 30))
        self.pbSignUp.setFont(font)
        self.pbSignUp.setStyleSheet(u"text-align: left;\n"
"border: none;\n"
"padding: 5px;\n"
"color: blue;")
        self.lHello = QLabel(self.frame)
        self.lHello.setObjectName(u"lHello")
        self.lHello.setGeometry(QRect(125, 60, 350, 70))
        font2 = QFont()
        font2.setFamilies([u"Yu Gothic UI"])
        font2.setPointSize(20)
        self.lHello.setFont(font2)
        self.lHello.setStyleSheet(u"background-color: white;\n"
"border: 3px solid gray;")
        self.lHello.setAlignment(Qt.AlignCenter)
        self.lQuestion = QLabel(self.frame)
        self.lQuestion.setObjectName(u"lQuestion")
        self.lQuestion.setGeometry(QRect(125, 300, 175, 30))
        self.lQuestion.setFont(font)
        self.lQuestion.setStyleSheet(u"padding: 5px")
        self.lQuestion.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lError = QLabel(self.frame)
        self.lError.setObjectName(u"lError")
        self.lError.setEnabled(True)
        self.lError.setGeometry(QRect(125, 230, 240, 16))
        self.lError.setFont(font)
        self.lError.setStyleSheet(u"color: red")
        self.lQuestion.raise_()
        self.leLogin.raise_()
        self.lePassword.raise_()
        self.pbSignIn.raise_()
        self.pbSignUp.raise_()
        self.lHello.raise_()
        self.lError.raise_()
        self.fSideBar = QFrame(self.centralwidget)
        self.fSideBar.setObjectName(u"fSideBar")
        self.fSideBar.setGeometry(QRect(0, 0, 800, 20))
        self.fSideBar.setStyleSheet(u"background-color: white")
        self.fSideBar.setFrameShape(QFrame.StyledPanel)
        self.fSideBar.setFrameShadow(QFrame.Raised)
        self.pbCloseWindow = QPushButton(self.fSideBar)
        self.pbCloseWindow.setObjectName(u"pbCloseWindow")
        self.pbCloseWindow.setGeometry(QRect(780, 0, 20, 20))
        self.pbCloseWindow.setStyleSheet(u"QPushButton\n{\nborder: none\n}\n"
                                         "QPushButton:hover\n{\nbackground-color: red\n}")
        icon = QIcon()
        icon.addFile(u"res/close-window-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pbCloseWindow.setIcon(icon)
        self.pbMinimizeWindow = QPushButton(self.fSideBar)
        self.pbMinimizeWindow.setObjectName(u"pbMinimizeWindow")
        self.pbMinimizeWindow.setGeometry(QRect(760, 0, 20, 20))
        self.pbMinimizeWindow.setStyleSheet(u"QPushButton\n{\nborder: none\n}\n"
                                            "QPushButton:hover\n{\nbackground-color: lightgray\n}")
        icon1 = QIcon()
        icon1.addFile(u"res/minimize-window-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pbMinimizeWindow.setIcon(icon1)
        LoginPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginPage)

        QMetaObject.connectSlotsByName(LoginPage)
    # setupUi

    def retranslateUi(self, LoginPage):
        LoginPage.setWindowTitle(QCoreApplication.translate("LoginPage", u"Rugram", None))
        self.leLogin.setPlaceholderText(QCoreApplication.translate("LoginPage", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.lePassword.setPlaceholderText(QCoreApplication.translate("LoginPage", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.pbSignIn.setText(QCoreApplication.translate("LoginPage", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.pbSignUp.setText(QCoreApplication.translate("LoginPage", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.lHello.setText(QCoreApplication.translate("LoginPage", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c", None))
        self.lQuestion.setText(QCoreApplication.translate("LoginPage", u"\u0415\u0449\u0451 \u043d\u0435 \u0441 \u043d\u0430\u043c\u0438?", None))
        self.lError.setText(QCoreApplication.translate("LoginPage", u"\u041d\u0435\u0432\u0435\u0440\u043d\u044b\u0439 \u043b\u043e\u0433\u0438\u043d \u0438\u043b\u0438 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.pbCloseWindow.setText("")
        self.pbMinimizeWindow.setText("")
    # retranslateUi

