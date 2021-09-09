import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

#---Import that will load the UI file---#
from PyQt5.uic import loadUi

import detechRs_rc #---THIS IMPORT WILL DISPLAY THE IMAGES STORED IN THE QRC FILE AND _rc.py FILE--#

#--CLASS CREATED THAT WILL LOAD THE UI FILE
class Register(QMainWindow):
    def __init__(self):
        super(Register, self).__init__()
        # --- FROM THE IMPORT PYQT5.UIC IMPORT LOADUI---##
        loadUi("register_UI.ui",self)

        #--- a code once the login button clicked, will call the loginFunction ---#
        self.registerButton.clicked.connect(self.registerFunction)

    #-- Created a function called "loginFunction" --#
    def registerFunction(self):
        nameRegLine=self.nameRegLine.text() #-- Getting the textbox context lgUserline --#
        usernameRegLine=self.usernameRegLine.text() #-- Getting the textbox context lgPassline --#
        emailRegLine = self.emailRegLine.text()  # -- Getting the textbox context lgPassline --#
        passwordRegLine = self.passwordRegLine.text()  # -- Getting the textbox context lgPassline --#
        confirmPasswordRegLine = self.confirmPasswordRegLine.text()  # -- Getting the textbox context lgPassline --#

        #-- Will display at the terminal what you wrote in the textbox(QLineEdit) --#
        print("Success Registration\n", nameRegLine,"\n", usernameRegLine,"\n", emailRegLine,"\n", passwordRegLine, "\n", confirmPasswordRegLine, "\n")



app=QApplication(sys.argv)
registerWindow=Register()
widget=QtWidgets.QStackedWidget()
widget.addWidget(registerWindow) #-- displays all design widgets of the UI Window --#
widget.setFixedWidth(1190) #-- setting the fixed window size in width --#
widget.setFixedHeight(782) #-- setting the fixed window size in height--#
widget.show()
app.exec_() #-- window execution --#