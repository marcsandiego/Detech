import sys
import re
import os
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QMessageBox, QComboBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
import mysql.connector as mc
#---Import that will load the UI file---#
from PyQt5.uic import loadUi
import detechRs_rc
import datetime
from threading import Timer
import schedule
import time
from yolov5 import detechYolo
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import *
import cv2
import threading

#link kung saan sinundan ko yung getting info from diff window
#https://www.youtube.com/watch?v=NrijKenny3Y

#--CLASS CREATED THAT WILL LOAD THE UI FILE
class mainPage(QMainWindow):
    activeCam = 0
    detections = []
    classes = None
    filenames = []

    def __init__(self):
        super(mainPage, self).__init__()
        # --- FROM THE IMPORT PYQT5.UIC IMPORT LOADUI---##
        self.selectedClass = 0
        self.loadMain()

    def loadMain(self):
        loadUi("mainPage_UI.ui", self)
        # --- SET THE PROFILE PAGE AS A DEFAULT PAGE AFTER LOGGING IN --- #
        self.mainWidget.setCurrentWidget(self.loginPage)

        self.loginButton.clicked.connect(self.loginFunction)
        self.registerButton.clicked.connect(self.registerUi)

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
            else:#pasok na sa app
                self.user_id = result[0]
                print(self.user_id)
                self.loadMainApp()

    def registerUi(self):
        self.mainWidget.setCurrentWidget(self.registerPage)
        self.registeredButton.clicked.connect(self.registerFunction)
        self.loginHere.clicked.connect(self.loadMain) #should go back to the first function!!!

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
            insert = "INSERT INTO users (name, username, email, password) VALUES (%s, %s, %s, %s)"
            value = (nameRegLine, usernameRegLine, emailRegLine, passwordRegLine)
            mycursor.execute(insert, value)
            mydb.commit()
            self.loadMain()

    def loadMainApp(self):
        self.userDisplayLabel.setText(self.lgUserLine.text())
        self.mainWidget.setCurrentWidget(self.mainMenu_page)
        self.stackedWidget.setCurrentWidget(self.profile_page)

        self.cameraWidgets = [[self.camera1_label, self.allCam1_label],
                              [self.camera2_label, self.allCam2_label],
                              [self.camera3_label, self.allCam3_label],
                              [self.camera4_label, self.allCam4_label], ]

        # date and time = need to improve the time, should be running
        dateTime = datetime.datetime.now()
        self.dateDisplay_label.setText('%02d/%02d/%s' % (dateTime.month, dateTime.day, dateTime.year))

        # --- DATA HISTORY PAGE ---#
        self.comboClasses.addItems(['All', 'Without Both', 'Facemask Only', 'Faceshield Only'])
        # --- YEAR ---#
        self.comboYear.addItems(
            [('%s' % (dateTime.year)), '2021', '2022', '2023', '2024', '2025', '2026', '2077', '2028', '2029', '2030'])
        # --- MONTHS --- #
        self.comboMonth.addItems(
            [('%02d' % (dateTime.month)), '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])
        # --- DATES --- #
        self.comboDate.addItems([('%02d' % (dateTime.day)), '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13',
             '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
             '31'])

        # --- CODED BUTTONS IN ABLE TO SELECT A CERTAIN STACKED WIDGET PAGE --- #
        self.profileButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.profile_page))  # Profile button to Profile page
        self.surveillanceButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.surveillance_page))  # Surveillance Button to Surveillance page
        self.dataHistoryButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.dataHistory_page))  # Data history button to Data history page
        self.settingsButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.settings_page))  # settings button to settings page

        # --- PROFILE EDIT PAGE ---#
        self.editProfile_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.editProfile_page))  # Edit profile button to edit profile
        self.editProfile_button.clicked.connect(lambda: self.editProfileWidget.setCurrentWidget(self.editUser_page))
        self.editProfileBack_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.profile_page))  # -- CANCEL BUTTON --#

        # --- PROFILE EDIT STACKED WIDGETS ---#

        self.editUser_button.clicked.connect(lambda: self.editProfileWidget.setCurrentWidget(self.editUser_page))
        self.editNameOwner_button.clicked.connect(lambda: self.editProfileWidget.setCurrentWidget(self.editNameOwner_page))
        self.editStoreName_button.clicked.connect(lambda: self.editProfileWidget.setCurrentWidget(self.editStoreName_page))
        self.editStoreType_button.clicked.connect(lambda : self.editProfileWidget.setCurrentWidget(self.editStoreType_page))
        self.editAddress_button.clicked.connect(lambda: self.editProfileWidget.setCurrentWidget(self.editAddress_page))
        self.editCity_button.clicked.connect(lambda: self.editProfileWidget.setCurrentWidget(self.editCity_page))
        self.editCountry_button.clicked.connect(lambda: self.editProfileWidget.setCurrentWidget(self.editCountry_page))

        # --- SETTINGS PAGE WIDGETS ---#
        self.detectionSetup_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.detectionSetup_page))  # detection setup button from settings to detection setup page
        self.setupCCTV_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(
        self.setupCCTV_page))  # setup cctv button from setings to setup cctv page

        # --- DETECTION SETUP PAGE BUTTONS ---#
        self.dtSetupBack_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.settings_page))  # -- BACK BUTTON DETECTION SETUP, RETURNS TO SETTINGS PAGE ---#

        # --- SET THE PROFILE PAGE AS A DEFAULT PAGE AFTER LOGGING IN --- #
        self.setupCCTV_widget.setCurrentWidget(self.cctvAvailableConnect_page)

        # --- setupCCTV widgets ---#
        self.cancelSetup_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.settings_page))  # cancel setup cctv button, returns to setting page
        self.connectIP_button.clicked.connect(lambda: self.setupCCTV_widget.setCurrentWidget(self.connectIP_page))  # connect IP button to connect IP page
        self.continueConnectIP_button.clicked.connect(self.addCamera)  # continue to connect ip to cinnection view surveillance sucesss
        self.checkSurveillance_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.surveillance_page))  # check surveillance button redirect to surveillance.

        # --- SET THE "ALL CAMERA" PAGE AS A DEFAULT PAGE WHEN SELECTING THE SURVEILLANCE PAGE--- #
        self.surveillance_frame.setCurrentWidget(self.allCamera_page)

        # --- CODED BUTTONS FOR SURVEILLANCE PAGE --- #
        self.camera1_button.clicked.connect(lambda: self.surveillance_frame.setCurrentWidget(self.camera1_page))
        self.camera2_button.clicked.connect(lambda: self.surveillance_frame.setCurrentWidget(self.camera2_page))
        self.camera3_button.clicked.connect(lambda: self.surveillance_frame.setCurrentWidget(self.camera3_page))
        self.camera4_button.clicked.connect(lambda: self.surveillance_frame.setCurrentWidget(self.camera4_page))
        self.allCamera_button.clicked.connect(lambda: self.surveillance_frame.setCurrentWidget(self.allCamera_page))

        #go to displayProfile
        self.displayProfile()

    # def closeEvent(self, *args, **kwargs):
    #     super(QMainWindow, self).closeEvent(*args, **kwargs)
    #     self.stopDetection()

    # Add Camera method
    def addCamera(self):
        url = str(self.IPaddress_Line.text())
        url = url.strip()

        # Check the validity of the URL
        if len(url) == 0:
            print("URL length is 0")
        else:
            test_url = int(url) if url.isnumeric() else url
            test = cv2.VideoCapture(test_url)
            if test is None or not test.isOpened():
                print("Invalid URL")
                self.label_27.setStyleSheet("background-color: red")
                self.label_27.setText("Invalid URL/IP")
                self.setupCCTV_widget.setCurrentWidget(self.cctvConnectedView_page)
                self.connectedCameraOutput_label.clear()
            else:
                # self.detections[url] = detechYolo.Detech("DetechModel.pt", url, 640, "cpu", "CCTV", self.classes)
                self.detections.insert(self.activeCam,Camera(url, detechYolo.Detech("DetechModelS.pt", url, 640, "cpu", "CCTV",  classes=self.classes, selectedClass=self.selectedClass, user_id=self.user_id), self.cameraWidgets[self.activeCam], str(self.activeCam+1)))
                print("Success!")
                self.label_27.setStyleSheet("background-color: green")
                self.label_27.setText("Connected IP: " +str(url))

                # Display sample frame
                ret, frame = test.read()
                if ret: 
                    rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    h, w, ch = rgbImage.shape
                    bytesPerLine = ch * w
                    convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                    p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                    self.connectedCameraOutput_label.setPixmap(QPixmap.fromImage(p))

                time.sleep(1)
                # self.startDetection(self.detections[url], self.camera1_label)
                # thread1 = threading.Thread(target=self.startDetection, args=[self.detections[url]])
                # thread1.start()
                # thread2 = threading.Thread(target=self.displayDetection, args=[url])
                # thread2.start()
                # self.displayDetection(self.detections[url].frame)
                self.detections[self.activeCam].start()
                self.activeCam += 1
                self.setupCCTV_widget.setCurrentWidget(self.cctvConnectedView_page)


    # def startDetection(self, det):
    #     det.loadModel()
    #     det.loadData()
    #     det.startInference()

    def stopDetection(self):
        for detection in self.detections:
            detection.stop()
        print("Stopped")

    # def displayDetection(self, url):
    #     while True:
    #         frame = self.detections[url].frame
    #         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #         QImg = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
    #         pixMap = QPixmap.fromImage(QImg)
    #         pixMap = pixMap.scaled(416,640, Qt.KeepAspectRatio)
    #         self.camera1_label.setPixmap(pixMap)
    #         time.sleep(1)     


    def displayingInformation(self):
        self.show()

    def displayProfile(self):
        # Display profile
        username1 = self.userDisplayLabel.text()
        self.userDisplayLabel.setText(username1)
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
            self.nameDisplay_label.setText(row[1])
            self.nameStore_label.setText(row[5])
            self.typeStore_label.setText(row[6])
            self.storeAddDisplay_label.setText(row[7])
            self.cityDisplay_label.setText(row[8])
            self.countryDisplay_label.setText(row[9])
            self.editOwnerField.setText(row[1])
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
        self.dataHistorySetting_button.clicked.connect(self.showDialogDelete)
        self.logoutAccount_button.clicked.connect(self.showDialogLogout)
        self.faceMaskOnly_radioButton.clicked.connect(self.fmOnly)
        self.faceShieldOnly_radioButton.clicked.connect(self.fsOnly)
        self.facemaskFaceshield_radioButton.clicked.connect(self.both)
        self.sortButton.clicked.connect(self.selectDate)

        # buttons to display camera
        # self.camera1_button.clicked.connect(self.load)
        # self.surveillanceButton.clicked.connect(self.load)

    # def load(self):
    #     th = Thread(self)
    #     th.changePixmap.connect(self.setImage)
    #     th.start()
    #     self.show()

    # def setImage(self, image):
    #     self.camera1_label.setPixmap(QPixmap.fromImage(image))
    #     self.allCam1_label.setPixmap(QPixmap.fromImage(image))


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
            query = "UPDATE users SET password = %s  WHERE username = %s"
            value = (newPass, username1)
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

    def showDialogDelete(self):
        msgBoxDel = QMessageBox()
        msgBoxDel.setIcon(QMessageBox.Warning)
        msgBoxDel.setText("Are you sure you want to delete all saved images?")
        msgBoxDel.setWindowTitle("Delete Data History")
        msgBoxDel.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        returnValue = msgBoxDel.exec()
        if returnValue == QMessageBox.Yes:
            self.deleteAll()

    def deleteAll(self):
        # delete in database
        print("magdelete")
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="detech"
        )

        mycursor = mydb.cursor()
        query = f"SELECT * FROM violators WHERE {self.user_id} LIKE user_id"
        mycursor.execute(query)
        result = mycursor.fetchall()
        for row in result:
            print(f"Removed {row}")
            os.remove(row[5])

        mycursor = mydb.cursor()
        query = f"DELETE FROM violators WHERE {self.user_id} LIKE user_id"
        mycursor.execute(query)
        mydb.commit()

        #delete in file folder
        # dir = 'violators'
        # for file in os.scandir(dir):
        #     os.remove(file.path)



    def fmOnly(self):
        if self.faceMaskOnly_radioButton.isChecked():
            self.detectionChoice_label.setText("Face Mask Only")
            pixmap = QPixmap('images/fmonly.png')
            self.classes = [1,2,3]
            self.selectedClass = 1
            self.pictureDetectionSample_label.setPixmap(pixmap)
        else:
            self.detectionChoice_label.setText("")
        self.displayProfile()

    def fsOnly(self):
        if self.faceShieldOnly_radioButton.isChecked():
            self.detectionChoice_label.setText("Face Shield Only")
            pixmap = QPixmap('images/fsonly.png')
            self.classes = [2,3]
            self.selectedClass = 2
            self.pictureDetectionSample_label.setPixmap(pixmap)
        else:
            self.detectionChoice_label.setText("")
        self.displayProfile()

    def both(self):
        if self.facemaskFaceshield_radioButton.isChecked():
            self.detectionChoice_label.setText("Face Mask and Face Shield")
            pixmap = QPixmap('images/both.png')
            self.classes = [0, 1, 2, 3]
            self.selectedClass = 0
            self.pictureDetectionSample_label.setPixmap(pixmap)
        else:
            self.detectionChoice_label.setText("")
        self.displayProfile()

    def selectDate(self):
        year = self.comboYear.currentText()
        month = self.comboMonth.currentText()
        day = self.comboDate.currentText()
        violationType = self.comboClasses.currentText()
        dateSelected = year+"-"+month+"-"+day
        print(dateSelected, violationType)

        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="detech"
        )

        if violationType == "All":
            mycursor = mydb.cursor()
            query = "SELECT filename FROM violators WHERE '" + dateSelected + f"' LIKE date(detection_date) AND {self.user_id} LIKE user_id"
            mycursor.execute(query)
            result = mycursor.fetchall()
            filenames = [list(i) for i in result]
            print(filenames)
            number_of_images = len(filenames)
            print(number_of_images)

        else:
            mycursor = mydb.cursor()
            query = "SELECT filename FROM violators WHERE '" + dateSelected +"' LIKE date(detection_date) AND '" + violationType + f"' LIKE violation AND {self.user_id} LIKE user_id"
            mycursor.execute(query)
            result = mycursor.fetchall()
            filenames = [list(i) for i in result]
            print(filenames)
            number_of_images = len(filenames)
            print(number_of_images)

        self.widget = QWidget()
        self.formLayout = QFormLayout()
        count = 0
        if number_of_images % 2 == 0:
            while count < (number_of_images):
                object = QLabel("left")
                filepath = str(filenames[count])[2:-2]
                object.setPixmap(QPixmap(filepath))
                object.setFixedSize(465, 465)
                object.setScaledContents(True)
                count += 1

                object2 = QLabel("right")
                filepath2 = str(filenames[count])[2:-2]
                object2.setPixmap(QPixmap(filepath2))
                object2.setFixedSize(465, 465)
                object2.setScaledContents(True)
                count += 1

                self.formLayout.addRow(object, object2)
        else:
            #pag odd dito
            while count < (number_of_images):
                object = QLabel("left")
                filepath = str(filenames[count])[2:-2]
                object.setPixmap(QPixmap(filepath))
                object.setFixedSize(465, 465)
                object.setScaledContents(True)
                count += 1

                if count <= (number_of_images)-1:
                    object2 = QLabel("right")
                    filepath2 = str(filenames[count])[2:-2]
                    object2.setPixmap(QPixmap(filepath2))
                    object2.setFixedSize(465, 465)
                    object2.setScaledContents(True)
                    count += 1
                else:
                    object2 = QLabel()
                    object2.setFixedSize(465, 465)

                self.formLayout.addRow(object, object2)

        self.widget.setLayout(self.formLayout)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)


# class Thread(QThread):
#     changePixmap = pyqtSignal(QImage)

#     def run(self):
#         cap = cv2.VideoCapture(0)
#         while True:
#             ret, frame = cap.read()
#             if ret:
#                 # https://stackoverflow.com/a/55468544/6622587
#                 rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#                 h, w, ch = rgbImage.shape
#                 bytesPerLine = ch * w
#                 convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
#                 p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
#                 self.changePixmap.emit(p)


# Class that contains camera informations, detections, and methods

class Camera:
    def __init__(self, url, detech=detechYolo.Detech(), widget=None, name=None) -> None:
        self.url = url
        self.detech = detech
        self.widget = widget
        self.name = name
        self.frameWorker = threading.Thread(target=self.setDisplay, daemon=True)
        pass


    def start(self):
        self.detech.startInference()
        print("Displaying results in 5 secs")
        time.sleep(5)
        self.frameWorker.start()

    def stop(self):
        self.detech.stopInference()
        self.frameWorker.join()

    def setDisplay(self):
        while True:
            if self.detech.isDetecting:
                # print("Changing Display")
                frame = self.detech.frame
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                QImg = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                pixMap = QPixmap.fromImage(QImg)
                pixMap1 = pixMap.scaled(961,611, Qt.KeepAspectRatio)
                pixMap2 = pixMap.scaled(486,311, Qt.KeepAspectRatio)
                self.widget[0].setPixmap(pixMap1)
                self.widget[1].setPixmap(pixMap2)
            else:
                print("No display")
            cv2.waitKey(300)

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
loginWindow=mainPage()
loginWindow.show()
app.setWindowIcon(QtGui.QIcon('chip_icon_normal.png'))
app.exec_() #-- window execution --#