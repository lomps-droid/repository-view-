import pyautogui, sys
import time, serial
import _thread
import cv2

def print_percent_done(index, total, bar_len=50, title='Carregando'):
    '''
    index is expected to be 0 based index. 
    0 <= index < total
    '''
    percent_done = (index+1)/total*100
    percent_done = round(percent_done, 1)

    done = round(percent_done/(100/bar_len))
    togo = bar_len-done

    done_str = '█'*int(done)
    togo_str = '░'*int(togo)

    print(f'\t⏳{title}: [{done_str}{togo_str}] {percent_done}% Completo', end='\r')

    if round(percent_done) == 100:
        print('\t✅')


r = 50
for i in range(r):
    print_percent_done(i,r)
    time.sleep(.02)

ser = serial.Serial('COM3', 9600)
time.sleep(1)
print("After starting, open the interface and wait for the initial program ")
op = int(input("To start press 1: "))


def tasks(id):
    if id == 1:
        print("The program will start in 7s...")
        time.sleep(1)
        print("The program will start in 6s...")
        time.sleep(1)
        print("The program will start in 5s...")
        time.sleep(1)
        print("The program will start in 4s...")
        time.sleep(1)
        print("The program will start in 3s...")
        time.sleep(1)
        print("The program will start in 2s...")
        time.sleep(1)
        print("The program will start in 1s...")
        time.sleep(1)

        #Reconhecendo imagens e salvando posição das mesmas
        imagem_locale = False
        while imagem_locale == False:
            op_1 = pyautogui.locateOnScreen('.//images//search.png', confidence = 0.90)
            if op_1 != None:
                imagem_locale = True
                print("Localized Image \n")
            else:
                print("Trying to find image\n")

        #Movimentação do mouse
        while 1:
            pyautogui.moveTo(op_1)
            pyautogui.move(170,50)
            time.sleep(3)

            pyautogui.move(200,0)
            time.sleep(3)

            pyautogui.move(200,0)
            time.sleep(3)
            ##
            pyautogui.moveTo(op_1)
            ##
            pyautogui.move(170,200)
            time.sleep(3)

            pyautogui.move(180,0)
            time.sleep(3)

            pyautogui.move(190,0)
            time.sleep(3)


#Iniciando função em paralelo
_thread.start_new_thread(tasks, (1,))
can_close = 0
see_dados = 0
time.sleep(7)
while 1:
    dados = ser.readline()
    try:
        dados = int(ser.readline().decode().strip('\n\t'))
        if see_dados == 1:
            sys.stdout.write("\rSinal atual: %i"% dados)
            sys.stdout.flush()
        #Variável Click serve para permitir apenas 1 click por vez.
        if dados < 500 and click == 0:
            pyautogui.click()
            click = 1
        if dados > 500 and dados < 1000:
            #Após retornar o valor para 'normal' , é possível clicar novamente.
            click = 0
            can_close = 1
            see_dados = 1
        if dados == 1023 and can_close == 1:
            #Finalizando função
            break
    except:
        pass