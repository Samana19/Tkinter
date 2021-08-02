from tkinter import *
root=Tk()
name=Label(root,text="Name").grid(row=0,column=0)
name1=Entry(root).grid(row=0,column=1)

password=Label(root,text="Password").grid(row=1,column=0)
password1=Entry(root).grid(row=1,column=1)

submit=Button(root, text="Submit",fg="purple").grid(row=2,column=1)

root.mainloop()