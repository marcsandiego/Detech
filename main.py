import sys
import re
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
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
        super(Login, self).__init__()
        # --- FROM THE IMPORT PYQT5.UIC IMPORT LOADUI---##
        loadUi("login_UI.ui",self)
        self.setFixedWidth(1190)  # -- setting the fixed window size in width --#
        self.setFixedHeight(782)  # -- setting the fixed window size in height--#

        # --- a code once the login button clicked, will call the loginFunction ---#
        self.loginButton.clicked.connect(self.loginFunction)
        self.registerButton.clicked.connect(self.registerUi)

        #ewan ko ginawa neto parang naging variable lang ni mainPage
        self.mainWindow = mainPage()

        # -- Created a function called "loginFunction" --#
    def loginFunction(self):
        lgUserLine = self.lgUserLine.text().capitalize()  # -- Getting the textbox context lgUserline --#
        lgPassLine = self.lgPassLine.text()  # -- Getting the textbox context lgPassline --#
        count = 0

        if lgUserLine == "":
            self.UsernameLabelResult.setText("Username cannot be blank!")
        else:
            self.UsernameLabelResult.setText("")
            count += 1

        if lgPassLine == "":
            self.PasswordLabelResult.setText("Password cannot be blank!")
        else:
            self.PasswordLabelResult.setText("")
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

            else: #call mainPage function
                self.passingInformation()


    def registerUi(self):
        loadUi("register_UI.ui", self)
        self.setFixedWidth(1190)  # -- setting the fixed window size in width --#
        self.setFixedHeight(782)  # -- setting the fixed window size in height--#
        self.registerButton.clicked.connect(self.registerFunction)

    def registerFunction(self):
        count = 0
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="detech"
        )
        nameRegLine = self.nameRegLine.text().capitalize()  # -- Getting the textbox context lgUserline --#
        usernameRegLine = self.usernameRegLine.text()  # -- Getting the textbox context lgPassline --#
        emailRegLine = self.emailRegLine.text()  # -- Getting the textbox context lgPassline --#
        passwordRegLine = self.passwordRegLine.text()  # -- Getting the textbox context lgPassline --#
        confirmPasswordRegLine = self.confirmPasswordRegLine.text()  # -- Getting the textbox context lgPassline --#

        #goods, checks if blank only
        if nameRegLine == "":
            self.labelNameError.setText("Name cannot be blank!")
        else:
            self.labelNameError.setText("")
            count += 1

        # goods, check if unique
        if usernameRegLine == "":
            self.labelUsernameError.setText("Username cannot be blank!")
        else:
            self.labelUsernameError.setText("")
            #query first
            mycursor = mydb.cursor()
            query = "SELECT * FROM users WHERE '" + usernameRegLine + "' LIKE username"
            mycursor.execute(query)
            result = mycursor.fetchone()

            #if unique username, save
            if result is not None:
                self.labelUsernameError.setText("Username is already in use!")
                self.usernameRegLine.setText("")
            else:
                count += 1

        # goods - email validator and check if unique
        if emailRegLine == "":
            self.labelEmailError.setText("Email cannot be blank!")
        else:
            self.labelEmailError.setText("")
            # check if valid email, query unique email
            if not re.fullmatch(regex, emailRegLine):
                self.labelEmailError.setText("Email is not valid!")
            else:
                # query email
                mycursor = mydb.cursor()
                queryEmail = "SELECT * FROM users WHERE '" + emailRegLine + "' LIKE email"
                mycursor.execute(queryEmail)
                resultEmail = mycursor.fetchone()

                if resultEmail is not None:
                    self.labelEmailError.setText("Email is already in used!")
                    self.emailRegLine.setText("")
                # if unique email, save
                else:
                    count += 1

        # goods, 8 or more character with number
        if passwordRegLine == "":
            self.labelPasswordError.setText("Password cannot be blank!")
        else:
            self.labelPasswordError.setText("")
            #8 or more letter, should contain number
            if len(passwordRegLine) < 8:
                self.labelPasswordError.setText("Password must be atleast 8!")
            else:
                if str.isalpha(passwordRegLine):
                    self.labelPasswordError.setText("Password must have atleast one integer!")
                else:
                    count += 1

        #goods, confirm password
        if confirmPasswordRegLine == "":
            self.labelConfirmPasswordError.setText("Please re-type password!")
        else:
            self.labelConfirmPasswordError.setText("")
            if confirmPasswordRegLine != passwordRegLine:
                self.labelConfirmPasswordError.setText("Password mismatch, try again!")
                self.confirmPasswordRegLine.setText("")
            else:
                count += 1

        #save to database if all conditions are passed!
        if count == 5:
            mycursor = mydb.cursor()
            insert = "INSERT INTO users (name, username, email, password, confirm_password) VALUES (%s, %s, %s, %s, %s)"
            value = (nameRegLine, usernameRegLine, emailRegLine, passwordRegLine, confirmPasswordRegLine)
            mycursor.execute(insert, value)
            mydb.commit()
            # go to login function - should call the login class


    def passingInformation(self):
        self.mainWindow.userDisplayLabel.setText(self.lgUserLine.text())
        self.mainWindow.displayingInformation()
        self.mainWindow.displayProfile()

class mainPage(QMainWindow):
    def __init__(self):
        super(mainPage, self).__init__()
        # --- FROM THE IMPORT PYQT5.UIC IMPORT LOADUI---##
        loadUi("mainPage_UI.ui",self)
        self.setFixedWidth(1596)
        self.setFixedHeight(882)

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
        self.editProfile_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.editProfile_page)) # Edit profile button to edit profile page
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
        self.editUsername.setText(username1)
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

        self.saveUsername_button.clicked.connect(self.changeUsername)
        self.savePass_button.clicked.connect(self.changePassword)
        self.changePass_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.changePass_page))  # change password button to change password page



    def changeUsername(self):
        username1 = self.userDisplayLabel.text()
        editUsername = self.editUsername.text()
        count = 0
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="detech"
        )

        if editUsername == "":
            self.editUserLabel.setText("Please input a username") #to change
        else:
            self.editUserLabel.setText("")
            mycursor = mydb.cursor()
            query = "SELECT * FROM users WHERE '" + editUsername + "' LIKE username"
            mycursor.execute(query)
            result = mycursor.fetchone()
            if result is not None:
                self.editUserLabel.setText("Username is already in use!")
            else:
                self.editUserLabel.setText("")
                self.userDisplayLabel.setText(editUsername)
                count += 1

        if count == 1:
            self.editUserLabel.setText("")
            mycursor = mydb.cursor()
            query = "UPDATE users SET username = %s  WHERE username = %s"
            value = (editUsername, username1)
            mycursor.execute(query, value)
            mydb.commit()
            self.stackedWidget.setCurrentWidget(self.profile_page)
            self.displayProfile()


    def changePassword(self):
        self.changePassCancel_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.profile_page))
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
            self.oldPassLabel.setText("Input password")
        else:
            self.oldPassLabel.setText("")
            mycursor = mydb.cursor()
            query = "SELECT * FROM users WHERE '" + oldPass + "' LIKE password AND '" + username1 + "' LIKE username"
            mycursor.execute(query)
            result = mycursor.fetchone()

            if result is not None:
                self.oldPassLabel.setText("")
                count += 1
            else:
                self.oldPassLabel.setText("Incorrect old password")

        if newPass == "":
            self.newPassLabel.setText("Input password")
        else:
            self.newPassLabel.setText("")
            if len(newPass) < 8:
                self.newPassLabel.setText("New password must be at least 8 characters!")
            else:
                if str.isalpha(newPass):
                    self.newPassLabel.setText("New password must have at least one integer!")
                else:
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










#--- LAUNCHING THE APPLICATION ---#

app=QApplication(sys.argv)
loginWindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(loginWindow) #-- displays all design widgets of the UI Window --#
widget.show()
app.exec_() #-- window execution --#