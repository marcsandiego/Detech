import sys
import re
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import mysql.connector as mc
#---Import that will load the UI file---#
from PyQt5.uic import loadUi
import detechRs_rc
import datetime
from threading import Timer
import schedule
import time

#link kung saan sinundan ko yung getting info from diff window
#https://www.youtube.com/watch?v=NrijKenny3Y

#--CLASS CREATED THAT WILL LOAD THE UI FILE
class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        # --- FROM THE IMPORT PYQT5.UIC IMPORT LOADUI---##
        self.setFixedWidth(1190)  # -- setting the fixed window size in width --#
        self.setFixedHeight(782)  # -- setting the fixed window size in height--#

        #ewan ko ginawa neto parang naging variable lang ni mainPage
        self.mainWindow = mainPage()
        self.openApp()

    def openApp(self):
        # --- a code once the login button clicked, will call the loginFunction ---#
        loadUi("login_UI.ui", self)
        self.loginButton.clicked.connect(self.loginFunction)
        self.registerButton.clicked.connect(self.registerUi)

        # -- Created a function called "loginFunction" --#
    def loginFunction(self):
        lgUserLine = self.lgUserLine.text().title()  # -- Getting the textbox context lgUserline --#
        lgPassLine = self.lgPassLine.text()  # -- Getting the textbox context lgPassline --#
        count = 0

        if lgUserLine == "":
            self.UsernameLabelResult.setText("Username cannot be blank!")
            self.lgUserLine.setStyleSheet(incorrectInput)

        else:
            self.UsernameLabelResult.setText("")
            self.lgUserLine.setStyleSheet(correctInput)
            count += 1

        if lgPassLine == "":
            self.PasswordLabelResult.setText("Password cannot be blank!")
            self.lgPassLine.setStyleSheet(incorrectInput)
        else:
            self.PasswordLabelResult.setText("")
            self.lgPassLine.setStyleSheet(correctInput)
            count += 1

        if count == 2:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="detech"
            )
            mycursor = mydb.cursor()
            query = "SELECT * FROM users WHERE '" + lgUserLine + "' LIKE username AND '" + lgPassLine + "' LIKE password"
            mycursor.execute(query)
            result = mycursor.fetchone()

            if result is None:
                self.UsernameLabelResult.setText("Incorrect username and/or password. Please try again.")
                self.PasswordLabelResult.setText("Incorrect username and/or password. Please try again.")
                self.lgUserLine.setText("")
                self.lgPassLine.setText("")
                self.lgUserLine.setStyleSheet(incorrectInput)
                self.lgPassLine.setStyleSheet(incorrectInput)

            else: #call mainPage function
                self.passingInformation()


    def registerUi(self):
        loadUi("register_UI.ui", self)
        self.setFixedWidth(1190)  # -- setting the fixed window size in width --#
        self.setFixedHeight(782)  # -- setting the fixed window size in height--#
        self.registerButton.clicked.connect(self.registerFunction)
        self.loginHere.clicked.connect(self.openApp) #should go back to the first function!!!

    def registerFunction(self):
        count = 0
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="detech"
        )
        nameRegLine = self.nameRegLine.text().title()  # -- Getting the textbox context lgUserline --#
        usernameRegLine = self.usernameRegLine.text()  # -- Getting the textbox context lgPassline --#
        emailRegLine = self.emailRegLine.text()  # -- Getting the textbox context lgPassline --#
        passwordRegLine = self.passwordRegLine.text()  # -- Getting the textbox context lgPassline --#
        confirmPasswordRegLine = self.confirmPasswordRegLine.text()  # -- Getting the textbox context lgPassline --#

        #goods, checks if blank only
        if nameRegLine == "":
            self.labelNameError.setText("Name cannot be blank!")
            self.nameRegLine.setStyleSheet(incorrectInput)
        else:
            self.labelNameError.setText("")
            self.nameRegLine.setStyleSheet(correctInput)
            count += 1

        # goods, check if unique
        if usernameRegLine == "":
            self.labelUsernameError.setText("Username cannot be blank!")
            self.usernameRegLine.setStyleSheet(incorrectInput)
        else:
            self.labelUsernameError.setText("")
            self.usernameRegLine.setStyleSheet(correctInput)
            #query first
            mycursor = mydb.cursor()
            query = "SELECT * FROM users WHERE '" + usernameRegLine + "' LIKE username"
            mycursor.execute(query)
            result = mycursor.fetchone()

            #if unique username, save
            if result is not None:
                self.labelUsernameError.setText("Username is already in use!")
                self.usernameRegLine.setStyleSheet(incorrectInput)
                self.usernameRegLine.setText("")
            else:
                self.usernameRegLine.setStyleSheet(correctInput)
                count += 1

        # goods - email validator and check if unique
        if emailRegLine == "":
            self.labelEmailError.setText("Email cannot be blank!")
            self.emailRegLine.setStyleSheet(incorrectInput)
        else:
            self.labelEmailError.setText("")
            # check if valid email, query unique email
            if not re.fullmatch(regex, emailRegLine):
                self.labelEmailError.setText("Email is not valid!")
                self.emailRegLine.setStyleSheet(incorrectInput)
            else:
                # query email
                mycursor = mydb.cursor()
                queryEmail = "SELECT * FROM users WHERE '" + emailRegLine + "' LIKE email"
                mycursor.execute(queryEmail)
                resultEmail = mycursor.fetchone()

                if resultEmail is not None:
                    self.labelEmailError.setText("Email is already in used!")
                    self.emailRegLine.setStyleSheet(incorrectInput)
                    self.emailRegLine.setText("")
                # if unique email, save
                else:
                    count += 1
                    self.emailRegLine.setStyleSheet(correctInput)

        # goods, 8 or more character with number
        if passwordRegLine == "":
            self.labelPasswordError.setText("Password cannot be blank!")
            self.passwordRegLine.setStyleSheet(incorrectInput)
        else:
            self.labelPasswordError.setText("")
            self.passwordRegLine.setStyleSheet(correctInput)
            #8 or more letter, should contain number
            if len(passwordRegLine) < 8:
                self.labelPasswordError.setText("Password must be atleast 8!")
                self.passwordRegLine.setStyleSheet(incorrectInput)
            else:
                if str.isalpha(passwordRegLine):
                    self.labelPasswordError.setText("Password must have atleast one integer!")
                    self.passwordRegLine.setStyleSheet(incorrectInput)
                else:
                    count += 1
                    self.passwordRegLine.setStyleSheet(correctInput)

        #goods, confirm password
        if confirmPasswordRegLine == "":
            self.labelConfirmPasswordError.setText("Please re-type password!")
            self.confirmPasswordRegLine.setStyleSheet(incorrectInput)
        else:
            self.labelConfirmPasswordError.setText("")
            if confirmPasswordRegLine != passwordRegLine:
                self.labelConfirmPasswordError.setText("Password mismatch, try again!")
                self.confirmPasswordRegLine.setStyleSheet(incorrectInput)
                self.confirmPasswordRegLine.setText("")
            else:
                count += 1
                self.confirmPasswordRegLine.setStyleSheet(correctInput)

        #save to database if all conditions are passed!
        if count == 5:
            mycursor = mydb.cursor()
            insert = "INSERT INTO users (name, username, email, password, confirm_password) VALUES (%s, %s, %s, %s, %s)"
            value = (nameRegLine, usernameRegLine, emailRegLine, passwordRegLine, confirmPasswordRegLine)
            mycursor.execute(insert, value)
            mydb.commit()
            self.openApp()


    def passingInformation(self):
        self.mainWindow.userDisplayLabel.setText(self.lgUserLine.text())
        self.mainWindow.displayingInformation()
        self.mainWindow.displayProfile()

class mainPage(QMainWindow):
    def __init__(self):
        super(mainPage, self).__init__()
        # --- FROM THE IMPORT PYQT5.UIC IMPORT LOADUI---##
        loadUi("mainPage_UI.ui",self)
        #self.setFixedWidth(1596)
        #self.setFixedHeight(882)

        # --- SET THE PROFILE PAGE AS A DEFAULT PAGE AFTER LOGGING IN --- #
        self.stackedWidget.setCurrentWidget(self.profile_page)


        # date and time = need to improve the time, should be running
        dateTime = datetime.datetime.now()
        self.dateDisplay_label.setText('%s/%s/%s' % (dateTime.month, dateTime.day, dateTime.year))
        self.timeDisplay_label.setText('%s:%s:%s' % (dateTime.hour, dateTime.minute, dateTime.second))

        # --- CODED BUTTONS IN ABLE TO SELECT A CERTAIN STACKED WIDGET PAGE --- #
        self.profileButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.profile_page)) # Profile button to Profile page
        self.surveillanceButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.surveillance_page)) # Surveillance Button to Surveillance page
        self.dataHistoryButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.dataHistory_page)) # Data history button to Data history page
        self.settingsButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.settings_page)) # settings button to settings page

        #--- PROFILE EDIT PAGE ---#
        self.editProfile_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.editProfile_page)) # Edit profile button to edit profile
        self.editProfile_button.clicked.connect(lambda: self.editProfileWidget.setCurrentWidget(self.editUser_page))
        self.editProfileBack_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.profile_page)) # -- CANCEL BUTTON --#

        #--- PROFILE EDIT STACKED WIDGETS ---#

        self.editUser_button.clicked.connect(lambda: self.editProfileWidget.setCurrentWidget(self.editUser_page))
        self.editNameOwner_button.clicked.connect(lambda: self.editProfileWidget.setCurrentWidget(self.editNameOwner_page))
        self.editStoreName_button.clicked.connect(lambda: self.editProfileWidget.setCurrentWidget(self.editStoreName_page))
        self.editStoreType_button.clicked.connect(lambda: self.editProfileWidget.setCurrentWidget(self.editStoreType_page))
        self.editAddress_button.clicked.connect(lambda: self.editProfileWidget.setCurrentWidget(self.editAddress_page))
        self.editCity_button.clicked.connect(lambda: self.editProfileWidget.setCurrentWidget(self.editCity_page))
        self.editCountry_button.clicked.connect(lambda: self.editProfileWidget.setCurrentWidget(self.editCountry_page))


        #--- SETTINGS PAGE WIDGETS ---#
        self.detectionSetup_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.detectionSetup_page)) #detection setup button from settings to detection setup page
        self.setupCCTV_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.setupCCTV_page)) #setup cctv button from setings to setup cctv page

        #--- DETECTION SETUP PAGE BUTTONS ---#
        self.dtSetupBack_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.settings_page)) #-- BACK BUTTON DETECTION SETUP, RETURNS TO SETTINGS PAGE ---#

        # --- SET THE PROFILE PAGE AS A DEFAULT PAGE AFTER LOGGING IN --- #
        self.setupCCTV_widget.setCurrentWidget(self.cctvAvailableConnect_page)

        # --- setupCCTV widgets ---#
        self.cancelSetup_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.settings_page)) #cancel setup cctv button, returns to setting page
        self.connectIP_button.clicked.connect(lambda: self.setupCCTV_widget.setCurrentWidget(self.connectIP_page)) #connect IP button to connect IP page
        self.continueConnectIP_button.clicked.connect(lambda: self.setupCCTV_widget.setCurrentWidget(self.cctvConnectedView_page)) # continue to connect ip to cinnection view surveillance sucesss
        self.checkSurveillance_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.surveillance_page)) #check surveillance button redirect to surveillance.

        # --- SET THE "ALL CAMERA" PAGE AS A DEFAULT PAGE WHEN SELECTING THE SURVEILLANCE PAGE--- #
        self.surveillance_frame.setCurrentWidget(self.allCamera_page)

        # --- CODED BUTTONS FOR SURVEILLANCE PAGE --- #
        self.camera1_button.clicked.connect(lambda: self.surveillance_frame.setCurrentWidget(self.camera1_page))
        self.camera2_button.clicked.connect(lambda: self.surveillance_frame.setCurrentWidget(self.camera2_page))
        self.camera3_button.clicked.connect(lambda: self.surveillance_frame.setCurrentWidget(self.camera3_page))
        self.camera4_button.clicked.connect(lambda: self.surveillance_frame.setCurrentWidget(self.camera4_page))
        self.allCamera_button.clicked.connect(lambda: self.surveillance_frame.setCurrentWidget(self.allCamera_page))
        self.displayProfile()


    def displayingInformation(self):
        self.show()

    def displayProfile(self):
        # Display profile
        username1 = self.userDisplayLabel.text()
        self.editUsernameField.setText(username1)
        self.editUserLabel.setText("")

        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="detech"
        )

        mycursor = mydb.cursor()
        query = "SELECT * FROM users WHERE '" + username1 + "' LIKE username"
        mycursor.execute(query)
        result = mycursor.fetchall()

        for row in result:
            self.nameDisplay_label.setText(row[0])
            self.nameStore_label.setText(row[5])
            self.typeStore_label.setText(row[6])
            self.storeAddDisplay_label.setText(row[7])
            self.cityDisplay_label.setText(row[8])
            self.countryDisplay_label.setText(row[9])
            self.editOwnerField.setText(row[0])
            self.editStoreNameField.setText(row[5])
            self.editStoreTypeField.setText(row[6])
            self.editAddressField.setText(row[7])
            self.editCityField.setText(row[8])
            self.editCountryField.setText(row[9])

        #buttons for change - to commit changes in credentials
        self.saveUsername_button.clicked.connect(self.changeUsername)
        self.savePass_button.clicked.connect(self.changePassword)
        self.changePassCancel_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.profile_page))
        self.saveOwner_button.clicked.connect(self.changeOwnername)
        self.saveStoreName_button.clicked.connect(self.changeStorename)
        self.saveStoreType_button.clicked.connect(self.changeStoretype)
        self.saveAddress_button.clicked.connect(self.changeAddress)
        self.saveCity_button.clicked.connect(self.changeCity)
        self.saveCountry_button.clicked.connect(self.changeCountry)
        self.changePass_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.changePass_page))  # change password button to change password page
        self.logoutAccount_button.clicked.connect(self.showDialogLogout)
        self.faceMaskOnly_radioButton.clicked.connect(self.fmOnly)
        self.faceShieldOnly_radioButton.clicked.connect(self.fsOnly)
        self.facemaskFaceshield_radioButton.clicked.connect(self.both)


    def changeUsername(self):
        username1 = self.userDisplayLabel.text()
        editUsername = self.editUsernameField.text()
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="detech"
        )

        if editUsername == "":
            self.editUserLabel.setText("Please input a username") #to change
            self.editUsernameField.setStyleSheet(incorrectEditInput)
        else:
            self.editUserLabel.setText("")
            mycursor = mydb.cursor()
            query = "SELECT * FROM users WHERE '" + editUsername + "' LIKE username"
            mycursor.execute(query)
            result = mycursor.fetchone()
            if result is not None:
                self.editUserLabel.setText("Username is already in use!")
                self.editUsernameField.setStyleSheet(incorrectEditInput)
            else:
                self.userDisplayLabel.setText(editUsername)
                self.editUsernameField.setStyleSheet(correctEditInput)
                self.editUserLabel.setText("")
                mycursor = mydb.cursor()
                query = "UPDATE users SET username = %s  WHERE username = %s"
                value = (editUsername, username1)
                mycursor.execute(query, value)
                mydb.commit()
                self.stackedWidget.setCurrentWidget(self.profile_page)
                self.displayProfile()

    def changeOwnername(self):
        username1 = self.userDisplayLabel.text()
        editOwnername = self.editOwnerField.text().title()

        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="detech"
        )

        if editOwnername == "":
            self.editOwnerLabel.setText("Please input your name")
            self.editOwnerField.setStyleSheet(incorrectEditInput)
        else:
            self.editOwnerLabel.setText("")
            self.editOwnerField.setStyleSheet(correctEditInput)
            mycursor = mydb.cursor()
            query = "UPDATE users SET name = %s  WHERE username = %s"
            value = (editOwnername, username1)
            mycursor.execute(query, value)
            mydb.commit()
            self.stackedWidget.setCurrentWidget(self.profile_page)
            self.displayProfile()

    def changeStorename(self):
        username1 = self.userDisplayLabel.text()
        editStorename = self.editStoreNameField.text().title()

        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="detech"
        )

        if editStorename == "":
            self.editStoreLabel.setText("Please input the store name")
            self.editStoreNameField.setStyleSheet(incorrectEditInput)
        else:
            self.editStoreLabel.setText("")
            mycursor = mydb.cursor()
            self.editStoreNameField.setStyleSheet(correctEditInput)
            query = "UPDATE users SET store_name = %s  WHERE username = %s"
            value = (editStorename, username1)
            mycursor.execute(query, value)
            mydb.commit()
            self.stackedWidget.setCurrentWidget(self.profile_page)
            self.displayProfile()

    def changeStoretype(self):
        username1 = self.userDisplayLabel.text()
        editStoretype = self.editStoreTypeField.text().title()

        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="detech"
        )

        if editStoretype == "":
            self.editTypeStoreLabel.setText("Please input the store type")
            self.editStoreTypeField.setStyleSheet(incorrectEditInput)
        else:
            self.editTypeStoreLabel.setText("")
            mycursor = mydb.cursor()
            self.editStoreTypeField.setStyleSheet(correctEditInput)
            query = "UPDATE users SET store_type = %s  WHERE username = %s"
            value = (editStoretype, username1)
            mycursor.execute(query, value)
            mydb.commit()
            self.stackedWidget.setCurrentWidget(self.profile_page)
            self.displayProfile()

    def changeAddress(self):
        username1 = self.userDisplayLabel.text()
        editAddress = self.editAddressField.text().title()

        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="detech"
        )

        if editAddress == "":
            self.editAddressLabel.setText("Please input the store address")
            self.editAddressField.setStyleSheet(incorrectEditInput)
        else:
            self.editAddressLabel.setText("")
            mycursor = mydb.cursor()
            self.editAddressField.setStyleSheet(correctEditInput)
            query = "UPDATE users SET address = %s  WHERE username = %s"
            value = (editAddress, username1)
            mycursor.execute(query, value)
            mydb.commit()
            self.stackedWidget.setCurrentWidget(self.profile_page)
            self.displayProfile()

    def changeCity(self):
        username1 = self.userDisplayLabel.text()
        editCity = self.editCityField.text().title()
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="detech"
        )

        if editCity == "":
            self.editCityLabel.setText("Please input city")
            self.editCityField.setStyleSheet(incorrectEditInput)
        else:
            self.editCityLabel.setText("")
            mycursor = mydb.cursor()
            self.editCityField.setStyleSheet(correctEditInput)
            query = "UPDATE users SET city = %s  WHERE username = %s"
            value = (editCity, username1)
            mycursor.execute(query, value)
            mydb.commit()
            self.stackedWidget.setCurrentWidget(self.profile_page)
            self.displayProfile()

    def changeCountry(self):
        username1 = self.userDisplayLabel.text()
        editCountry = self.editCountryField.text().title()

        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="detech"
        )

        if editCountry == "":
            self.editCountryLabel.setText("Please input country")
            self.editCountryField.setStyleSheet(incorrectEditInput)
        else:
            self.editCountryLabel.setText("")
            mycursor = mydb.cursor()
            self.editCountryField.setStyleSheet(correctEditInput)
            query = "UPDATE users SET country = %s  WHERE username = %s"
            value = (editCountry, username1)
            mycursor.execute(query, value)
            mydb.commit()
            self.stackedWidget.setCurrentWidget(self.profile_page)
            self.displayProfile()

    def changePassword(self):
        username1 = self.userDisplayLabel.text()
        oldPass = self.oldPass_lineEdit.text()
        newPass = self.newPass_lineEdit.text()
        count = 0

        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="detech"
        )

        if oldPass == "":
            self.oldPassLabel.setText("Input your old password")
            self.oldPass_lineEdit.setStyleSheet(incorrectEditInput)
        else:
            self.oldPassLabel.setText("")
            mycursor = mydb.cursor()
            query = "SELECT * FROM users WHERE '" + oldPass + "' LIKE password AND '" + username1 + "' LIKE username"
            mycursor.execute(query)
            result = mycursor.fetchone()

            if result is not None:
                self.oldPassLabel.setText("")
                self.oldPass_lineEdit.setStyleSheet(correctEditInput)
                count += 1
            else:
                self.oldPassLabel.setText("Incorrect old password")
                self.oldPass_lineEdit.setStyleSheet(incorrectEditInput)

        if newPass == "":
            self.newPassLabel.setText("Input new password")
            self.newPass_lineEdit.setStyleSheet(incorrectEditInput)
        else:
            self.newPassLabel.setText("")
            if len(newPass) < 8:
                self.newPassLabel.setText("New password must be at least 8 characters!")
                self.newPass_lineEdit.setStyleSheet(incorrectEditInput)
            else:
                if str.isalpha(newPass):
                    self.newPassLabel.setText("New password must have at least one integer!")
                    self.newPass_lineEdit.setStyleSheet(incorrectEditInput)
                else:
                    self.newPass_lineEdit.setStyleSheet(correctEditInput)
                    count += 1

        if count == 2:
            mycursor = mydb.cursor()
            query = "UPDATE users SET password = %s , confirm_password = %s  WHERE username = %s"
            value = (newPass, newPass, username1)
            mycursor.execute(query, value)
            mydb.commit()
            self.oldPassLabel.setText("")
            self.newPassLabel.setText("")
            self.stackedWidget.setCurrentWidget(self.profile_page)
            self.displayProfile()

    def showDialogLogout(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText("Are you sure you want to logout?")
        msgBox.setWindowTitle("Confirm Exit")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Yes:
            print('OK clicked')
            sys.exit()

    def fmOnly(self):
        if self.faceMaskOnly_radioButton.isChecked():
            self.detectionChoice_label.setText("Face Mask Only")
            pixmap = QPixmap('images/fmonly.png')
            self.pictureDetectionSample_label.setPixmap(pixmap)
        else:
            self.detectionChoice_label.setText("")
        self.displayProfile()

    def fsOnly(self):
        if self.faceShieldOnly_radioButton.isChecked():
            self.detectionChoice_label.setText("Face Shield Only")
            pixmap = QPixmap('images/fsonly.png')
            self.pictureDetectionSample_label.setPixmap(pixmap)
        else:
            self.detectionChoice_label.setText("")
        self.displayProfile()

    def both(self):
        if self.facemaskFaceshield_radioButton.isChecked():
            self.detectionChoice_label.setText("Face Mask and Face Shield")
            pixmap = QPixmap('images/both.png')
            self.pictureDetectionSample_label.setPixmap(pixmap)
        else:
            self.detectionChoice_label.setText("")
        self.displayProfile()





#variables for stylesheet

#login and register
correctInput = """
QLineEdit{
border: 2px solid rgb(121, 121, 121);
color: rgb(255, 255, 255);
border-radius: 8px;
padding-left: 15px;
}
QLineEdit::hover{border : 2px solid white; border-radius: 8px; color: rgb(255, 255, 255);}
QLineEdit::!hover{border : 2px solid rgb(121, 121, 121); border-radius: 8px; color: rgb(255, 255, 255);}
"""
incorrectInput = """
QLineEdit{
color: rgb(255, 255, 255);
border-radius: 8px;
padding-left: 15px;
}
background-color:rgba(40, 48, 79, 1); border-radius: 8px;\                                                         
color: rgb(255, 255, 255); border: 2px solid rgb(250, 95, 85);
"""

#edit account
correctEditInput = """
QLineEdit{
font: 15px "Roboto";
border: 2px solid rgb(121, 121, 121);
color:rgb(255, 255, 255);
background-color: rgba(19, 24, 42, 1);
border-radius: 8px;
padding-left: 15px;
}
QLineEdit::hover{border : 2px solid white; border-radius: 8px; color: rgb(255, 255, 255);}
QLineEdit::!hover{border : 2px solid rgb(121, 121, 121); border-radius: 8px; color: rgb(255, 255, 255);}
"""

incorrectEditInput = """
QLineEdit{
font: 15px "Roboto";
color:rgb(255, 255, 255);
border-radius: 8px;
padding-left: 15px;
background-color: rgba(19, 24, 42, 1);
}
background-color: rgba(19, 24, 42, 1); border-radius: 8px;\                                                         
color: rgb(255, 255, 255); border: 2px solid rgb(250, 95, 85);
"""


#--- LAUNCHING THE APPLICATION ---#

app=QApplication(sys.argv)
loginWindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(loginWindow) #-- displays all design widgets of the UI Window --#
widget.show()
app.exec_() #-- window execution --#