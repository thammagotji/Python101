from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import pydirectinput as pi
import pyautogui as pg
import time
import math
import threading

class Fishing:

    def __init__(self):
        self.stop_thread=False
        print('Fishing Activated')            

    def track(self):
            pos3 = pg.locateOnScreen('C:\\Python311\\python101\\python101_project2\\fish1.jpg',confidence=0.7)      # fish on bar
            pos4 = pg.locateOnScreen('C:\\Python311\\python101\\python101_project2\\fish2.jpg',confidence=0.7)      # fish escaping
            pos5 = pg.locateOnScreen('C:\\Python311\\python101\\python101_project2\\fish3.jpg',confidence=0.7)      # fish off bar
            if pos3 is not None:
                pi.keyUp('c')
            elif pos4 is not None:
                pi.keyDown('c')
                time.sleep(0.2)
                pi.keyUp('c')
            elif pos5 is not None:
                pi.keyDown('c')
                time.sleep(0.2)
                pi.keyUp('c')

    def identify(self):         
        anchovy = pg.locateOnScreen('C:\\Python311\\python101\\python101_project2\\anchovy.jpg',region=(640,270,640,540),confidence=0.9)
        flounder = pg.locateOnScreen('C:\\Python311\\python101\\python101_project2\\flounder.jpg',region=(640,270,640,540),confidence=0.9)
        halibut = pg.locateOnScreen('C:\\Python311\\python101\\python101_project2\\halibut.jpg',region=(640,270,640,540),confidence=0.9)
        herring = pg.locateOnScreen('C:\\Python311\\python101\\python101_project2\\herring.jpg',region=(640,270,640,540),confidence=0.9)
        sardine = pg.locateOnScreen('C:\\Python311\\python101\\python101_project2\\sardine.jpg',region=(640,270,640,540),confidence=0.9)
        t = datetime.now().strftime('%H:%M:%S ')
        if anchovy is not None:
            T.insert(END, t+'anchovy caught'+'\n')      # displaying the fish's name in the textbox
            T.see(END)
            time.sleep(0.5)
            pi.press('c')
        elif flounder is not None:
            T.insert(END, t+'flounder caught'+'\n')
            T.see(END)
            time.sleep(0.5)
            pi.press('c')
        elif halibut is not None:
            T.insert(END, t+'halibut caught'+'\n')
            T.see(END)
            time.sleep(0.5)
            pi.press('c')
        elif herring is not None:
            T.insert(END, t+'herring caught'+'\n')
            T.see(END)
            time.sleep(0.5)
            pi.press('c')
        elif sardine is not None:
            T.insert(END, t+'sardine caught'+'\n')
            T.see(END)
            time.sleep(0.5)
            pi.press('c')
        else:
            T.insert(END, t+'the fish swam away'+'\n')
            T.see(END)

    def main(self):
        while not self.stop_thread:
            time.sleep(0.5)
            pi.keyDown('c')
            time.sleep(1)
            pi.keyUp('c')
            A = 0
            while A == 0:
                pos1 = pg.locateOnScreen('C:\\Python311\\python101\\python101_project2\\noti.jpg',confidence=0.7)
                if pos1 is not None:
                    pi.press('c')
                    A = 1
                    print('found!')
                    time.sleep(1.5)
                    pos2 = pg.locateOnScreen('C:\\Python311\\python101\\python101_project2\\tab.jpg',confidence=0.6)
                    if pos2 is not None:
                        print('fishing...')
                        while pos2 is not None:
                            pos2 = pg.locateOnScreen('C:\\Python311\\python101\\python101_project2\\tab.jpg',confidence=0.5)
                            f.track()
                        time.sleep(1)
                        print('fish caught')
                        f.identify()
                        
                    else:
                        print('trash')
                        seaweed = pg.locateOnScreen('C:\\Python311\\python101\\python101_project2\\seaweed.jpg',region=(640,270,640,540),confidence=0.8)
                        t = datetime.now().strftime('%H:%M:%S ')
                        if seaweed is not None:
                            T.insert(END, t+'obtain seaweed'+'\n')
                            T.see(END)
                            time.sleep(0.5)
                            pi.press('c')
                        else:
                            T.insert(END, t+'obtain trash'+'\n')
                            T.see(END)
                            time.sleep(0.5)
                            pi.press('c')
                        time.sleep(0.5)
                else:
                    print('waiting...')

    def stop(self):
        self.stop_thread = True     # Deactivate the bot
        pi.keyUp('c')

def Button1():
    T.insert(END,'---- Bot Initiated ----'+'\n')
    T.update()
    time.sleep(0.5)
    pg.click(960,540)
    global f
    f = Fishing() # create an instance of Fishing
    th = threading.Thread(target=f.main) # pass the Fishing instance and the main method to the Thread constructor
    th.start()

def Button2():
    T.insert(END,'---- Bot Deactivated ----'+'\n')
    T.update()
    T.see(END)
    f.stop()

GUI = Tk()
GUI.title('starfishbot gui interface')
GUI.geometry('300x300')

L1 = Label(GUI,text='Stardew Valley - Fishing bot',font=('Arial Black',12),fg='black')
L1.place(x=25,y=20)

FB1 = Frame(GUI)  
FB1.place(x=30,y=60)
B1 = ttk.Button(FB1,text='START',command=Button1)
B1.pack(ipadx=20,ipady=20)

FB2 = Frame(GUI)    
FB2.place(x=150,y=60)
B2 = ttk.Button(FB2,text='STOP',command=Button2)
B2.pack(ipadx=20,ipady=20)

L2 = Label(GUI,text='Fishing log:',font=('Arial',10),fg='black')
L2.place(x=30,y=145)
T = Text(GUI,height=6,width=30)
T.place(x=30,y=170)

GUI.mainloop()
