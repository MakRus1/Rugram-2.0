import time

from PySide6 import QtWidgets
from PySide6.QtGui import QAction, QPainterPath, QPainter

from src.window import *

from forms.ui_LoginPage import *
from forms.ui_RegisterPage import *
from forms.ui_MainPage import *

from database.db_handler import *


class Post:
    photoPath = ""
    title = ""
    description = ""
    isLiked = False

class UserInfo:
    name = ""
    passw = ""
    bio = ""
    imagePath = ""
    subscribers = []
    subscriptions = []
    posts = []
    favorites = []


class Frame(Window):
    def __init__(self, app, parent=None):
        self.post = Post()
        self.mainName = ""
        self.app = app
        super().__init__(Ui_LoginPage(), parent)
        self.SignIn()


    def SignIn(self):
        self.ui = Ui_LoginPage()
        self.SetUp()
        titleFont = QFont()
        titleFont.setFamilies([u"Yu Gothic UI"])
        titleFont.setPointSize(24)

        mainFont = QFont()
        mainFont.setFamilies([u"Yu Gothic UI"])
        mainFont.setPointSize(16)

        subFont = QFont()
        subFont.setFamilies([u"Yu Gothic UI"])
        subFont.setPointSize(18)

        self.ui.lHello.setFixedSize(self.ui.frame.size().width() - 600, 80)
        self.ui.lHello.move((self.ui.frame.width() - self.ui.lHello.width()) // 2, 150)
        self.ui.lHello.setFont(titleFont)

        self.ui.leLogin.setFixedSize(self.ui.frame.size().width() - 600, 60)
        self.ui.leLogin.move((self.ui.frame.width() - self.ui.leLogin.width()) // 2, 250)
        self.ui.leLogin.setFont(mainFont)

        self.ui.lePassword.setFixedSize(self.ui.frame.size().width() - 600, 60)
        self.ui.lePassword.move((self.ui.frame.width() - self.ui.lePassword.width()) // 2, 350)
        self.ui.lePassword.setFont(mainFont)
        self.ui.lePassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.ui.pbSignIn.setFixedSize(self.ui.frame.size().width() - 600, 60)
        self.ui.pbSignIn.move((self.ui.frame.width() - self.ui.pbSignIn.width()) // 2, 450)
        self.ui.pbSignIn.setFont(subFont)

        self.ui.lQuestion.setFixedSize((self.ui.frame.size().width() - 600) // 2, 40)
        self.ui.lQuestion.move((self.ui.frame.width() - self.ui.lHello.width()) // 2, 550)
        self.ui.lQuestion.setFont(mainFont)

        self.ui.pbSignUp.setFixedSize((self.ui.frame.size().width() - 600) // 2, 40)
        self.ui.pbSignUp.move(self.ui.frame.width() // 2, 550)
        self.ui.pbSignUp.setFont(mainFont)

        self.ui.lError.setFixedSize(self.ui.frame.size().width() - 600, 40)
        self.ui.lError.move((self.ui.frame.width() - self.ui.lHello.width()) // 2, 410)
        self.ui.lError.setFont(mainFont)
        self.ui.lError.hide()

        self.ui.pbSignIn.clicked.connect(self.auth)
        self.ui.pbSignUp.clicked.connect(self.SignUp)


    def auth(self):
        UserInfo.name = self.ui.leLogin.text()
        UserInfo.passw = self.ui.lePassword.text()
        if Login(UserInfo.name, UserInfo.passw) == False:
            self.ui.lError.show()
        else:
            self.mainName = UserInfo.name
            self.MainPage()


    def SignUp(self):
        self.ui = Ui_RegisterPage()
        self.SetUp()

        titleFont = QFont()
        titleFont.setFamilies([u"Yu Gothic UI"])
        titleFont.setPointSize(20)

        mainFont = QFont()
        mainFont.setFamilies([u"Yu Gothic UI"])
        mainFont.setPointSize(16)

        subFont = QFont()
        subFont.setFamilies([u"Yu Gothic UI"])
        subFont.setPointSize(18)

        self.ui.lTitle.setText("Регистрация")
        self.ui.lTitle.setStyleSheet("border: 3px solid gray")
        self.ui.lTitle.setFixedSize(self.ui.frame.size().width() - 600, 60)
        self.ui.lTitle.move((self.ui.frame.width() - self.ui.lTitle.width()) // 2, 100)
        self.ui.lTitle.setFont(titleFont)

        self.ui.pbSetImage.setStyleSheet("QPushButton\n{\nborder: 2px solid gray;\nborder-radius: 50px;\n}\n"
                                         "QPushButton:hover\n{\nbackground-color: lightgray;\n}\n")
        self.ui.pbSetImage.setFixedSize(100, 100)
        self.ui.pbSetImage.move((self.ui.frame.width() - self.ui.pbSetImage.width()) // 2, 180)

        self.ui.leUsername.setFixedSize(self.ui.frame.size().width() - 600, 40)
        self.ui.leUsername.move((self.ui.frame.width() - self.ui.lTitle.width()) // 2, 300)
        self.ui.leUsername.setFont(mainFont)

        self.ui.lePassword.setFixedSize(self.ui.frame.size().width() - 600, 40)
        self.ui.lePassword.move((self.ui.frame.width() - self.ui.lTitle.width()) // 2, 350)
        self.ui.lePassword.setFont(mainFont)
        self.ui.lePassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.ui.teBio.setFixedSize(self.ui.frame.size().width() - 600, 150)
        self.ui.teBio.move((self.ui.frame.width() - self.ui.lTitle.width()) // 2, 400)
        self.ui.teBio.setFont(mainFont)

        self.ui.pbRegister.setFixedSize(self.ui.frame.size().width() - 600, 40)
        self.ui.pbRegister.move((self.ui.frame.width() - self.ui.lTitle.width()) // 2, 570)
        self.ui.pbRegister.setFont(subFont)
        self.ui.pbRegister.setStyleSheet("QPushButton\n{\nborder: 2px solid gray\n}\n"
                                         "QPushButton:hover\n{\nbackground-color: lightgray\n}\n")
        self.ui.pbRegister.setText("Зарегистрироваться")

        self.ui.lQuestion.setFixedSize((self.ui.frame.size().width() - 600)//2, 40)
        self.ui.lQuestion.move((self.ui.frame.width() - self.ui.lTitle.width()) // 2, 620)
        self.ui.lQuestion.setFont(mainFont)
        self.ui.lQuestion.setStyleSheet(u"padding: 5px")

        self.ui.pbLogIn.setFixedSize((self.ui.frame.size().width() - 600)//2, 40)
        self.ui.pbLogIn.move((self.ui.frame.width())//2, 620)
        self.ui.pbLogIn.setFont(mainFont)
        self.ui.pbLogIn.setStyleSheet(u"border: none; text-align: left; padding: 5px; color: blue\n")

        self.ui.pbSetImage.clicked.connect(self.SetImage)
        self.ui.pbRegister.clicked.connect(self.reg)
        self.ui.pbLogIn.clicked.connect(self.SignIn)


    def SetImage(self):
        UserInfo.imagePath = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите фотографию", filter="*.png; *.jpg; *.jpeg")[0]
        self.ui.pbSetImage.setText("")
        # print(fname[0])
        # self.ui.pbSetImage.setIcon(QtGui.QPixmap(UserInfo.imagePath))
        # self.ui.pbSetImage.setIconSize(QtCore.QSize(100, 100))

        self.ui.lProfileImage = QLabel(self.ui.pbSetImage.parent())
        self.ui.lProfileImage.setFixedSize(self.ui.pbSetImage.width(), self.ui.pbSetImage.height())
        self.ui.lProfileImage.move(self.ui.pbSetImage.x(), self.ui.pbSetImage.y())

        self.target = QPixmap(self.ui.lProfileImage.size())
        self.target.fill(Qt.transparent)
        p = QPixmap(UserInfo.imagePath).scaled(
            self.ui.lProfileImage.width(), self.ui.lProfileImage.height(),
            Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        painter = QPainter(self.target)
        path = QPainterPath()
        path.addRoundedRect(
            0, 0, self.ui.lProfileImage.width(), self.ui.lProfileImage.height(), self.ui.pbSetImage.width()//2, self.ui.pbSetImage.height()//2)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, p)
        self.ui.lProfileImage.setPixmap(self.target)

        self.ui.lProfileImage.show()


    def reg(self):
        self.ui.lError = QtWidgets.QLabel(self.ui.frame)
        self.ui.lError.setObjectName(u"lError")
        self.ui.lError.setGeometry(QRect(125, 60, 350, 70))
        font = QFont()
        font.setFamilies([u"Yu Gothic UI"])
        font.setPointSize(14)
        self.ui.lError.setFont(font)
        self.ui.lError.setStyleSheet(u"color: red")
        self.ui.lError.setFixedSize(self.ui.frame.size().width() - 600, 20)
        self.ui.lError.move((self.ui.frame.width() - self.ui.lTitle.width()) // 2, 550)

        if self.ui.leUsername.text() == "":
            self.ui.lError.setText("Введите имя пользователя!")
            self.ui.lError.show()
            return
        else:
            UserInfo.name = self.ui.leUsername.text()

        if self.ui.lePassword.text() == "":
            self.ui.lError.setText("Введите пароль!")
            self.ui.lError.show()
            return
        else:
            UserInfo.passw = self.ui.lePassword.text()
        UserInfo.bio = self.ui.teBio.toPlainText()

        if UserInfo.imagePath == "":
            UserInfo.imagePath = BASE_DIR[:-8] + "/forms/res/profile-placeholder.png"

        if Register(UserInfo.name, UserInfo.passw, UserInfo.imagePath, UserInfo.bio) == True:
            self.mainName = UserInfo.name
            self.MainPage()
        else:
            self.ui.lError.setText("Такой ник уже используется")
            self.ui.lError.show()


    def MainPage(self):
        self.ui = Ui_MainPage()
        self.SetUp()
        info = getProfileInfo(self.mainName)

        UserInfo.name = info[1]
        UserInfo.passw = info[2]
        UserInfo.imagePath = BASE_DIR[:-8] + "media/profileImage.jpg"
        write_to_file(info[3], BASE_DIR[:-8] + "media/profileImage.jpg")
        UserInfo.bio = info[4]
        UserInfo.subscribers = getSubscribers(info[1])
        UserInfo.subscriptions = getSubscriptions(info[1])
        temp = getPosts(UserInfo.name)
        UserInfo.posts.clear()
        for el in temp[0]:
            self.post.title = el[0]
            self.post.photoPath = el[1]
            self.post.description = el[2]
            UserInfo.posts.append(self.post)
            self.post = Post()

        temp = getPosts(UserInfo.name, True)
        UserInfo.favorites.clear()
        for el in temp[0]:
            self.post.title = el[0]
            self.post.photoPath = el[1]
            self.post.description = el[2]
            UserInfo.favorites.append(self.post)
            self.post = Post()
        self.ui = Ui_MainPage()
        self.SetUp()
        # self.post = Post()
        # self.post.title = info[7][0]
        # self.post.photoPath = info[7][1]
        # self.post.description = info[7][2]
        # UserInfo.posts.append(self.post)
        # UserInfo.favorites = info[8]

        mainFont = QFont()
        mainFont.setFamilies([u"Yu Gothic UI"])
        mainFont.setPointSize(16)

        subFont = QFont()
        subFont.setFamilies([u"Yu Gothic UI"])
        subFont.setPointSize(18)

        id = QFontDatabase.addApplicationFont(BASE_DIR[:-8] + "forms/res/BadScript-Regular.ttf")
        families = QFontDatabase.applicationFontFamilies(id)
        postFont = QFont(families[0], 14)

        # self.ui.frame.move(0, 20)
        # self.ui.frame.setFixedSize(self.width(), self.height() - 20)

        self.ui.fNavBar = QtWidgets.QFrame(self.ui.frame)
        self.ui.fNavBar.setObjectName(u"fNavBar")
        self.ui.fNavBar.setGeometry(QRect(0, 0, 300, self.ui.frame.height()))
        self.ui.fNavBar.setStyleSheet("background-color: lightgray;\nborder-radius: 10px;\n")

        self.ui.fPosts = QFrame(self.ui.frame)
        self.ui.fPosts.setObjectName(u"fPosts")
        self.ui.fPosts.setGeometry(QRect(self.ui.frame.x() + 100, 10,
                                         self.ui.frame.x() + self.ui.frame.width() - 800, self.ui.frame.height()))
        self.ui.fPosts.setStyleSheet("background-color: white;\nborder-radius: 10px;\n")

        self.ui.fProfileInfo = QtWidgets.QFrame(self.ui.frame)
        self.ui.fProfileInfo.setObjectName(u"fProfileInfo")
        self.ui.fProfileInfo.setGeometry(QRect(self.ui.frame.width() - 300, 0,
                                               300, self.ui.frame.height()))
        self.ui.fProfileInfo.setStyleSheet("background-color: lightgray;\nborder-radius: 10px;\n")

        self.ui.pbMyProfile = QtWidgets.QPushButton(self.ui.fNavBar)
        self.ui.pbMyProfile.setObjectName(u"pbMyProfile")
        self.ui.pbMyProfile.setGeometry(QRect(20, 20, self.ui.fNavBar.width() - 40, 60))
        self.ui.pbMyProfile.setText("Профиль")
        self.ui.pbMyProfile.setFont(mainFont)
        self.ui.pbMyProfile.setStyleSheet(
            "QPushButton\n{\nborder: 3px solid gray;\nbackground-color: white;\nborder-radius: 10px;\n}\n"
            "QPushButton:hover\n{\nbackground-color: lightgray;\n}\n")

        self.ui.pbSearch = QtWidgets.QPushButton(self.ui.fNavBar)
        self.ui.pbSearch.setObjectName(u"pbSearch")
        self.ui.pbSearch.setGeometry(QRect(20, 100, self.ui.fNavBar.width() - 40, 60))
        self.ui.pbSearch.setText("Поиск")
        self.ui.pbSearch.setFont(mainFont)
        self.ui.pbSearch.setStyleSheet("QPushButton\n{\nborder: 3px solid gray;\nbackground-color: white;\nborder-radius: 10px;\n}\n"
                                       "QPushButton:hover\n{\nbackground-color: lightgray;\n}\n")

        self.ui.pbLikes = QtWidgets.QPushButton(self.ui.fNavBar)
        self.ui.pbLikes.setObjectName(u"pbLikes")
        self.ui.pbLikes.setGeometry(QRect(20, 180, self.ui.fNavBar.width() - 40, 60))
        self.ui.pbLikes.setText("Понравившиеся")
        self.ui.pbLikes.setFont(mainFont)
        self.ui.pbLikes.setStyleSheet(
            "QPushButton\n{\nborder: 3px solid gray;\nbackground-color: white;\nborder-radius: 10px;\n}\n"
            "QPushButton:hover\n{\nbackground-color: lightgray;\n}\n")

        self.ui.pbSettings = QtWidgets.QPushButton(self.ui.fNavBar)
        self.ui.pbSettings.setObjectName(u"pbSettings")
        self.ui.pbSettings.setGeometry(QRect(20, 260, self.ui.fNavBar.width() - 40, 60))
        self.ui.pbSettings.setText("Настройки")
        self.ui.pbSettings.setFont(mainFont)
        self.ui.pbSettings.setStyleSheet(
            "QPushButton\n{\nborder: 3px solid gray;\nbackground-color: white;\nborder-radius: 10px;\n}\n"
            "QPushButton:hover\n{\nbackground-color: lightgray;\n}\n")

        self.ui.lMyProfile = QtWidgets.QLabel(self.ui.fProfileInfo)
        self.ui.lMyProfile.setObjectName(u"lMyProfile")
        self.ui.lMyProfile.setGeometry(QRect(20, 20, self.ui.fProfileInfo.width() - 40, 60))
        self.ui.lMyProfile.setAlignment(Qt.AlignCenter)
        self.ui.lMyProfile.setText("Мой профиль")
        self.ui.lMyProfile.setFont(mainFont)

        self.ui.lProfileImage = QLabel(self.ui.fProfileInfo)
        self.ui.lProfileImage.setObjectName(u"lProfileImage")
        self.ui.lProfileImage.setGeometry(QRect(75, 75, 150, 150))
        self.target = QPixmap(self.ui.lProfileImage.size())
        self.target.fill(Qt.transparent)
        write_to_file(getProfileInfo(UserInfo.name)[3], BASE_DIR[:-8] + "media/profileImage.jpg")
        p = QPixmap(BASE_DIR[:-8] + "media/profileImage.jpg").scaled(
            self.ui.lProfileImage.width(), self.ui.lProfileImage.height(),
            Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        painter = QPainter(self.target)
        path = QPainterPath()
        path.addRoundedRect(
            0, 0, self.ui.lProfileImage.width(), self.ui.lProfileImage.height(), 75, 75)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, p)
        self.ui.lProfileImage.setPixmap(self.target)

        self.ui.lSubscribers = QtWidgets.QLabel(self.ui.fProfileInfo)
        self.ui.lSubscribers.setObjectName(u"lSubscribers")
        self.ui.lSubscribers.setGeometry(QRect(20, 250, self.ui.fProfileInfo.width() - 40, 40))
        self.ui.lSubscribers.setText("Подписчики: " + str(len(UserInfo.subscribers)))
        self.ui.lSubscribers.setFont(mainFont)
        self.ui.lSubscribers.setStyleSheet("color: white;\nbackground-color: gray;\nborder-radius: 10px;\npadding: 5px;\n")

        self.ui.lSubscriptions = QtWidgets.QLabel(self.ui.fProfileInfo)
        self.ui.lSubscriptions.setObjectName(u"lSubscriptions")
        self.ui.lSubscriptions.setGeometry(QRect(20, 300, self.ui.fProfileInfo.width() - 40, 40))
        self.ui.lSubscriptions.setText("Подписки: " + str(len(UserInfo.subscriptions)))
        self.ui.lSubscriptions.setFont(mainFont)
        self.ui.lSubscriptions.setStyleSheet("color: white;\nbackground-color: gray;\nborder-radius: 10px;\npadding: 5px;\n")

        if len(UserInfo.posts):
            x = 60
            y = 60
            w = self.ui.fPosts.width() - 120
            h = self.ui.fPosts.width() - 80
            dx = w + 40
            dy = h + 20
            for i in range(len(UserInfo.posts)):
                self.ui.fPost = QFrame(self.ui.fPosts)
                self.ui.fPost.setObjectName(u"fPost" + str(i))
                self.ui.fPost.setGeometry(x, y + i * dy, w, h)
                self.ui.fPost.setStyleSheet("background: lightgray;")

                self.ui.lPostImage = QLabel(self.ui.fPost)
                self.ui.lPostImage.setObjectName(u"lPostImage")
                self.ui.lPostImage.setGeometry(10, 10, self.ui.fPost.width() - 20, self.ui.fPost.width() - 20)
                self.ui.lPostImage.setPixmap(QPixmap(UserInfo.posts[i].photoPath))

                self.ui.lPostTitle = QLabel(self.ui.fPost)
                self.ui.lPostTitle.setObjectName(u"lPostTitle")
                self.ui.lPostTitle.setGeometry(5, h - 30, w - 45, 25)
                self.ui.lPostTitle.setAlignment(Qt.AlignLeft | Qt.AlignCenter)
                self.ui.lPostTitle.setFont(postFont)
                self.ui.lPostTitle.setStyleSheet("color: black;")
                self.ui.lPostTitle.setText(UserInfo.posts[i].title)

                self.ui.pbLike = QPushButton(self.ui.fPost)
                self.ui.pbLike.setObjectName(str(i))
                self.ui.pbLike.setGeometry(w - 35, h - 35, 30, 30)

                if not UserInfo.posts[i].isLiked:
                    self.ui.pbLike.setIcon(QPixmap(BASE_DIR[:-8] + "forms/res/heart-50.png"))
                else:
                    self.ui.pbLike.setIcon(QPixmap(BASE_DIR[:-8] + "forms/res/red-heart-64.png"))
                # self.ui.pbLike.setStyleSheet("background-color: black;")
                self.ui.pbLike.setIconSize(QSize(30, 30))
                self.ui.pbLike.clicked.connect(self.like)

                self.ui.lPostDescription = QLabel(self.ui.fPost)
                self.ui.lPostDescription.setObjectName(u"lPostDescription")
                self.ui.lPostDescription.setGeometry(5, 5, self.ui.fPost.width() - 10, self.ui.fPost.width() - 10)
                self.ui.lPostDescription.setAlignment(Qt.AlignCenter)
                self.ui.lPostDescription.setFont(postFont)
                self.ui.lPostDescription.setStyleSheet("color: black;")
                self.ui.lPostDescription.setText(UserInfo.posts[i].description)
                self.ui.lPostDescription.hide()

        self.ui.lTitle = QLabel(self.ui.fPosts)
        self.ui.lTitle.setAlignment(Qt.AlignCenter)
        self.ui.lTitle.setFont(subFont)
        self.ui.lTitle.setText("Лента")
        self.ui.lTitle.setFixedSize(300, 40)
        self.ui.lTitle.setStyleSheet("color: black; border: 3px solid gray")
        self.ui.lTitle.move((self.ui.fPosts.width() - self.ui.lTitle.width()) // 2, 10)

        self.ui.pbMyProfile.pressed.connect(self.ProfilePage)
        self.ui.pbSearch.pressed.connect(self.Search)
        self.ui.pbLikes.pressed.connect(self.Favorites)
        self.ui.pbSettings.pressed.connect(self.Settings)


    def ProfilePage(self, username = ""):
        if username == "":
            info = getProfileInfo(self.mainName)
        else:
            info = getProfileInfo(username)
        UserInfo.name = info[1]
        UserInfo.imagePath = BASE_DIR[:-8] + "media/UserProfileImage.jpg"
        write_to_file(info[3], UserInfo.imagePath)
        UserInfo.bio = info[4]
        UserInfo.subscribers = getSubscribers(info[1])
        UserInfo.subscriptions = getSubscriptions(info[1])
        temp = getPosts(UserInfo.name)
        UserInfo.posts.clear()
        for el in temp[0]:
            self.post.title = el[0]
            self.post.photoPath = el[1]
            self.post.description = el[2]
            UserInfo.posts.append(self.post)
            self.post = Post()

        temp = getPosts(UserInfo.name, True)
        UserInfo.favorites.clear()
        for el in temp[0]:
            self.post.title = el[0]
            self.post.photoPath = el[1]
            self.post.description = el[2]
            UserInfo.favorites.append(self.post)
            self.post = Post()
        self.ui = Ui_MainPage()
        self.SetUp()

        mainFont = QFont()
        mainFont.setFamilies([u"Yu Gothic UI"])
        mainFont.setPointSize(16)

        subFont = QFont()
        subFont.setFamilies([u"Yu Gothic UI"])
        subFont.setPointSize(18)

        miniFont = QFont()
        miniFont.setFamilies([u"Yu Gothic UI"])
        miniFont.setPointSize(14)

        id = QFontDatabase.addApplicationFont(BASE_DIR[:-8] + "forms/res/BadScript-Regular.ttf")
        families = QFontDatabase.applicationFontFamilies(id)
        postFont = QFont(families[0], 14)

        # self.ui.frame.move(0, 20)
        # self.ui.frame.setFixedSize(self.width(), self.height() - 20)

        self.ui.fProfileInfo = QtWidgets.QFrame(self.ui.frame)
        self.ui.fProfileInfo.setObjectName(u"fProfileInfo")
        self.ui.fProfileInfo.setGeometry(QRect(self.ui.frame.x() - 100, self.ui.frame.y() - 50,
                                               self.ui.frame.width() - 200, self.ui.frame.height() // 2 - 75))
        self.ui.fProfileInfo.setStyleSheet("background-color: lightgray;\nborder-radius: 10px;\n")

        self.ui.fPosts = QtWidgets.QFrame(self.ui.frame)
        self.ui.fPosts.setObjectName(u"fPosts")
        self.ui.fPosts.setGeometry(QRect(self.ui.frame.x() - 100, self.ui.frame.y() + self.ui.frame.height() // 2 - 100,
                                            self.ui.frame.width() - 200, self.ui.frame.height() // 2))
        self.ui.fPosts.setStyleSheet("background-color: lightgray;\nborder-radius: 10px;\n")

        self.ui.pbMyProfile = QPushButton(self.ui.frame)
        self.ui.pbMyProfile.setObjectName(u"pbMyProfile")
        self.ui.pbMyProfile.setFixedSize(200, 40)
        self.ui.pbMyProfile.move((self.ui.frame.width() - self.ui.pbMyProfile.width()) // 2, 10)
        self.ui.pbMyProfile.setFont(subFont)
        if username == "":
            self.ui.pbMyProfile.setText("Мой профиль")
        else:
            self.ui.pbMyProfile.setText("Профиль пользователя")
            self.ui.pbMyProfile.setFixedWidth(300)
        # self.ui.pbMyProfile.setAlignment(Qt.AlignCenter)

        self.ui.lProfilePhoto = QLabel(self.ui.fProfileInfo)
        self.ui.lProfilePhoto.setObjectName(u"lProfilePhoto")
        self.ui.lProfilePhoto.setGeometry(50, 50, 200, 200)
        self.ui.lProfilePhoto.setStyleSheet("background-color: gray;\nborder-radius: 100px")
        self.target = QPixmap(self.ui.lProfilePhoto.size())
        self.target.fill(Qt.transparent)
        p = QPixmap(UserInfo.imagePath).scaled(
            self.ui.lProfilePhoto.width(), self.ui.lProfilePhoto.height(),
            Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        painter = QPainter(self.target)
        path = QPainterPath()
        path.addRoundedRect(
            0, 0, self.ui.lProfilePhoto.width(), self.ui.lProfilePhoto.height(), 100, 100)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, p)
        self.ui.lProfilePhoto.setPixmap(self.target)

        self.ui.lProfileName = QLabel(self.ui.fProfileInfo)
        self.ui.lProfileName.setObjectName(u"lProfileName")
        self.ui.lProfileName.setGeometry(350, 20, 250, 50)
        self.ui.lProfileName.setStyleSheet("background-color: gray; padding: 10px; color: white")
        self.ui.lProfileName.setFont(mainFont)
        self.ui.lProfileName.setText(UserInfo.name)

        self.ui.lProfileBio = QLabel(self.ui.fProfileInfo)
        self.ui.lProfileBio.setObjectName(u"lProfileBio")
        self.ui.lProfileBio.setGeometry(350, 80, 450, 200)
        self.ui.lProfileBio.setStyleSheet("background-color: gray; padding: 10px; color: white")
        self.ui.lProfileBio.setFont(miniFont)
        self.ui.lProfileBio.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.ui.lProfileBio.setText(UserInfo.bio)

        self.ui.lProfileSubscribers = QLabel(self.ui.fProfileInfo)
        self.ui.lProfileSubscribers.setObjectName(u"lProfileSubscribers")
        self.ui.lProfileSubscribers.setGeometry(630, 20, 170, 22)
        self.ui.lProfileSubscribers.setStyleSheet("background-color: gray; padding: auto 5px; color: white")
        self.ui.lProfileSubscribers.setFont(miniFont)
        self.ui.lProfileSubscribers.setText("Подписчики: " + str(len(UserInfo.subscribers)))

        self.ui.lProfileSubscriptions = QLabel(self.ui.fProfileInfo)
        self.ui.lProfileSubscriptions.setObjectName(u"lProfileSubscriptions")
        self.ui.lProfileSubscriptions.setGeometry(630, 48, 170, 22)
        self.ui.lProfileSubscriptions.setStyleSheet("background-color: gray; padding: auto 5px; color: white")
        self.ui.lProfileSubscriptions.setFont(miniFont)
        self.ui.lProfileSubscriptions.setText("Подписки: " + str(len(UserInfo.subscriptions)))

        self.ui.pbHome = QPushButton(self.ui.fProfileInfo)
        self.ui.pbHome.setObjectName(u"pbHome")
        self.ui.pbHome.setGeometry(self.ui.fProfileInfo.width() - 70, 50, 50, 50)
        self.ui.pbHome.setStyleSheet("QPushButton\n{\nbackground-color: white;\n}\n"
                                     "QPushButton:hover\n{\nborder: 3px solid black;\n}\n")
        self.ui.pbHome.setIcon(QPixmap(BASE_DIR[:-8] + "forms/res/home-50.png"))
        self.ui.pbHome.setIconSize(QSize(45, 45))

        if username == "":
            self.ui.pbSettings = QPushButton(self.ui.fProfileInfo)
            self.ui.pbSettings.setObjectName(u"pbSettings")
            self.ui.pbSettings.setGeometry(self.ui.fProfileInfo.width() - 70, 120, 50, 50)
            self.ui.pbSettings.setStyleSheet("QPushButton\n{\nbackground-color: white;\n}\n"
                                             "QPushButton:hover\n{\nborder: 3px solid black;\n}\n")
            self.ui.pbSettings.setIcon(QPixmap(BASE_DIR[:-8] + "forms/res/settings-50.png"))
            self.ui.pbSettings.setIconSize(QSize(45, 45))

            self.ui.pbNewPost = QPushButton(self.ui.fProfileInfo)
            self.ui.pbNewPost.setObjectName(u"pbNewPost")
            self.ui.pbNewPost.setGeometry(self.ui.fProfileInfo.width() - 70, 190, 50, 50)
            self.ui.pbNewPost.setStyleSheet("QPushButton\n{\nbackground-color: white;\n}\n"
                                             "QPushButton:hover\n{\nborder: 3px solid black;\n}\n")
            self.ui.pbNewPost.setIcon(QPixmap(BASE_DIR[:-8] + "forms/res/plus-50.png"))
            self.ui.pbNewPost.setIconSize(QSize(45, 45))
        else:
            self.ui.pbSubscribe = QPushButton(self.ui.fProfileInfo)
            self.ui.pbSubscribe.setObjectName(u"pbSubscribe")
            self.ui.pbSubscribe.setGeometry(self.ui.fProfileInfo.width() - 70, 120, 50, 50)
            self.ui.pbSubscribe.setStyleSheet("QPushButton\n{\nbackground-color: white;\n}\n"
                                             "QPushButton:hover\n{\nborder: 3px solid black;\n}\n")
            flag = False
            for el in UserInfo.subscribers:
                if el == self.mainName:
                    flag = True
            if flag:
                self.ui.pbSubscribe.setIcon(QPixmap(BASE_DIR[:-8] + "forms/res/tick-50.png"))
            else:
                self.ui.pbSubscribe.setIcon(QPixmap(BASE_DIR[:-8] + "forms/res/add-friends-50.png"))
            self.ui.pbSubscribe.setIconSize(QSize(45, 45))

        if len(UserInfo.posts):
            x = 20
            y = 20
            w = self.ui.fPosts.width() // 3 - 40
            h = self.ui.fPosts.width() // 3
            dx = w + 40
            dy = h + 20
            for i in range(len(UserInfo.posts)):
                self.ui.fPost = QFrame(self.ui.fPosts)
                self.ui.fPost.setObjectName(u"fPost" + str(i))
                self.ui.fPost.setGeometry(x + (i % 3) * dx, y + (i // 3) * dy, w, h)
                self.ui.fPost.setStyleSheet("background: white;")

                self.ui.lPostImage = QLabel(self.ui.fPost)
                self.ui.lPostImage.setGeometry(5, 5, self.ui.fPost.width() - 10, self.ui.fPost.width() - 10)
                self.ui.lPostImage.setPixmap(QPixmap(UserInfo.posts[i].photoPath))

                self.ui.lPostTitle = QLabel(self.ui.fPost)
                self.ui.lPostTitle.setGeometry(5, h - 30, w - 45, 25)
                self.ui.lPostTitle.setAlignment(Qt.AlignLeft | Qt.AlignCenter)
                self.ui.lPostTitle.setFont(postFont)
                self.ui.lPostTitle.setStyleSheet("color: black;")
                self.ui.lPostTitle.setText(UserInfo.posts[i].title)

                self.ui.pbLike = QPushButton(self.ui.fPost)
                self.ui.pbLike.setObjectName(str(i))
                self.ui.pbLike.setGeometry(w - 35, h - 35, 30, 30)

                if not UserInfo.posts[i].isLiked:
                    self.ui.pbLike.setIcon(QPixmap(BASE_DIR[:-8] + "forms/res/heart-50.png"))
                else:
                    self.ui.pbLike.setIcon(QPixmap(BASE_DIR[:-8] + "forms/res/red-heart-64.png"))
                # self.ui.pbLike.setStyleSheet("background-color: black;")
                self.ui.pbLike.setIconSize(QSize(30, 30))
                self.ui.pbLike.clicked.connect(self.like)

                self.ui.lPostDescription = QLabel(self.ui.fPost)
                self.ui.lPostDescription.setGeometry(5, 5, self.ui.fPost.width() - 10, self.ui.fPost.width() - 10)
                self.ui.lPostDescription.setAlignment(Qt.AlignCenter)
                self.ui.lPostDescription.setFont(postFont)
                self.ui.lPostDescription.setStyleSheet("color: black;")
                self.ui.lPostDescription.setText(UserInfo.posts[i].description)
                self.ui.lPostDescription.hide()

                print(UserInfo.posts[i].photoPath)
        else:
            self.ui.lHaventPosts = QLabel(self.ui.fPosts)
            self.ui.lHaventPosts.setObjectName(u"lHaventPosts")
            self.ui.lHaventPosts.setFixedSize(400, 50)
            self.ui.lHaventPosts.move((self.ui.fPosts.width() - self.ui.lHaventPosts.width()) // 2,
                                      (self.ui.fPosts.height() - self.ui.lHaventPosts.height()) // 2 - 100)
            self.ui.lHaventPosts.setAlignment(Qt.AlignCenter)
            self.ui.lHaventPosts.setStyleSheet("color: black;")
            self.ui.lHaventPosts.setFont(subFont)
            if username == "":
                self.ui.lHaventPosts.setText("У вас пока что нет постов")
            else:
                self.ui.lHaventPosts.setText("У пользователя пока что нет постов")

            self.ui.lSadSmile = QLabel(self.ui.fPosts)
            self.ui.lSadSmile.setObjectName(u"lSadSmile")
            self.ui.lSadSmile.setFixedSize(100, 100)
            self.ui.lSadSmile.move((self.ui.fPosts.width() - self.ui.lSadSmile.width()) // 2,
                                   (self.ui.fPosts.height() - self.ui.lSadSmile.height()) // 2)
            self.ui.lSadSmile.setPixmap(QPixmap(BASE_DIR[:-8] + "forms/res/sad-50.png"))
            self.ui.lSadSmile.setAlignment(Qt.AlignCenter)
        self.ui.pbHome.pressed.connect(self.MainPage)
        if username == "":
            self.ui.pbSettings.pressed.connect(self.Settings)
            self.ui.pbNewPost.pressed.connect(self.AddPost)
        else:
            self.ui.pbSubscribe.pressed.connect(self.Subscribe)
        # self.ui.pbMyProfile.pressed.connect(self.MoveBack)


    def Subscribe(self):
        flag = False
        for el in UserInfo.subscribers:
            if el == self.mainName:
                flag = True
        if flag:
            unsubscribe(self.mainName, UserInfo.name)
        else:
            subscribe(self.mainName, UserInfo.name)
        self.ProfilePage(UserInfo.name)


    def like(self):
        sndr = self.sender()
        for i in range(len(UserInfo.posts)):
            if i == int(sndr.objectName()):
                if not UserInfo.posts[i].isLiked:
                    sndr.setIcon(QPixmap(BASE_DIR[:-8] + "forms/res/red-heart-64.png"))
                    addPost(self.mainName, [sndr.parent().children()[0].text(),
                                            sndr.parent().children()[1].text(),
                                            sndr.parent().children()[3].text()], True)
                    UserInfo.posts[i].isLiked = True
                else:
                    sndr.setIcon(QPixmap(BASE_DIR[:-8] + "forms/res/heart-50.png"))
                    UserInfo.posts[i].isLiked = False
                    temp = []
                    for el in UserInfo.posts:
                        if el.isLiked:
                            temp.append(el)
                    # addPosts(self.mainName, el, True)



    def mousePressEvent(self, event):
        oName = QObject()
        try:
            oName = self.children()[1].children()[0].children()[1]
            print(oName)
        except Exception:
            pass
        if oName.objectName() == u"fPosts":
            # print(event.pos())

            for i in range(len(UserInfo.posts)):
                post = oName.children()[i]
                print(post)
                ax = post.mapToGlobal(QPoint(0, 0)).x()
                ay = post.mapToGlobal(QPoint(0, 0)).y()
                w = post.width()
                h = post.height()

                print(post.children())

                lx = post.children()[2].mapToGlobal(QPoint(0, 0)).x()
                ly = post.children()[2].mapToGlobal(QPoint(0, 0)).y()
                lw = post.children()[2].width()
                lh = post.children()[2].height()

                if ax <= event.pos().x() <= ax + w and ay <= event.pos().y() <= ay + h \
                and not(lx <= event.pos().x() <= lx + lw and ly <= event.pos().y() <= ly + lh):
                    x = post.x()
                    for j in range(w, 0, -5):
                        post.move(x + (w - j) // 2, post.y())
                        post.setFixedSize(j, post.height())
                        self.app.processEvents()
                        time.sleep(.02)
                    if post.children()[0].isHidden():
                        print(post.children())
                        post.children()[0].show()
                        post.children()[1].show()
                        post.children()[2].show()
                        post.children()[3].hide()
                    else:
                        post.children()[0].hide()
                        post.children()[1].hide()
                        post.children()[2].hide()
                        post.children()[3].show()
                    self.app.processEvents()
                    for j in range(0, w, 5):
                        post.move(x + (w - j) // 2, post.y())
                        post.setFixedSize(j, post.height())
                        self.app.processEvents()
                        time.sleep(.02)
                    post.move(x, post.y())
                    post.setFixedSize(w, post.height())
                    self.app.processEvents()


    '''
    def MoveBack(self):
        delta = (self.ui.frame.y() - 50) - self.ui.fProfileInfo.y()
        y1 = self.ui.fProfileInfo.y()
        y2 = self.ui.fPosts.y()

        for i in range(y1, y1 + delta, 10):
            self.ui.fProfileInfo.move(self.ui.fProfileInfo.x(), i)
            self.ui.fPosts.move(self.ui.fPosts.x(), i - y1 + y2)
            self.app.processEvents()
            time.sleep(.02)

        self.ui.fProfileInfo.move(self.ui.fProfileInfo.x(), y1 + delta)
        self.ui.fPosts.move(self.ui.fPosts.x(), y2 + delta)
    '''


    def wheelEvent(self, event):
        oName = QObject()
        flag = True
        try:
            oName = self.children()[1].children()[0].children()
        except Exception:
            pass
        if oName[2].objectName() == "fProfileInfo":
            flag = False
        oName = oName[1]
        if oName.objectName() == u"fPosts":
            dy = event.angleDelta().y() // 4
            if flag:
                if self.ui.fProfileInfo.y() + dy > self.ui.frame.y() - 50 or \
                        self.ui.fPosts.height() - dy > 20 + (1 + len(UserInfo.posts) // 3) * (self.ui.fPosts.width() // 3 + 20):
                    return
                self.ui.fProfileInfo.move(self.ui.fProfileInfo.x(), self.ui.fProfileInfo.y() + dy)
            else:
                if self.ui.fPosts.height() - dy > 20 + len(UserInfo.posts) * (self.ui.fPost.height() + 20) \
                or self.ui.lTitle.y() + dy > 20:
                    return
                self.ui.lTitle.move(self.ui.lTitle.x(), self.ui.lTitle.y() + dy)
            self.ui.fPosts.move(self.ui.fPosts.x(), self.ui.fPosts.y() + dy)
            self.ui.fPosts.setFixedSize(self.ui.fPosts.width(), self.ui.fPosts.height() - dy)


    def Search(self):
        self.ui = Ui_MainPage()
        self.SetUp()

        titleFont = QFont()
        titleFont.setFamilies([u"Yu Gothic UI"])
        titleFont.setPointSize(24)

        mainFont = QFont()
        mainFont.setFamilies([u"Yu Gothic UI"])
        mainFont.setPointSize(16)

        subFont = QFont()
        subFont.setFamilies([u"Yu Gothic UI"])
        subFont.setPointSize(18)

        miniFont = QFont()
        miniFont.setFamilies([u"Yu Gothic UI"])
        miniFont.setPointSize(14)

        self.ui.lTitle = QLabel(self.ui.frame)
        self.ui.lTitle.setObjectName(u"lTitle")
        self.ui.lTitle.setFixedSize(300, 60)
        self.ui.lTitle.move((self.ui.frame.width() - self.ui.lTitle.width()) // 2, 20)
        self.ui.lTitle.setFont(subFont)
        self.ui.lTitle.setAlignment(Qt.AlignCenter)
        self.ui.lTitle.setText("Поиск пользователя")
        self.ui.lTitle.setStyleSheet("border: 5px solid gray")

        self.ui.leSearch = QLineEdit(self.ui.frame)
        self.ui.leSearch.setObjectName(u"leSearch")
        self.ui.leSearch.setGeometry(50, 100, self.ui.frame.width() - 180, 60)
        self.ui.leSearch.setFont(mainFont)
        self.ui.leSearch.setStyleSheet("border: 3px solid lightgray; padding: 5px")
        self.ui.leSearch.setPlaceholderText("Имя пользователя")

        self.ui.pbSearch = QPushButton(self.ui.frame)
        self.ui.pbSearch.setObjectName(u"pbSearch")
        self.ui.pbSearch.setGeometry(self.ui.frame.width() - 110, 100, 60, 60)
        self.ui.pbSearch.setStyleSheet("QPushButton\n{\nbackground-color: lightgray;\n}\n"
                                       "QPushButton:hover\n{\nborder: 3px solid black;\n}\n")
        self.ui.pbSearch.setIcon(QPixmap(BASE_DIR[:-8] + "forms/res/search-50.png"))
        self.ui.pbSearch.setIconSize(QSize(60, 60))

        self.ui.fUsers = QFrame(self.ui.frame)
        self.ui.fUsers.setObjectName(u"fUsers")
        self.ui.fUsers.setGeometry(50, 200, self.ui.frame.width() - 100, self.ui.frame.height() - 300)
        self.ui.fUsers.setStyleSheet("background-color: lightgray;")

        self.ui.lRequest = QLabel(self.ui.fUsers)
        self.ui.lRequest.setFixedSize(400, 60)
        self.ui.lRequest.move((self.ui.fUsers.width() - self.ui.lRequest.width()) // 2, 20)
        self.ui.lRequest.setFont(subFont)
        self.ui.lRequest.setAlignment(Qt.AlignCenter)
        self.ui.lRequest.setText("Пользователи не найдены")
        self.ui.lRequest.setStyleSheet("border: 5px solid gray; color: black")
        self.ui.lRequest.hide()

        self.ui.pbUser = QPushButton(self.ui.fUsers)
        self.ui.pbUser.setGeometry(50, 50, self.ui.fUsers.width() - 100, 40)
        self.ui.pbUser.setStyleSheet("background-color: white; border: solid 5px gray")
        self.ui.pbUser.setFont(mainFont)
        self.ui.pbUser.setDisabled(True)
        self.ui.pbUser.hide()

        self.ui.pbHome = QPushButton(self.ui.frame)
        self.ui.pbHome.setObjectName(u"pbHome")
        self.ui.pbHome.setGeometry(50, self.ui.frame.height() - 70, self.ui.frame.width() - 100, 50)
        self.ui.pbHome.setStyleSheet("QPushButton\n{\nbackground-color: lightgray;\n}\n"
                                     "QPushButton:hover\n{\nborder: 3px solid black;\n}\n")
        self.ui.pbHome.setFont(subFont)
        self.ui.pbHome.setText("На главную")

        self.ui.pbHome.clicked.connect(self.MainPage)
        self.ui.pbSearch.clicked.connect(self.FindUser)
        self.ui.pbUser.clicked.connect(self.SetUser)


    def SetUser(self):
        self.ProfilePage(self.ui.pbUser.text())


    def FindUser(self):
        if Find(self.ui.leSearch.text()) and self.ui.leSearch.text() != UserInfo.name:
            self.ui.pbUser.setDisabled(False)
            self.ui.pbUser.show()
            self.ui.pbUser.setText(self.ui.leSearch.text())
            self.ui.lRequest.hide()
        else:
            self.ui.lRequest.show()
            self.ui.pbUser.hide()


    def Favorites(self):
        temp = getPosts(UserInfo.name, True)
        UserInfo.favorites.clear()
        for el in temp[0]:
            self.post.title = el[0]
            self.post.photoPath = el[1]
            self.post.description = el[2]
            UserInfo.favorites.append(self.post)
            self.post = Post()

        self.ui = Ui_MainPage()
        self.SetUp()


        titleFont = QFont()
        titleFont.setFamilies([u"Yu Gothic UI"])
        titleFont.setPointSize(24)

        mainFont = QFont()
        mainFont.setFamilies([u"Yu Gothic UI"])
        mainFont.setPointSize(16)

        subFont = QFont()
        subFont.setFamilies([u"Yu Gothic UI"])
        subFont.setPointSize(18)

        miniFont = QFont()
        miniFont.setFamilies([u"Yu Gothic UI"])
        miniFont.setPointSize(14)

        id = QFontDatabase.addApplicationFont(BASE_DIR[:-8] + "forms/res/BadScript-Regular.ttf")
        families = QFontDatabase.applicationFontFamilies(id)
        postFont = QFont(families[0], 14)

        self.ui.lTitle = QLabel(self.ui.frame)
        self.ui.lTitle.setObjectName(u"lTitle")
        self.ui.lTitle.setFixedSize(350, 60)
        self.ui.lTitle.move((self.ui.frame.width() - self.ui.lTitle.width()) // 2, 20)
        self.ui.lTitle.setFont(subFont)
        self.ui.lTitle.setAlignment(Qt.AlignCenter)
        self.ui.lTitle.setText("Понравившиеся публикации")
        self.ui.lTitle.setStyleSheet("border: 5px solid gray")

        self.ui.fPosts = QFrame(self.ui.frame)
        self.ui.fPosts.setObjectName(u"fPosts")
        self.ui.fPosts.setGeometry(50, 100, self.ui.frame.width() - 100, self.ui.frame.height() - 200)
        self.ui.fPosts.setStyleSheet("background-color: lightgray;")

        if len(UserInfo.favorites):
            x = 20
            y = 20
            w = self.ui.fPosts.width() // 3 - 40
            h = self.ui.fPosts.width() // 3
            dx = w + 40
            dy = h + 20
            for i in range(len(UserInfo.posts)):
                self.ui.fPost = QFrame(self.ui.fPosts)
                self.ui.fPost.setObjectName(u"fPost" + str(i))
                self.ui.fPost.setGeometry(x + (i % 3) * dx, y + (i // 3) * dy, w, h)
                self.ui.fPost.setStyleSheet("background: white;")

                self.ui.lPostImage = QLabel(self.ui.fPost)
                self.ui.lPostImage.setGeometry(5, 5, self.ui.fPost.width() - 10, self.ui.fPost.width() - 10)
                self.ui.lPostImage.setPixmap(QPixmap(UserInfo.posts[i].photoPath))

                self.ui.lPostTitle = QLabel(self.ui.fPost)
                self.ui.lPostTitle.setGeometry(5, h - 30, self.ui.fPost.width() - 10, 25)
                self.ui.lPostTitle.setAlignment(Qt.AlignCenter)
                self.ui.lPostTitle.setFont(postFont)
                self.ui.lPostTitle.setStyleSheet("color: black;")
                self.ui.lPostTitle.setText(UserInfo.posts[i].title)

                self.ui.lPostDescription = QLabel(self.ui.fPost)
                self.ui.lPostDescription.setGeometry(5, 5, self.ui.fPost.width() - 10, self.ui.fPost.width() - 10)
                self.ui.lPostDescription.setAlignment(Qt.AlignCenter)
                self.ui.lPostDescription.setFont(postFont)
                self.ui.lPostDescription.setStyleSheet("color: black;")
                self.ui.lPostDescription.setText(UserInfo.posts[i].description)
                self.ui.lPostDescription.hide()
        else:
            self.ui.lHaventPosts = QLabel(self.ui.fPosts)
            self.ui.lHaventPosts.setObjectName(u"lHaventPosts")
            self.ui.lHaventPosts.setFixedSize(550, 50)
            self.ui.lHaventPosts.move((self.ui.fPosts.width() - self.ui.lHaventPosts.width()) // 2,
                                      (self.ui.fPosts.height() - self.ui.lHaventPosts.height()) // 2 - 100)
            self.ui.lHaventPosts.setAlignment(Qt.AlignCenter)
            self.ui.lHaventPosts.setStyleSheet("color: black;")
            self.ui.lHaventPosts.setFont(subFont)
            self.ui.lHaventPosts.setText("У вас пока что нет понравившихся публикаций")

            self.ui.lSadSmile = QLabel(self.ui.fPosts)
            self.ui.lSadSmile.setObjectName(u"lSadSmile")
            self.ui.lSadSmile.setFixedSize(100, 100)
            self.ui.lSadSmile.move((self.ui.fPosts.width() - self.ui.lSadSmile.width()) // 2,
                                   (self.ui.fPosts.height() - self.ui.lSadSmile.height()) // 2)
            self.ui.lSadSmile.setPixmap(QPixmap(BASE_DIR[:-8] + "forms/res/sad-50.png"))
            self.ui.lSadSmile.setAlignment(Qt.AlignCenter)

        self.ui.pbHome = QPushButton(self.ui.frame)
        self.ui.pbHome.setObjectName(u"pbHome")
        self.ui.pbHome.setGeometry(50, self.ui.frame.height() - 70, self.ui.frame.width() - 100, 50)
        self.ui.pbHome.setStyleSheet("QPushButton\n{\nbackground-color: lightgray;\n}\n"
                                     "QPushButton:hover\n{\nborder: 3px solid black;\n}\n")
        self.ui.pbHome.setFont(subFont)
        self.ui.pbHome.setText("На главную")

        self.ui.pbHome.clicked.connect(self.MainPage)


    def Settings(self):
        self.ui = Ui_MainPage()
        self.SetUp()

        titleFont = QFont()
        titleFont.setFamilies([u"Yu Gothic UI"])
        titleFont.setPointSize(24)

        mainFont = QFont()
        mainFont.setFamilies([u"Yu Gothic UI"])
        mainFont.setPointSize(16)

        subFont = QFont()
        subFont.setFamilies([u"Yu Gothic UI"])
        subFont.setPointSize(18)

        miniFont = QFont()
        miniFont.setFamilies([u"Yu Gothic UI"])
        miniFont.setPointSize(14)

        self.ui.lTitle = QLabel(self.ui.frame)
        self.ui.lTitle.setObjectName(u"lTitle")
        self.ui.lTitle.setFixedSize(350, 60)
        self.ui.lTitle.move((self.ui.frame.width() - self.ui.lTitle.width()) // 2, 20)
        self.ui.lTitle.setFont(subFont)
        self.ui.lTitle.setAlignment(Qt.AlignCenter)
        self.ui.lTitle.setText("Настройки профиля")
        self.ui.lTitle.setStyleSheet("border: 5px solid gray")

        self.ui.fSettings = QFrame(self.ui.frame)
        self.ui.fSettings.setObjectName(u"fSettings")
        self.ui.fSettings.setGeometry(50, 100, self.ui.frame.width() - 100, self.ui.frame.height() - 200)
        self.ui.fSettings.setStyleSheet("background-color: lightgray;")

        self.ui.pbSetImage = QPushButton(self.ui.fSettings)
        self.ui.pbSetImage.setObjectName(u"pbSetImage")
        self.ui.pbSetImage.setStyleSheet("QPushButton\n{\nbackground-color: white; border-radius: 75px; border: 3px solid #B4B4B4;\n}\n"
                                         "QPushButton:hover\n{\nborder: 3px solid gray\n}\n")
        self.ui.pbSetImage.setFixedSize(150, 150)
        self.ui.pbSetImage.move((self.ui.fSettings.width() - self.ui.pbSetImage.width()) // 2, 20)

        self.ui.leUsername = QLineEdit(self.ui.fSettings)
        self.ui.leUsername.setObjectName(u"leUsername")
        self.ui.leUsername.setFixedSize(self.ui.fSettings.size().width() - 400, 40)
        self.ui.leUsername.move((self.ui.fSettings.width() - self.ui.leUsername.width()) // 2, 200)
        self.ui.leUsername.setFont(mainFont)
        self.ui.leUsername.setStyleSheet("background-color: white; border: 3px solid #B4B4B4; padding: 5px;")
        self.ui.leUsername.setPlaceholderText("Имя пользователя")

        self.ui.lePassword = QLineEdit(self.ui.fSettings)
        self.ui.lePassword.setObjectName(u"lePassword")
        self.ui.lePassword.setFixedSize(self.ui.fSettings.size().width() - 400, 40)
        self.ui.lePassword.move((self.ui.fSettings.width() - self.ui.lePassword.width()) // 2, 250)
        self.ui.lePassword.setFont(mainFont)
        self.ui.lePassword.setStyleSheet("background-color: white; border: 3px solid #B4B4B4; padding: 5px;")
        self.ui.lePassword.setPlaceholderText("Пароль")

        self.ui.teBio = QTextEdit(self.ui.fSettings)
        self.ui.teBio.setObjectName(u"teBio")
        self.ui.teBio.setFixedSize(self.ui.fSettings.size().width() - 400, 150)
        self.ui.teBio.move((self.ui.fSettings.width() - self.ui.teBio.width()) // 2, 300)
        self.ui.teBio.setFont(mainFont)
        self.ui.teBio.setStyleSheet("background-color: white; border: 3px solid #B4B4B4; padding: 5px;")
        self.ui.teBio.setPlaceholderText("О себе")

        self.ui.pbSaveChanges = QPushButton(self.ui.fSettings)
        self.ui.pbSaveChanges.setObjectName(u"pbSaveChanges")
        self.ui.pbSaveChanges.setGeometry(200, self.ui.fSettings.height() - 70, self.ui.fSettings.width() - 400, 50)
        self.ui.pbSaveChanges.setStyleSheet("QPushButton\n{\nbackground-color: white; border: 3px solid #B4B4B4;\n}\n"
                                            "QPushButton:hover\n{\nborder: 3px solid gray;\n}\n")
        self.ui.pbSaveChanges.setFont(subFont)
        self.ui.pbSaveChanges.setText("Применить изменения")

        self.ui.pbHome = QPushButton(self.ui.frame)
        self.ui.pbHome.setObjectName(u"pbHome")
        self.ui.pbHome.setGeometry(50, self.ui.frame.height() - 70, self.ui.frame.width() - 100, 50)
        self.ui.pbHome.setStyleSheet("QPushButton\n{\nbackground-color: lightgray;\n}\n"
                                     "QPushButton:hover\n{\nborder: 3px solid black;\n}\n")
        self.ui.pbHome.setFont(subFont)
        self.ui.pbHome.setText("На главную")

        self.ui.pbHome.clicked.connect(self.MainPage)
        self.ui.pbSetImage.clicked.connect(self.SetImage)
        self.ui.pbSaveChanges.clicked.connect(self.EditProfile)


    def EditProfile(self):
        info = getProfileInfo(UserInfo.name)
        login = self.ui.leUsername.text()
        passw = self.ui.lePassword.text()
        bio = self.ui.teBio.toPlainText()
        if login == "":
            login = info[1]
        else:
            UserInfo.name = login
        if passw == "":
            passw = info[2]
        if bio == "":
            bio = info[4]

        if editProfile(info[1], login, passw, bio) == False:
            mainFont = QFont()
            mainFont.setFamilies([u"Yu Gothic UI"])
            mainFont.setPointSize(16)
            self.ui.lError = QLabel(self.ui.fSettings)
            self.ui.lError.setGeometry(self.ui.pbSaveChanges.x(), self.ui.pbSaveChanges.y() - 40,
                                       self.ui.pbSaveChanges.width(), 40)
            self.ui.lError.setText("Имя пользователя занято. Попробуйте другое")
            self.ui.lError.setStyleSheet("color: red;")
            self.ui.lError.setFont(mainFont)
            self.ui.lError.show()
            return
        self.MainPage()


    def AddPost(self):
        self.ui = Ui_MainPage()
        self.SetUp()

        titleFont = QFont()
        titleFont.setFamilies([u"Yu Gothic UI"])
        titleFont.setPointSize(24)

        mainFont = QFont()
        mainFont.setFamilies([u"Yu Gothic UI"])
        mainFont.setPointSize(16)

        subFont = QFont()
        subFont.setFamilies([u"Yu Gothic UI"])
        subFont.setPointSize(18)

        miniFont = QFont()
        miniFont.setFamilies([u"Yu Gothic UI"])
        miniFont.setPointSize(14)

        self.ui.lTitle = QLabel(self.ui.frame)
        self.ui.lTitle.setObjectName(u"lTitle")
        self.ui.lTitle.setFixedSize(350, 60)
        self.ui.lTitle.move((self.ui.frame.width() - self.ui.lTitle.width()) // 2, 20)
        self.ui.lTitle.setFont(subFont)
        self.ui.lTitle.setAlignment(Qt.AlignCenter)
        self.ui.lTitle.setText("Добавление нового поста")
        self.ui.lTitle.setStyleSheet("border: 5px solid gray")

        self.ui.fAddPost = QFrame(self.ui.frame)
        self.ui.fAddPost.setObjectName(u"fAddPost")
        self.ui.fAddPost.setGeometry(50, 100, self.ui.frame.width() - 100, self.ui.frame.height() - 200)
        self.ui.fAddPost.setStyleSheet("background-color: lightgray;")

        self.ui.pbAddPostImage = QPushButton(self.ui.fAddPost)
        self.ui.pbAddPostImage.setObjectName(u"pbAddPostImage")
        self.ui.pbAddPostImage.setStyleSheet(
            "QPushButton\n{\nbackground-color: white; border: 3px solid #B4B4B4;\n}\n"
            "QPushButton:hover\n{\nborder: 3px solid gray\n}\n")
        self.ui.pbAddPostImage.setFixedSize(250, 250)
        self.ui.pbAddPostImage.move((self.ui.fAddPost.width() - self.ui.pbAddPostImage.width()) // 2, 20)

        self.ui.lPostTitle = QLineEdit(self.ui.fAddPost)
        self.ui.lPostTitle.setObjectName(u"lPostTitle")
        self.ui.lPostTitle.setFixedSize(self.ui.fAddPost.size().width() - 400, 50)
        self.ui.lPostTitle.move((self.ui.fAddPost.size().width() - self.ui.lPostTitle.width()) // 2, 290)
        self.ui.lPostTitle.setFont(mainFont)
        self.ui.lPostTitle.setStyleSheet("background-color: white; border: 3px solid #B4B4B4; padding: 5px;")
        self.ui.lPostTitle.setPlaceholderText("Заголовок поста")

        self.ui.teDescription = QTextEdit(self.ui.fAddPost)
        self.ui.teDescription.setObjectName(u"teDescription")
        self.ui.teDescription.setFixedSize(self.ui.fAddPost.size().width() - 400, 100)
        self.ui.teDescription.move((self.ui.fAddPost.width() - self.ui.teDescription.width()) // 2, 350)
        self.ui.teDescription.setFont(mainFont)
        self.ui.teDescription.setStyleSheet("background-color: white; border: 3px solid #B4B4B4; padding: 5px;")
        self.ui.teDescription.setPlaceholderText("Описание")

        self.ui.pbPublish = QPushButton(self.ui.fAddPost)
        self.ui.pbPublish.setObjectName(u"pbPublish")
        self.ui.pbPublish.setGeometry(200, self.ui.fAddPost.height() - 70, self.ui.fAddPost.width() - 400, 50)
        self.ui.pbPublish.setStyleSheet("QPushButton\n{\nbackground-color: white; border: 3px solid #B4B4B4;\n}\n"
                                            "QPushButton:hover\n{\nborder: 3px solid gray;\n}\n")
        self.ui.pbPublish.setFont(subFont)
        self.ui.pbPublish.setText("Опубликовать")

        self.ui.pbHome = QPushButton(self.ui.frame)
        self.ui.pbHome.setObjectName(u"pbHome")
        self.ui.pbHome.setGeometry(50, self.ui.frame.height() - 70, self.ui.frame.width() - 100, 50)
        self.ui.pbHome.setStyleSheet("QPushButton\n{\nbackground-color: lightgray;\n}\n"
                                     "QPushButton:hover\n{\nborder: 3px solid black;\n}\n")
        self.ui.pbHome.setFont(subFont)
        self.ui.pbHome.setText("На главную")

        self.ui.pbHome.clicked.connect(self.MainPage)
        self.ui.pbAddPostImage.clicked.connect(self.AddPostImage)
        self.ui.pbPublish.clicked.connect(self.PublishPost)


    def AddPostImage(self):
        self.post.photoPath = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите фотографию", filter="*.png; *.jpg; *.jpeg")[0]
        self.ui.pbAddPostImage.setText("")

        self.ui.lPostImage = QLabel(self.ui.pbAddPostImage.parent())
        self.ui.lPostImage.setFixedSize(self.ui.pbAddPostImage.size())
        self.ui.lPostImage.move(self.ui.pbAddPostImage.x(), self.ui.pbAddPostImage.y())

        self.ui.lPostImage.setPixmap(QPixmap(self.post.photoPath))

        self.ui.lPostImage.show()


    def PublishPost(self):
        mainFont = QFont()
        mainFont.setFamilies([u"Yu Gothic UI"])
        mainFont.setPointSize(16)
        self.ui.lError = QLabel(self.ui.fAddPost)
        self.ui.lError.setGeometry(self.ui.pbPublish.x(), self.ui.pbPublish.y() - 40,
                                   self.ui.pbPublish.width(), 40)
        self.ui.lError.setFont(mainFont)
        self.ui.lError.setStyleSheet("color: red;")

        self.post.description = self.ui.teDescription.toPlainText()
        if self.post.photoPath == "":
            self.ui.lError.setText("Отсутствует изображение поста!")
            self.ui.lError.show()
            return
        else:
            self.ui.lError.setText("")
            self.ui.lError.hide()

        if len(self.ui.lPostTitle.text()) <= 30:
            self.post.title = self.ui.lPostTitle.text()
            self.ui.lError.setText("")
            self.ui.lError.hide()
        else:
            self.ui.lError.setText("Заголовок поста слишком длинный!")
            self.ui.lError.show()
            return

        addPost(UserInfo.name, [self.post.title, self.post.photoPath, self.post.description])
        self.post = Post()
        self.ProfilePage()

