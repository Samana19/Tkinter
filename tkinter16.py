from tkinter import*
root=Tk()
root.title("hello")

def show():
    mylabel=Label(root,text=var.get()).pack()

var=StringVar()

checkbtn=Checkbutton(root, text="check this box",
                     variable=var, onvalue="On",
                     offvalue="Off")
checkbtn.deselect()
checkbtn.pack()

myButton=Button(root, text="Show selection", command=show).pack()
mainloop()