# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("background: #696562")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 801, 581))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.userLogin = QtWidgets.QLineEdit(self.page)
        self.userLogin.setGeometry(QtCore.QRect(270, 210, 281, 50))
        self.userLogin.setStyleSheet("QLineEdit{\n"
"background: white;\n"
"border-radius: 20px;\n"
"padding: 10px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid black;\n"
"\n"
"}\n"
"QLineEdit:focus{border: 2px solid black;}")
        self.userLogin.setObjectName("userLogin")
        self.passwordLogin = QtWidgets.QLineEdit(self.page)
        self.passwordLogin.setGeometry(QtCore.QRect(270, 280, 281, 50))
        self.passwordLogin.setStyleSheet("QLineEdit{\n"
"background: white;\n"
"border-radius: 20px;\n"
"padding: 10px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid black;\n"
"\n"
"}\n"
"QLineEdit:focus{border: 2px solid black;}")
        self.passwordLogin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLogin.setObjectName("passwordLogin")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(340, 70, 131, 111))
        self.label_2.setStyleSheet("background: transparent;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/Other/Icons/login_icon.png"))
        self.label_2.setObjectName("label_2")
        self.btn_loginpage = QtWidgets.QPushButton(self.page)
        self.btn_loginpage.setGeometry(QtCore.QRect(270, 360, 281, 51))
        self.btn_loginpage.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background: red;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius: 20px;\n"
"background: #49ebff;\n"
"}")
        self.btn_loginpage.setObjectName("btn_loginpage")
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setGeometry(QtCore.QRect(0, 50, 0, 551))
        self.frame.setMinimumSize(QtCore.QSize(0, 551))
        self.frame.setMaximumSize(QtCore.QSize(150, 551))
        self.frame.setStyleSheet("background: #333130")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.login_btn = QtWidgets.QPushButton(self.frame)
        self.login_btn.setGeometry(QtCore.QRect(0, 0, 151, 41))
        self.login_btn.setStyleSheet("QPushButton{color: white;\n"
"background: transparent;}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid white;\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons_Menu/Icons/24x24/cil-home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_btn.setIcon(icon)
        self.login_btn.setIconSize(QtCore.QSize(24, 24))
        self.login_btn.setObjectName("login_btn")
        self.login_register = QtWidgets.QPushButton(self.frame)
        self.login_register.setGeometry(QtCore.QRect(0, 50, 151, 41))
        self.login_register.setStyleSheet("QPushButton{color: white;\n"
"background: transparent;}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid white;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons_Menu/Icons/24x24/cil-user-follow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_register.setIcon(icon1)
        self.login_register.setIconSize(QtCore.QSize(24, 24))
        self.login_register.setObjectName("login_register")
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setGeometry(QtCore.QRect(60, 0, 741, 51))
        self.frame_2.setStyleSheet("background: #333130")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.menuExpand_login = QtWidgets.QPushButton(self.page)
        self.menuExpand_login.setGeometry(QtCore.QRect(0, 0, 61, 51))
        self.menuExpand_login.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid white\n"
"}")
        self.menuExpand_login.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons_Menu/Icons/24x24/cil-list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuExpand_login.setIcon(icon2)
        self.menuExpand_login.setIconSize(QtCore.QSize(24, 24))
        self.menuExpand_login.setObjectName("menuExpand_login")
        self.error_login = QtWidgets.QLabel(self.page)
        self.error_login.setGeometry(QtCore.QRect(270, 190, 271, 16))
        self.error_login.setStyleSheet("background: transparent;\n"
"color: red;")
        self.error_login.setText("")
        self.error_login.setAlignment(QtCore.Qt.AlignCenter)
        self.error_login.setObjectName("error_login")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.frame_4 = QtWidgets.QFrame(self.page_2)
        self.frame_4.setGeometry(QtCore.QRect(0, 50, 150, 551))
        self.frame_4.setStyleSheet("background: #333130")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 50, 151, 41))
        self.pushButton_3.setStyleSheet("QPushButton{color: white;\n"
"background: transparent;}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid white;\n"
"}")
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.return_login = QtWidgets.QPushButton(self.frame_4)
        self.return_login.setGeometry(QtCore.QRect(0, 0, 151, 41))
        self.return_login.setStyleSheet("QPushButton{color: white;\n"
"background: transparent;}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid white;\n"
"}")
        self.return_login.setIcon(icon)
        self.return_login.setIconSize(QtCore.QSize(24, 24))
        self.return_login.setObjectName("return_login")
        self.userRegister = QtWidgets.QLineEdit(self.page_2)
        self.userRegister.setGeometry(QtCore.QRect(280, 310, 281, 50))
        self.userRegister.setStyleSheet("QLineEdit{\n"
"background: white;\n"
"border-radius: 20px;\n"
"padding: 10px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid black;\n"
"\n"
"}\n"
"QLineEdit:focus{border: 2px solid black;}")
        self.userRegister.setObjectName("userRegister")
        self.passwordRegister = QtWidgets.QLineEdit(self.page_2)
        self.passwordRegister.setGeometry(QtCore.QRect(280, 380, 281, 50))
        self.passwordRegister.setStyleSheet("QLineEdit{\n"
"background: white;\n"
"border-radius: 20px;\n"
"padding: 10px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid black;\n"
"\n"
"}\n"
"QLineEdit:focus{border: 2px solid black;}")
        self.passwordRegister.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordRegister.setObjectName("passwordRegister")
        self.confirmRegister = QtWidgets.QLineEdit(self.page_2)
        self.confirmRegister.setGeometry(QtCore.QRect(280, 450, 281, 50))
        self.confirmRegister.setStyleSheet("QLineEdit{\n"
"background: white;\n"
"border-radius: 20px;\n"
"padding: 10px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid black;\n"
"\n"
"}\n"
"QLineEdit:focus{border: 2px solid black;}")
        self.confirmRegister.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmRegister.setObjectName("confirmRegister")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(340, 70, 131, 111))
        self.label_3.setStyleSheet("background: transparent\n"
"")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/Other/Icons/login_icon.png"))
        self.label_3.setObjectName("label_3")
        self.menuExpand_register = QtWidgets.QPushButton(self.page_2)
        self.menuExpand_register.setGeometry(QtCore.QRect(0, 0, 61, 51))
        self.menuExpand_register.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid white\n"
"}")
        self.menuExpand_register.setText("")
        self.menuExpand_register.setIcon(icon2)
        self.menuExpand_register.setIconSize(QtCore.QSize(24, 24))
        self.menuExpand_register.setObjectName("menuExpand_register")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(60, 0, 741, 51))
        self.label_4.setStyleSheet("background: #333130")
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.nameRegister = QtWidgets.QLineEdit(self.page_2)
        self.nameRegister.setGeometry(QtCore.QRect(280, 240, 281, 50))
        self.nameRegister.setStyleSheet("QLineEdit{\n"
"background: white;\n"
"border-radius: 20px;\n"
"padding: 10px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid black;\n"
"\n"
"}\n"
"QLineEdit:focus{border: 2px solid black;}")
        self.nameRegister.setObjectName("nameRegister")
        self.error_register = QtWidgets.QLabel(self.page_2)
        self.error_register.setGeometry(QtCore.QRect(280, 180, 261, 16))
        self.error_register.setStyleSheet("background: transparent;\n"
"color: red;")
        self.error_register.setText("")
        self.error_register.setAlignment(QtCore.Qt.AlignCenter)
        self.error_register.setObjectName("error_register")
        self.btn_registerpage_2 = QtWidgets.QPushButton(self.page_2)
        self.btn_registerpage_2.setGeometry(QtCore.QRect(280, 520, 281, 51))
        self.btn_registerpage_2.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background: red;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius: 20px;\n"
"background: #49ebff;\n"
"}")
        self.btn_registerpage_2.setObjectName("btn_registerpage_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.user_menu = QtWidgets.QFrame(self.page_3)
        self.user_menu.setGeometry(QtCore.QRect(0, 50, 150, 531))
        self.user_menu.setStyleSheet("background: #333130")
        self.user_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.user_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.user_menu.setObjectName("user_menu")
        self.btn_search = QtWidgets.QPushButton(self.user_menu)
        self.btn_search.setGeometry(QtCore.QRect(0, 0, 150, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_search.setFont(font)
        self.btn_search.setToolTipDuration(1)
        self.btn_search.setStyleSheet("QPushButton{color: white;\n"
"background: transparent;}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid white;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons_Geral/Icons/Geral/search_b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_search.setIcon(icon3)
        self.btn_search.setIconSize(QtCore.QSize(32, 32))
        self.btn_search.setObjectName("btn_search")
        self.btn_balance = QtWidgets.QPushButton(self.user_menu)
        self.btn_balance.setGeometry(QtCore.QRect(0, 50, 150, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_balance.setFont(font)
        self.btn_balance.setStyleSheet("QPushButton{color: white;\n"
"background: transparent;}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid white;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons_Geral/Icons/Geral/balance_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_balance.setIcon(icon4)
        self.btn_balance.setIconSize(QtCore.QSize(48, 48))
        self.btn_balance.setObjectName("btn_balance")
        self.pushButton_5 = QtWidgets.QPushButton(self.user_menu)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 490, 150, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{color: white;\n"
"background: transparent;}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid white;\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Icons_Geral/Icons/Geral/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon5)
        self.pushButton_5.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_5.setObjectName("pushButton_5")
        self.inputSearch = QtWidgets.QLineEdit(self.page_3)
        self.inputSearch.setGeometry(QtCore.QRect(310, 60, 411, 31))
        self.inputSearch.setStyleSheet("QLineEdit{\n"
"background: white;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid black;\n"
"\n"
"}\n"
"QLineEdit:focus{border: 2px solid black;}")
        self.inputSearch.setText("")
        self.inputSearch.setObjectName("inputSearch")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(225, 60, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{\n"
"background: transparent;\n"
"color: white\n"
"}")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page_3)
        self.label_6.setGeometry(QtCore.QRect(150, 40, 61, 51))
        self.label_6.setStyleSheet("background: transparent")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/Icons_Geral/Icons/Geral/Search.png"))
        self.label_6.setObjectName("label_6")
        self.frame_5 = QtWidgets.QFrame(self.page_3)
        self.frame_5.setGeometry(QtCore.QRect(60, 0, 741, 51))
        self.frame_5.setStyleSheet("background: #333130")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.pushButton = QtWidgets.QPushButton(self.page_3)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 61, 51))
        self.pushButton.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid white\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(24, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_2.setGeometry(QtCore.QRect(730, 55, 64, 41))
        self.pushButton_2.setStyleSheet("QPushButton{color: white;\n"
"background: transparent;}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid white;\n"
"}")
        self.pushButton_2.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Icons_Geral/Icons/Geral/ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon6)
        self.pushButton_2.setIconSize(QtCore.QSize(64, 64))
        self.pushButton_2.setObjectName("pushButton_2")
        self.user_menu.raise_()
        self.label_5.raise_()
        self.frame_5.raise_()
        self.label_6.raise_()
        self.pushButton.raise_()
        self.inputSearch.raise_()
        self.pushButton_2.raise_()
        self.stackedWidget.addWidget(self.page_3)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 580, 801, 21))
        self.frame_3.setStyleSheet("background: #333130")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 20))
        self.label.setStyleSheet("color: white")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.userLogin.setPlaceholderText(_translate("MainWindow", "USER"))
        self.passwordLogin.setPlaceholderText(_translate("MainWindow", "PASSWORD"))
        self.btn_loginpage.setText(_translate("MainWindow", "LOGIN"))
        self.btn_loginpage.setShortcut(_translate("MainWindow", "Return"))
        self.login_btn.setText(_translate("MainWindow", "HOME"))
        self.login_register.setText(_translate("MainWindow", "REGISTER"))
        self.pushButton_3.setText(_translate("MainWindow", "REGISTER"))
        self.return_login.setText(_translate("MainWindow", "HOME"))
        self.userRegister.setPlaceholderText(_translate("MainWindow", "USER"))
        self.passwordRegister.setPlaceholderText(_translate("MainWindow", "PASSWORD"))
        self.confirmRegister.setPlaceholderText(_translate("MainWindow", "CONFIRM PASSWORD"))
        self.nameRegister.setPlaceholderText(_translate("MainWindow", "YOUR NAME"))
        self.btn_registerpage_2.setText(_translate("MainWindow", "REGISTER"))
        self.btn_search.setText(_translate("MainWindow", "HOME"))
        self.btn_balance.setText(_translate("MainWindow", "BALANCE"))
        self.pushButton_5.setText(_translate("MainWindow", "LOGOUT"))
        self.label_5.setText(_translate("MainWindow", "SEARCH:"))
        self.label.setText(_translate("MainWindow", "Created by: Alexandre D. ~ xand.douglass@gmail.com"))
import ic_rc
