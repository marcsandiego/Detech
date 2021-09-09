import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import mysql.connector as mc
#---Import that will load the UI file---#
from PyQt5.uic import loadUi

import detechRs_rc #---THIS IMPORT WILL DISPLAY THE IMAGES STORED IN THE QRC FILE AND _rc.py FILE--#

#--CLASS CREATED THAT WILL LOAD THE UI FILE
class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        # --- FROM THE IMPORT PYQT5.UIC IMPORT LOADUI---##
        loadUi("login_UI.ui",self)

        # --- a code once the login button clicked, will call the loginFunction ---#
        self.loginButton.clicked.connect(self.loginFunction)

        # -- Created a function called "loginFunction" --#

    def loginFunction(self):
        lgUserLine = self.lgUserLine.text()  # -- Getting the textbox context lgUserline --#
        lgPassLine = self.lgPassLine.text()  # -- Getting the textbox context lgPassline --#

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
            self.labelResult.setText("Incorrect credentials")

        else:
            self.labelResult.setText("go to homepage")


app=QApplication(sys.argv)
loginWindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(loginWindow) #-- displays all design widgets of the UI Window --#
widget.setFixedWidth(1190) #-- setting the fixed window size in width --#
widget.setFixedHeight(782) #-- setting the fixed window size in height--#
widget.show()
app.exec_() #-- window execution --#