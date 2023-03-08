from tkinter import *
from tkinter import ttk # theme
from tkinter import messagebox
from datetime import datetime
from tkinter import messagebox
from PIL import ImageTk, Image
import math

price_total1 = 0
price_total2 = 0
price_total3 = 0

##### csv #####
import csv

def writecsv(datalist):
    with open('sukiorder.csv','a',newline='') as file:
        fw = csv.writer(file)       # fw = file writer
        fw.writerow(datalist)       # datalist = ['pen','eraser']

def readcsv():
    with open('sukiorder.csv',newline='') as file:
        fr = csv.reader(file)       # fr = file reader
        data = list(fr)
        return data

# data = readcsv()
# print(data)
##### csv #####

GUI = Tk()
GUI.title('Information saving program')
GUI.geometry('500x700')

L1 = Label(GUI,text='Suki Teeyai',font=('Ariel Black',30))
L1.place(x=150,y=20)

canvas1 = Canvas(GUI,width=120,height=100)
canvas1.pack()
img1 = ImageTk.PhotoImage(Image.open("C:\Python311\python101\homework\pork.jpg"))
canvas1.create_image(55,50,image=img1)
canvas1.place(x=50,y=100)

canvas2 = Canvas(GUI,width=120,height=100)
canvas2.pack()
img2 = ImageTk.PhotoImage(Image.open("C:\\Python311\\python101\\homework\\beef.png"))
canvas2.create_image(55,50,image=img2)
canvas2.place(x=50,y=250)

canvas3 = Canvas(GUI,width=120,height=100)
canvas3.pack()
img3 = ImageTk.PhotoImage(Image.open("C:\\Python311\\python101\\homework\\veggy.jpg"))
canvas3.create_image(55,50,image=img3)
canvas3.place(x=50,y=400)

LF1 = ttk.LabelFrame(GUI,text='number of pork set')
LF1.place(x=200,y=100)
LF2 = ttk.LabelFrame(GUI,text='number of beef set')
LF2.place(x=200,y=250)
LF3 = ttk.LabelFrame(GUI,text='number of vegetables set')
LF3.place(x=200,y=400)

v_data1 = StringVar()        # special variable in GUI alphebetic input
E1 = ttk.Entry(LF1,textvariable=v_data1,font=('Angsana New',25))
E1.pack(pady=10,padx=10)
v_data2 = StringVar()
E2 = ttk.Entry(LF2,textvariable=v_data2,font=('Angsana New',25))
E2.pack(pady=10,padx=10)
v_data3 = StringVar()
E3 = ttk.Entry(LF3,textvariable=v_data3,font=('Angsana New',25))
E3.pack(pady=10,padx=10)

def Savedata():
    global price_total1,price_total2,price_total3
    t=datetime.now().strftime('%Y%m%d %H%M%S')
    sunkor=v_data1.get()         # record data in v_data
    price_total1 = price_total1+int(sunkor)*150
    beef=v_data2.get()
    price_total2 = price_total2+int(beef)*200
    veggy=v_data3.get()
    price_total3 = price_total3+int(veggy)*50
    text = [t, 'pork', sunkor,'beef', beef, 'vegetable', veggy]           # time+data
    writecsv(text)              # save in csv
    v_data1.set('')              # clear v_data
    v_data2.set('')
    v_data3.set('')
    text = 'Your order has been sent, we are now preparing your meal.'
    messagebox.showinfo('Order',text)

def Showdata():
    global price_total1,price_total2,price_total3
    t=datetime.now().strftime('%Y%m%d %H%M%S')
    text2 = [t, '-----order ended-----']
    order=readcsv()
    bill = price_total1+price_total2+price_total3
    print(bill)
    text3 = 'total meal cost = '+ str(bill)+ ' Baht.'
    writecsv(text2)
    messagebox.showinfo('Bill',text3)
    
Bf1 = ttk.LabelFrame(GUI)
Bf1.place(x=50,y=550)
Btn1 = ttk.Button(Bf1,text='order',command=lambda: Savedata())
Btn1.pack(ipadx=50,ipady=30)

Bf2 = ttk.LabelFrame(GUI)
Bf2.place(x=250,y=550)
Btn2 = ttk.Button(Bf2,text='bill',command=lambda: Showdata())
Btn2.pack(ipadx=50,ipady=30)


