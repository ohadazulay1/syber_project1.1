# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstWindowdis.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from signUpWin2 import Ui_SignUp
from clientt import Client
import sys


class Ui_firstWindow(object):
    def __init__(self):
        self.c = Client()
        app = QtWidgets.QApplication(sys.argv)
        self.firstWindow = QtWidgets.QMainWindow()
        #ui = Ui_firstWindow()
        self.setupUi()
        self.firstWindow.show()
        sys.exit(app.exec_())

    def setupUi(self):
        self.firstWindow.setObjectName("firstWindow")
        self.firstWindow.resize(3395, 1499)
        self.centralwidget = QtWidgets.QWidget(self.firstWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.signUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.signUpButton.setGeometry(QtCore.QRect(390, 650, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.signUpButton.setFont(font)
        self.signUpButton.setObjectName("signUpButton")
        self.welcomeLabel = QtWidgets.QLabel(self.centralwidget)
        self.welcomeLabel.setGeometry(QtCore.QRect(320, 110, 461, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.signInUpLabel = QtWidgets.QLabel(self.centralwidget)
        self.signInUpLabel.setGeometry(QtCore.QRect(540, 340, 321, 121))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.signInUpLabel.setFont(font)
        self.signInUpLabel.setObjectName("signInUpLabel")
        self.usernameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameInput.setGeometry(QtCore.QRect(680, 470, 113, 22))
        self.usernameInput.setObjectName("usernameInput")
        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(680, 500, 113, 22))
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setObjectName("passwordInput")
        self.signInButton = QtWidgets.QPushButton(self.centralwidget)
        self.signInButton.setGeometry(QtCore.QRect(830, 480, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.signInButton.setFont(font)
        self.signInButton.setObjectName("signInButton")
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(540, 460, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")

        self.wrongUsernameOrPassword = QtWidgets.QLabel(self.centralwidget)
        self.wrongUsernameOrPassword.setGeometry(QtCore.QRect(540, 430, 500, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.wrongUsernameOrPassword.setFont(font)
        self.wrongUsernameOrPassword.setObjectName("wrongUsernameOrPassword")

        self.empty = QtWidgets.QLabel(self.centralwidget)
        self.empty.setGeometry(QtCore.QRect(540, 430, 500, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.empty.setFont(font)
        self.empty.setObjectName("emptyTextBox")

        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(540, 490, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.ifItIsYourFirstTimeHereLabel = QtWidgets.QLabel(self.centralwidget)
        self.ifItIsYourFirstTimeHereLabel.setGeometry(QtCore.QRect(140, 650, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ifItIsYourFirstTimeHereLabel.setFont(font)
        self.ifItIsYourFirstTimeHereLabel.setObjectName("ifItIsYourFirstTimeHereLabel")
        self.picture = QtWidgets.QLabel(self.centralwidget)
        self.picture.setGeometry(QtCore.QRect(1290, 360, 501, 331))
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap("../../../.designer/backup/patches-smiley-face-happy-sad-venn_grande.webp"))
        self.picture.setObjectName("picture")
        self.wigglyFaceCaption = QtWidgets.QLabel(self.centralwidget)
        self.wigglyFaceCaption.setGeometry(QtCore.QRect(990, -10, 581, 331))
        font = QtGui.QFont()
        font.setFamily("Vivaldi")
        font.setPointSize(72)
        font.setItalic(True)
        font.setUnderline(True)
        self.wigglyFaceCaption.setFont(font)
        self.wigglyFaceCaption.setObjectName("wigglyFaceCaption")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1130, 320, 651, 371))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(
            "../../OneDrive/תמונות/forProject/patches-smiley-face-happy-sad-venn_grande.webp"))
        self.label.setObjectName("label")
        self.firstWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.firstWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 3395, 26))
        self.menubar.setObjectName("menubar")
        self.firstWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.firstWindow)
        self.statusbar.setObjectName("statusbar")
        self.firstWindow.setStatusBar(self.statusbar)

        self.retranslateUi(self.firstWindow)
        self.signUpButton.clicked.connect(self.signUpButtonPressed)
        self.signInButton.clicked.connect(self.signInPressed)


        QtCore.QMetaObject.connectSlotsByName(self.firstWindow)

    def retranslateUi(self, firstWindow):
        _translate = QtCore.QCoreApplication.translate
        firstWindow.setWindowTitle(_translate("firstWindow", "MainWindow"))
        self.signUpButton.setText(_translate("firstWindow", "sign up"))
        self.welcomeLabel.setText(_translate("firstWindow", "Welcome!"))
        self.signInUpLabel.setText(_translate("firstWindow", "please sign in:"))
        self.signInButton.setText(_translate("firstWindow", "sign in"))
        self.usernameLabel.setText(_translate("firstWindow", "username:"))
        self.empty.setText(_translate("firstWindow", "your username or password is empty, write one and login"))
        self.empty.hide()
        self.wrongUsernameOrPassword.setText((_translate("firstWindow", "your username or password are incorrect, please try loggin in again")))
        self.wrongUsernameOrPassword.hide()
        self.passwordLabel.setText(_translate("firstWindow", "password:"))
        self.ifItIsYourFirstTimeHereLabel.setText(_translate("firstWindow", "If it is your first time here:"))
        self.wigglyFaceCaption.setText(_translate("firstWindow", "wiggly face"))

#    def addLabel(self, firstWindow):
 #       _translate = QtCore.QCoreApplication.translate
  #      firstWindow.setWindowTitle(_translate("firstWindow", "MainWindow"))
   #     font = QtGui.QFont()
    #    font.setPointSize(16)
     #   self.misstakeLabel.setFont(font)
      #  self.misstakeLabel.setObjectName("misstakeLabel")
       # self.misstakeLabel = QtWidgets.QLabel(self.centralwidget)
        #self.misstakeLabel.setGeometry(QtCore.QRect(200, 480, 151, 31))
        #self.misstakeLabel.setText(_translate("firstWindow", "the username or the password is not correct"))

    def signUpButtonPressed(self):
        self.firstWindow.hide()
        self.signUpWin = QtWidgets.QMainWindow()
        self.ui = Ui_SignUp()
        self.ui.setupUi(self.signUpWin)
        self.signUpWin.show()

    def signInPressed(self):
        print("userName: " + self.usernameInput.text())
        print("password: " + self.passwordInput.text())
        if self.usernameInput.text() == '' or self.passwordInput.text() == '':
            self.wrongUsernameOrPassword.hide()
            self.empty.show()
        #if self.passwordInput.text() == '':
         #   self.empty.show()
        else:
            isInDB = self.c.login(self.usernameInput.text(), self.passwordInput.text())
            if isInDB:
                self.firstWindow.hide()
                app = QtWidgets.QApplication(sys.argv)
                sys.exit(app.exec_())
            else:
                self.empty.hide()
                self.wrongUsernameOrPassword.show()

#if __name__ == "__main__":
    #app = QtWidgets.QApplication(sys.argv)
    #firstWindow = QtWidgets.QMainWindow()
    #ui = Ui_firstWindow()
    #ui.setupUi(firstWindow)
    #firstWindow.show()
    #sys.exit(app.exec_())
 #   w = Ui_firstWindow()