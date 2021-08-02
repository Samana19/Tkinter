from tkinter import*pip
root=Tk()
hello=Entry(root,width=40,fg="",bg="white")
hello.pack()
def click():
    textoutput="Welcome " + name.get()
    lable=Label(root,text=textoutput)
    lable.pack()
button=Button(root,text='Submit', command=click)
button.pack()

root.mainloop()