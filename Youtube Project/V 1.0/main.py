import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import designer
from scripts import *


class Main(QMainWindow, designer.Ui_MainWindow):
    def __init__(self, parent = None ) -> None:
        super().__init__(parent)
        super().setupUi(self)



if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app_open = Main()
    app_open.show()
    qt.exec_()