import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import designer
import function, ic_rc, sqlite3


class AppB(QMainWindow, designer.Ui_MainWindow):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)

        #Home page:
        self.login_page()

    def login_page(self):
        #Entering the Register Page #############################################################
        self.stackedWidget.setCurrentWidget(self.page) #
        #UIFunction #############################################################
        self.menuExpand_login.clicked.connect(lambda: function.UiFunction_menu.toggleMenu_Login(self, 150, True)) #Expand Menu or Reduce Menu
        #MENUButton #############################################################
        self.login_register.clicked.connect(self.register_page)
        #Function #############################################################
        self.btn_loginpage.clicked.connect(lambda: function.Login_and_Register.login(self))
        #self.stackedWidget.setCurrentWidget(self.page_3)
        

    def register_page(self):
        #Entering the Register Page #############################################################
        self.stackedWidget.setCurrentWidget(self.page_2) #
        #UIFunction #############################################################
        self.menuExpand_register.clicked.connect(lambda: function.UiFunction_menu.toggleMenu_Register(self, 150, True)) #Expand Menu or Reduce Menu
        #MENUButton #############################################################
        self.return_login.clicked.connect(self.login_page) #Return to Home Page
        #Function #############################################################
        self.btn_registerpage_2.clicked.connect(lambda: function.Login_and_Register.registerConfirm(self))

if __name__ == '__main__':
    insert_table = function.DataMain()
    insert_table.createdb()
    qt = QApplication(sys.argv)
    app_open = AppB()
    app_open.show()
    qt.exec_()