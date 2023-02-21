from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import math

gui = Tk()
gui.title('jan ken pon game')
gui.geometry('540x400')
gui.configure(bg='#060664')

head = Label(gui,text="JAN KEN PON !!",font=('Arial Black',30))
head.place(x=90,y=30)

jan = ImageTk.PhotoImage(Image.open("C:\Python311\jan.png"))
ken = ImageTk.PhotoImage(Image.open("C:\Python311\ken.png"))
pon = ImageTk.PhotoImage(Image.open("C:\Python311\pon.png"))

global score
score = 0

def janfunc():
    global score
    you = 1
    bot = random.randint(1,3)
    if bot==1:
        text = 'DRAW !!'
        messagebox.showinfo('Result',text)
    elif bot==2:
        text = 'YOU WIN !!'
        score = score+1
        label = Label(gui, text="Your Score: " + str(score), font=('Arial Black',20))
        label.place(x=165,y=320)
        messagebox.showinfo('Result',text)
    elif bot==3:
        
        text = 'YOU LOSE !!'
        score = score-1
        label = Label(gui, text="Your Score: " + str(score), font=('Arial Black',20))
        label.place(x=165,y=320)
        messagebox.showinfo('Result',text)

def kenfunc():
    global score
    you = 2
    bot = random.randint(1,3)
    if bot==2:
        text = 'DRAW !!'
        messagebox.showinfo('Result',text)
    elif bot==3:
        text = 'YOU WIN !!'
        messagebox.showinfo('Result',text)
        score = score+1
        label = Label(gui, text="Your Score: " + str(score), font=('Arial Black',20))
        label.place(x=165,y=320)
    elif bot==1:
        text = 'YOU LOSE !!'
        messagebox.showinfo('Result',text)
        score = score-1
        label = Label(gui, text="Your Score: " + str(score), font=('Arial Black',20))
        label.place(x=165,y=320)

def ponfunc():
    global score
    you = 3
    bot = random.randint(1,3)
    if bot==3:
        text = 'DRAW !!'
        messagebox.showinfo('Result',text)
    elif bot==1:
        text = 'YOU WIN !!'
        messagebox.showinfo('Result',text)
        score = score+1
        label = Label(gui, text="Your Score: " + str(score), font=('Arial Black',20))
        label.place(x=165,y=320)
    elif bot==2:
        text = 'YOU LOSE !!'
        messagebox.showinfo('Result',text)
        score = score-1
        label = Label(gui, text="Your Score: " + str(score), font=('Arial Black',20))
        label.place(x=165,y=320)

frame1 = Frame(gui)
frame1.place(x=40,y=150)
B1 = ttk.Button(frame1,image=jan,command=janfunc)
#B1 = ttk.Button(frame1,image=jan,command=lambda: label.config(text="Your Score: " + str(score)))
B1.pack(ipadx=10,ipady=10)

frame2 = Frame(gui)
frame2.place(x=200,y=150)
B2 = ttk.Button(frame2,image=ken,command=kenfunc)
B2.pack(ipadx=10,ipady=10)

frame3 = Frame(gui)
frame3.place(x=360,y=150)
B3 = ttk.Button(frame3,image=pon,command=ponfunc)
B3.pack(ipadx=10,ipady=10)

label = Label(gui, text="Your Score: " + str(score), font=('Arial Black',20))
label.place(x=165,y=320)

gui.mainloop()

