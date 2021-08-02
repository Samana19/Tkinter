from tkinter import *

root=Tk()

def click():
    label=Label(root, text="Button was clicked")
    label.pack()

button1=Button(root, text="Click", command=click)
button1.pack()

root.mainloop()