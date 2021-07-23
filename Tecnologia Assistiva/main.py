import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import designer, icons_rc
from PyQt5.QtCore import QPropertyAnimation, QRect



class Ui_start(QMainWindow, designer.Ui_MainWindow):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.op = []
        #Definindo Botões
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.create_op.clicked.connect(lambda: self.get_op())
        self.op_save.clicked.connect(lambda: self.toggleMenu_Login(self.op_selecionada1.y(),1,self.op_selecionada1.width(),131,True))
        self.op_save_2.clicked.connect(lambda: self.toggleMenu_Login(self.op_selecionada2.y(),2,self.op_selecionada2.width(),131,True))
        self.op_save_3.clicked.connect(lambda: self.toggleMenu_Login(self.op_selecionada3.y(),3,self.op_selecionada3.width(),131,True))
        self.op_save_4.clicked.connect(lambda: self.toggleMenu_Login(self.op_selecionada4.y(),4,self.op_selecionada4.width(),131,True))
        self.op_save_5.clicked.connect(lambda: self.toggleMenu_Login(self.op_selecionada5.y(),5,self.op_selecionada5.width(),131,True))
        self.op_save_6.clicked.connect(lambda: self.toggleMenu_Login(self.op_selecionada6.y(),6,self.op_selecionada6.width(),131,True))

        #Verificando se arquivo conf.ini já existe e inserindo dados dele na Interface
        try:
            with open('conf.ini','r') as arquivo:
                #Salvando as opções do arquivo em variáveis
                op_saves = []
                lines = arquivo.readlines()
                for line_saves in lines:
                    line_saves = line_saves.strip('\n')
                    if line_saves == '':
                        line_saves = 'Vazio'
                    op_saves.append(line_saves)
            #Caso o arquivo exista, ir direto para página da aplicação
            self.edit_op(op_saves[0],op_saves[1],op_saves[2],op_saves[3],op_saves[4],op_saves[5])
            print(op_saves)
            self.stackedWidget.setCurrentWidget(self.page_2)
        except:
            self.create_op.clicked.connect(lambda: self.get_op())
        
    def get_op(self):
        x = 0
        i = 0
        for i in range(6):
            self.op.append('')
            i += 1
        self.op[0] = self.op_1.text()
        self.op[1] = self.op_2.text()
        self.op[2] = self.op_3.text()
        self.op[3] = self.op_4.text()
        self.op[4] = self.op_5.text()
        self.op[5] = self.op_6.text()
        for self.op[x] in self.op:
            if self.op[x] == '':
                self.op[x] = ''
            x += 1
        self.salve_file(self.op[0],self.op[1],self.op[2],self.op[3],self.op[4],self.op[5])
        self.stackedWidget.setCurrentWidget(self.page_2)
        self.edit_op(self.op[0],self.op[1],self.op[2],self.op[3],self.op[4],self.op[5])
    
    def salve_file(self,op1,op2,op3,op4,op5,op6):
        with open('conf.ini', 'w') as arquivo:
            arquivo.write(op1+"\n")
            arquivo.write(op2+"\n")
            arquivo.write(op3+"\n")
            arquivo.write(op4+"\n")
            arquivo.write(op5+"\n")
            arquivo.write(op6+"\n")
    
    def edit_op(self,op1,op2,op3,op4,op5,op6):
        self.op_save.setText(op1)
        self.op_save_2.setText(op2)
        self.op_save_3.setText(op3)
        self.op_save_4.setText(op4)
        self.op_save_5.setText(op5)
        self.op_save_6.setText(op6)
        ##As opções clicladas
        self.op_selecionada1.setText(op1)
        self.op_selecionada2.setText(op2)
        self.op_selecionada3.setText(op3)
        self.op_selecionada4.setText(op4)
        self.op_selecionada5.setText(op5)
        self.op_selecionada6.setText(op6)


    def toggleMenu_Login(self,position,id_op,select_op, maxWidth,enable):
            if enable:
                #GET WIDTH
                y_position = position
                width = select_op
                maxExtend = maxWidth
                standard = 0

                #SET AX WIDTH
                if width == 0:
                    widthExtended = maxExtend
                else:
                    widthExtended = standard

                #Animation
                if id_op == 1:
                    self.animation = QPropertyAnimation(self.op_selecionada1, b"geometry")
                if id_op == 2:
                    self.animation = QPropertyAnimation(self.op_selecionada2, b"geometry")
                if id_op == 3:
                    self.animation = QPropertyAnimation(self.op_selecionada3, b"geometry")
                if id_op == 4:
                    self.animation = QPropertyAnimation(self.op_selecionada4, b"geometry")
                if id_op == 5:
                    self.animation = QPropertyAnimation(self.op_selecionada5, b"geometry")
                if id_op == 6:
                    self.animation = QPropertyAnimation(self.op_selecionada6, b"geometry")
                self.animation.setDuration(600)
                self.animation.setStartValue(QRect(0, y_position, width, 41))
                self.animation.setEndValue(QRect(0, y_position, widthExtended, 41))
                self.animation.start()

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app_open = Ui_start()
    app_open.show()
    qt.exec_()