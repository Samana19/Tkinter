from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
root=Tk()
root.title("Dropdown Menu")

def show():
    mylabel=Label(root,text=clicked.get()).pack()

clicked=StringVar()
clicked.set("Monday")

drop=OptionMenu(root,clicked,"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
drop.pack()

mybutton=Button(root,text="Show selection", command=show).pack()

mainloop()