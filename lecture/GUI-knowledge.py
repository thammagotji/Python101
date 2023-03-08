from tkinter import *
from tkinter import ttk # theme
from tkinter import messagebox

##### csv #####
import csv

def writecsv(datalist):
    with open('data.csv','a',newline='') as file:
        fw = csv.writer(file)       # fw = file writer
        fw.writerow(datalist)       # datalist = ['pen','eraser']

def readcsv():
    with open('data.csv',newline='') as file:
        fr = csv.reader(file)       # fr = file reader
        data = list(fr)
        return data

data = readcsv()
print(data)
##### csv #####

GUI = Tk()
GUI.title('Information saving program')
GUI.geometry('800x400')

L1 = Label(GUI,text='My Shortnote',font=('Angsana New',20),fg='blue')
L1.place(x=30,y=20)

# B1 = ttk.Button(GUI,text='show money')
# B1.pack(ipadx=20,ipady=20)  # size button

# BUTTON2
def Button2():
    text = 'the walley currently has 200 baht'
    messagebox.showinfo('money',text)

FB1 = Frame(GUI)    # board
FB1.place(x=200,y=200)
B2 = ttk.Button(FB1,text='show money',command=Button2)
B2.pack(ipadx=20,ipady=20)

##### section write #####
LF1 = ttk.LabelFrame(GUI,text='type something')
LF1.place(x=400,y=50)

v_data = StringVar()        # special variable in GUI alphebetic input
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Angsana New',25))
E1.pack(pady=10,padx=10)

from datetime import datetime

def Savedata():
    t=datetime.now().strftime('%Y%m%d %H%M%S')
    data=v_data.get()       # record data in v_data
    text = [t,data]         # time+data
    writecsv(text)          # save in csv
    v_data.set('')          # clear v_data

B3 = ttk.Button(LF1,text='save',command=Savedata)
B3.pack(ipadx=20,ipady=20)



GUI.mainloop()
