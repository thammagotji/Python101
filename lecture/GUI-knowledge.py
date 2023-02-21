from tkinter import *
from tkinter import ttk # theme
from tkinter import messagebox

GUI = Tk()
GUI.title('Information saving program')
GUI.geometry('500x400')

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

GUI.mainloop()
