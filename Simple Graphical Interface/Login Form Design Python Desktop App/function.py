import sqlite3
from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5 import QtGui
import main
import designer
from passlib.hash import pbkdf2_sha256

#DataBase
class DataMain:
    def __init__(self):
        self.verify = False
        self.exists = False

    def createdb(self):
        #Connect DB
        self.connection = sqlite3.connect('data_base.db')
        self.cursor = self.connection.cursor()

        #CREATE TABLE clients AND items
        self.cursor.execute('CREATE TABLE IF NOT EXISTS clients('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'username STR,'
        'password STR,'
        'name STR,'
        'balance INT,'
        'purchaseditems STR'
        ')')
        self.connection.commit()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS items('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'name STR,'
        'information STR,'
        'price INT,'
        'amount,'
        'owner '
        ')')
        self.connection.commit()
        #Close DB
        self.cursor.close()
        self.connection.close()
#############################################################
    def verify_user(self, usr, passw):
        self.connection = sqlite3.connect('data_base.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('SELECT username,password FROM clients')
        self.connection.commit()
        for i,x in self.cursor.fetchall():
            i = str(i)
            if i == usr:
                if pbkdf2_sha256.verify(passw, x):
                    #User and Pass = Exist
                    self.verify = True
                    self.cursor.close()
                    self.connection.close()
                    return
        self.cursor.close()
        self.connection.close()

    def user_register(self, usr_confirm):
        usr_confirm = (usr_confirm)
        self.connection = sqlite3.connect('data_base.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('SELECT username,password FROM clients')
        for x,z in self.cursor.fetchall():
            x = str(x)
            usr_confirm = str(usr_confirm)
            #print(usr_confirm)
            if x == usr_confirm:
                self.exists = True
                return

#############################################################
    def insert_user(self, usr, passw, name):
        #Conect to DB
        self.connection = sqlite3.connect('data_base.db')
        self.cursor = self.connection.cursor()
        #Insert data in DB
        self.cursor.execute('INSERT INTO clients (username, password, name, balance, purchaseditems) VALUES (?,?,?,0,?)', (usr, passw, name, None))
        self.connection.commit()
        #CloseDB
        self.cursor.close()
        self.connection.close()


#Animation -> Menu Expand or Reduce
class UiFunction_menu(main.AppB): 
    ##TOGGLE MENU
    def toggleMenu_Login(self, maxWidth, enable):
        if enable:
            #GET WIDTH
            width = self.frame.width()
            maxExtend = maxWidth
            standard = 0

            #SET AX WIDTH
            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            #Animation
            self.animation = QPropertyAnimation(self.frame, b"geometry")
            self.animation.setDuration(400)
            self.animation.setStartValue(QRect(0, 50, width, 551))
            self.animation.setEndValue(QRect(0, 50, widthExtended, 551))
            self.animation.start()


    def toggleMenu_Register(self, maxWidth, enable):
        if enable:
            #GET WIDTH
            width = self.frame_4.width()
            maxExtend = maxWidth
            standard = 0

            #SET AX WIDTH
            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            #Animation
            self.animation = QPropertyAnimation(self.frame_4, b"geometry")
            self.animation.setDuration(400)
            self.animation.setStartValue(QRect(0, 50, width, 551))
            self.animation.setEndValue(QRect(0, 50, widthExtended, 551))
            self.animation.start()




class Login_and_Register(main.AppB):
    def login(self):
        intologin = DataMain()
        intologin.verify_user(self.userLogin.text(),self.passwordLogin.text())
        if intologin.verify == True:
            self.stackedWidget.setCurrentWidget(self.page_3)
        else:
            self.error_login.setText(
                "Username or password is incorrect "
            )
    def registerConfirm(self):
        intoRegister = DataMain()
        intoRegister.user_register(self.userRegister.text())
        if intoRegister.exists == False:
            if self.passwordRegister.text() == self.confirmRegister.text():
                if self.passwordRegister.text() == '' or self.userRegister.text() == '' or self.nameRegister.text() == '':
                    self.error_register.setText("Blank space")
                else:
                    encrypt_pass = pbkdf2_sha256.hash(self.passwordRegister.text(), rounds = 200000, salt_size = 16)
                    intoRegister.insert_user(self.userRegister.text(),encrypt_pass, self.nameRegister.text())
                    self.stackedWidget.setCurrentWidget(self.page)
                    self.error_login.setText("Account successfully created")
            else:
                self.error_register.setText("Differents password")
        else:
            self.error_register.setText("User already exists")



