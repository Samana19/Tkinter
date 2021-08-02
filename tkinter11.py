from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("popup window")

def function():
    response=messagebox.askyesno("Popup","Hello")
    Label(root,text=response).pack()

    if response==1:
        Label(root,text=)



button=Button(root,text="Popup",command=function).pack()
mainloop()
