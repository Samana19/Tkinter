from tkinter import*
root=Tk()

button1=Button(root, text="Click Me",fg="purple",bg="pink")
button1.pack()
button2=Button(root, text="Click",fg="purple",bg="pink", state=DISABLED)
button2.pack()

button3=Button(root, text="Click",fg="purple",bg="pink",padx=50)
button3.pack()

button4=Button(root, text="Click",fg="purple",bg="pink",padx=50 ,pady=30)
button4.pack()

root.mainloop()
