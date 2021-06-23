import sys,os
from PyQt5.QtWidgets import QApplication, QMainWindow
import designer
import scripts


class Main(QMainWindow, designer.Ui_MainWindow):
    def __init__(self, parent = None ) -> None:
        super().__init__(parent)
        super().setupUi(self)
        #Set first page
        self.stackedWidget.setCurrentWidget(self.download_page)
        self.download_button_2.clicked.connect(lambda: self.download_start(self.addURL.text()))

    def download_start(self, url):
        if len(url) >= 11: #Verify valid URL
            link = scripts.Addurl(url)
            link.set_URL()
        else:
            print("error")



if __name__ == '__main__':
    try:
        os.makedirs("./downloads")
    except OSError:
        pass
    qt = QApplication(sys.argv)
    app_open = Main()
    app_open.show()
    qt.exec_()