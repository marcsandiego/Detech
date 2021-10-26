# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_UIaAPcDS.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *



class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        if loginWindow.objectName():
            loginWindow.setObjectName(u"loginWindow")
        loginWindow.resize(1190, 775)
        loginWindow.setStyleSheet(u"background-color: rgb(19, 24, 42);")
        self.centralwidget = QWidget(loginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.loginFrame = QFrame(self.centralwidget)
        self.loginFrame.setObjectName(u"loginFrame")
        self.loginFrame.setGeometry(QRect(-10, 40, 1201, 741))
        self.loginFrame.setStyleSheet(u"background-color: rgb(40, 48, 79);")
        self.loginFrame.setFrameShape(QFrame.StyledPanel)
        self.loginFrame.setFrameShadow(QFrame.Raised)
        self.usernameLoginLabel = QLabel(self.loginFrame)
        self.usernameLoginLabel.setObjectName(u"usernameLoginLabel")
        self.usernameLoginLabel.setGeometry(QRect(750, 280, 81, 16))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(10)
        self.usernameLoginLabel.setFont(font)
        self.usernameLoginLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.passLoginLabel = QLabel(self.loginFrame)
        self.passLoginLabel.setObjectName(u"passLoginLabel")
        self.passLoginLabel.setGeometry(QRect(750, 390, 81, 16))
        self.passLoginLabel.setFont(font)
        self.passLoginLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lgUserLine = QLineEdit(self.loginFrame)
        self.lgUserLine.setObjectName(u"lgUserLine")
        self.lgUserLine.setGeometry(QRect(750, 310, 311, 41))
        self.lgUserLine.setFont(font)
        self.lgUserLine.setStyleSheet(u"QLineEdit{\n"
        "border: 2px solid rgb(121, 121, 121);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius: 8px;\n"
        "padding-left: 15px;\n"
        "}\n"
        "\n"
        "QLineEdit:hover{\n"
        "	border: 2px solid white;\n"
        "}\n"
        "\n"
        "QLineEdit:focus{\n"
        "	border: 2px solid white;\n"
        "}")
        self.lgUserLine.setInputMask(u"")
        self.lgUserLine.setEchoMode(QLineEdit.Normal)
        self.lgPassLine = QLineEdit(self.loginFrame)
        self.lgPassLine.setObjectName(u"lgPassLine")
        self.lgPassLine.setGeometry(QRect(750, 420, 311, 41))
        self.lgPassLine.setFont(font)
        self.lgPassLine.setStyleSheet(u"QLineEdit{\n"
        "border: 2px solid rgb(121, 121, 121);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius: 8px;\n"
        "padding-left: 15px;\n"
        "}\n"
        "\n"
        "QLineEdit:hover{\n"
        "	border: 2px solid white;\n"
        "}\n"
        "\n"
        "QLineEdit:focus{\n"
        "	border: 2px solid white;\n"
        "}")
        self.lgPassLine.setEchoMode(QLineEdit.Password)
        self.loginButton = QPushButton(self.loginFrame)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(830, 520, 151, 41))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.loginButton.setFont(font1)
        self.loginButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(16, 91, 151, 255), stop:1 rgba(44, 156, 234, 255));\n"
        "color: white;\n"
        "border-radius: 20px;")
        icon = QIcon()
        icon.addFile(u":/images/images/ri_login-circle-fill.png", QSize(), QIcon.Normal, QIcon.Off)
        self.loginButton.setIcon(icon)
        self.loginButton.setIconSize(QSize(25, 25))
        self.label = QLabel(self.loginFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(770, 630, 161, 20))
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(9)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.registerHereLabel = QLabel(self.loginFrame)
        self.registerHereLabel.setObjectName(u"registerHereLabel")
        self.registerHereLabel.setGeometry(QRect(940, 630, 101, 21))
        font3 = QFont()
        font3.setFamily(u"Roboto")
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setWeight(75)
        self.registerHereLabel.setFont(font3)
        self.registerHereLabel.setStyleSheet(u"color: rgb(45, 158, 236);")
        self.lgDetechLogo = QLabel(self.loginFrame)
        self.lgDetechLogo.setObjectName(u"lgDetechLogo")
        self.lgDetechLogo.setGeometry(QRect(750, 80, 311, 141))
        self.lgDetechLogo.setPixmap(QPixmap(u":/images/images/LOGO-and-TEXT - DETECH.png"))
        self.lgDetechLogo.setScaledContents(True)
        self.label_3 = QLabel(self.loginFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 0, 601, 741))
        self.label_3.setPixmap(QPixmap(u":/images/images/login image.jpg"))
        self.label_3.setScaledContents(True)
        self.detechLabel = QLabel(self.centralwidget)
        self.detechLabel.setObjectName(u"detechLabel")
        self.detechLabel.setGeometry(QRect(20, 10, 81, 21))
        font4 = QFont()
        font4.setFamily(u"Roboto")
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.detechLabel.setFont(font4)
        self.detechLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        loginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(loginWindow)

        QMetaObject.connectSlotsByName(loginWindow)


    # setupUi

    def retranslateUi(self, loginWindow):
        loginWindow.setWindowTitle(QCoreApplication.translate("loginWindow", u"MainWindow", None))
        self.usernameLoginLabel.setText(QCoreApplication.translate("loginWindow", u"Username:", None))
        self.passLoginLabel.setText(QCoreApplication.translate("loginWindow", u"Password:", None))
        self.loginButton.setText(QCoreApplication.translate("loginWindow", u"Login", None))
        self.label.setText(QCoreApplication.translate("loginWindow", u"Don't have an account?", None))
        self.registerHereLabel.setText(QCoreApplication.translate("loginWindow", u"Register Here.", None))
        self.lgDetechLogo.setText("")
        self.label_3.setText("")
        self.detechLabel.setText(QCoreApplication.translate("loginWindow", u"DETECH", None))
    # retranslateUi

