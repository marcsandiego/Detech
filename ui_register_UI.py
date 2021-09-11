# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register_UIrmktRL.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import detechRs_rc

class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        if not loginWindow.objectName():
            loginWindow.setObjectName(u"loginWindow")
        loginWindow.resize(1190, 775)
        loginWindow.setStyleSheet(u"background-color: rgb(19, 24, 42);")
        self.centralwidget = QWidget(loginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.registrationFrame = QFrame(self.centralwidget)
        self.registrationFrame.setObjectName(u"registrationFrame")
        self.registrationFrame.setGeometry(QRect(-10, 40, 1201, 741))
        self.registrationFrame.setStyleSheet(u"background-color: rgb(40, 48, 79);")
        self.registrationFrame.setFrameShape(QFrame.StyledPanel)
        self.registrationFrame.setFrameShadow(QFrame.Raised)
        self.nameRegLabel = QLabel(self.registrationFrame)
        self.nameRegLabel.setObjectName(u"nameRegLabel")
        self.nameRegLabel.setGeometry(QRect(130, 110, 81, 16))
        font = QFont()
        font.setPointSize(10)
        self.nameRegLabel.setFont(font)
        self.nameRegLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.nameRegLine = QLineEdit(self.registrationFrame)
        self.nameRegLine.setObjectName(u"nameRegLine")
        self.nameRegLine.setGeometry(QRect(130, 130, 341, 41))
        self.nameRegLine.setFont(font)
        self.nameRegLine.setStyleSheet(u"QLineEdit{\n"
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
        self.nameRegLine.setInputMask(u"")
        self.nameRegLine.setEchoMode(QLineEdit.Normal)
        self.registerButton = QPushButton(self.registrationFrame)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setGeometry(QRect(220, 610, 151, 41))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.registerButton.setFont(font1)
        self.registerButton.setStyleSheet(u"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(16, 91, 151, 255), stop:1 rgba(44, 156, 234, 255));\n"
"color: white;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 rgb(119, 88, 127), stop: 1 rgb(28, 96, 255)\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 rgb(17, 21, 255), stop: 1 #ddd\n"
"        );\n"
"    }")
        icon = QIcon()
        icon.addFile(u":/images/images/ri_login-circle-fill.png", QSize(), QIcon.Normal, QIcon.Off)
        self.registerButton.setIcon(icon)
        self.registerButton.setIconSize(QSize(25, 25))
        self.label = QLabel(self.registrationFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 660, 141, 20))
        font2 = QFont()
        font2.setPointSize(9)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_3 = QLabel(self.registrationFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(600, 0, 601, 741))
        self.label_3.setPixmap(QPixmap(u":/images/images/login image.jpg"))
        self.label_3.setScaledContents(True)
        self.label_2 = QLabel(self.registrationFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 591, 51))
        self.label_2.setStyleSheet(u"border-image:url(:/images/images/rectangleReg.png)")
        self.accountReg = QLabel(self.registrationFrame)
        self.accountReg.setObjectName(u"accountReg")
        self.accountReg.setGeometry(QRect(160, 30, 291, 41))
        font3 = QFont()
        font3.setPointSize(22)
        font3.setBold(True)
        self.accountReg.setFont(font3)
        self.accountReg.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(79, 112, 190, 1);")
        self.usernameRegLabel = QLabel(self.registrationFrame)
        self.usernameRegLabel.setObjectName(u"usernameRegLabel")
        self.usernameRegLabel.setGeometry(QRect(130, 210, 81, 16))
        self.usernameRegLabel.setFont(font)
        self.usernameRegLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.usernameRegLine = QLineEdit(self.registrationFrame)
        self.usernameRegLine.setObjectName(u"usernameRegLine")
        self.usernameRegLine.setGeometry(QRect(130, 230, 341, 41))
        self.usernameRegLine.setFont(font)
        self.usernameRegLine.setStyleSheet(u"QLineEdit{\n"
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
        self.usernameRegLine.setInputMask(u"")
        self.usernameRegLine.setEchoMode(QLineEdit.Normal)
        self.emailRegLine = QLineEdit(self.registrationFrame)
        self.emailRegLine.setObjectName(u"emailRegLine")
        self.emailRegLine.setGeometry(QRect(130, 330, 341, 41))
        self.emailRegLine.setFont(font)
        self.emailRegLine.setStyleSheet(u"QLineEdit{\n"
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
        self.emailRegLine.setInputMask(u"")
        self.emailRegLine.setEchoMode(QLineEdit.Normal)
        self.emailRegLabel = QLabel(self.registrationFrame)
        self.emailRegLabel.setObjectName(u"emailRegLabel")
        self.emailRegLabel.setGeometry(QRect(130, 310, 81, 16))
        self.emailRegLabel.setFont(font)
        self.emailRegLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.passwordRegLabel = QLabel(self.registrationFrame)
        self.passwordRegLabel.setObjectName(u"passwordRegLabel")
        self.passwordRegLabel.setGeometry(QRect(130, 410, 81, 16))
        self.passwordRegLabel.setFont(font)
        self.passwordRegLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.passwordRegLine = QLineEdit(self.registrationFrame)
        self.passwordRegLine.setObjectName(u"passwordRegLine")
        self.passwordRegLine.setGeometry(QRect(130, 430, 341, 41))
        self.passwordRegLine.setFont(font)
        self.passwordRegLine.setStyleSheet(u"QLineEdit{\n"
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
        self.passwordRegLine.setInputMask(u"")
        self.passwordRegLine.setEchoMode(QLineEdit.Normal)
        self.confirmPasswordRegLabel = QLabel(self.registrationFrame)
        self.confirmPasswordRegLabel.setObjectName(u"confirmPasswordRegLabel")
        self.confirmPasswordRegLabel.setGeometry(QRect(130, 510, 111, 16))
        self.confirmPasswordRegLabel.setFont(font)
        self.confirmPasswordRegLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.confirmPasswordRegLine = QLineEdit(self.registrationFrame)
        self.confirmPasswordRegLine.setObjectName(u"confirmPasswordRegLine")
        self.confirmPasswordRegLine.setGeometry(QRect(130, 530, 341, 41))
        self.confirmPasswordRegLine.setFont(font)
        self.confirmPasswordRegLine.setStyleSheet(u"QLineEdit{\n"
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
        self.confirmPasswordRegLine.setInputMask(u"")
        self.confirmPasswordRegLine.setEchoMode(QLineEdit.Normal)
        self.loginHere = QPushButton(self.registrationFrame)
        self.loginHere.setObjectName(u"loginHere")
        self.loginHere.setGeometry(QRect(330, 660, 75, 20))
        self.loginHere.setStyleSheet(u"QPushButton{\n"
"color: rgb(45, 158, 236);\n"
"font: 700 9pt \"Segoe UI\";\n"
"text-decoration: underline;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 rgb(70, 70, 70), stop: 1 rgb(85, 170, 255)\n"
"        );\n"
"    }")
        self.loginHere.setFlat(True)
        self.detechLabel = QLabel(self.centralwidget)
        self.detechLabel.setObjectName(u"detechLabel")
        self.detechLabel.setGeometry(QRect(20, 10, 81, 21))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.detechLabel.setFont(font4)
        self.detechLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        loginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(loginWindow)

        QMetaObject.connectSlotsByName(loginWindow)
    # setupUi

    def retranslateUi(self, loginWindow):
        loginWindow.setWindowTitle(QCoreApplication.translate("loginWindow", u"MainWindow", None))
        self.nameRegLabel.setText(QCoreApplication.translate("loginWindow", u"Name:", None))
        self.registerButton.setText(QCoreApplication.translate("loginWindow", u"Register", None))
        self.label.setText(QCoreApplication.translate("loginWindow", u"Already have an account?", None))
        self.label_3.setText("")
        self.label_2.setText("")
        self.accountReg.setText(QCoreApplication.translate("loginWindow", u"Account Registration", None))
        self.usernameRegLabel.setText(QCoreApplication.translate("loginWindow", u"Username:", None))
        self.emailRegLabel.setText(QCoreApplication.translate("loginWindow", u"Email:", None))
        self.passwordRegLabel.setText(QCoreApplication.translate("loginWindow", u"Password:", None))
        self.confirmPasswordRegLabel.setText(QCoreApplication.translate("loginWindow", u"Confirm Password:", None))
        self.loginHere.setText(QCoreApplication.translate("loginWindow", u"Login Here", None))
        self.detechLabel.setText(QCoreApplication.translate("loginWindow", u"DETECH", None))
    # retranslateUi

