from tkinter import *

root=Tk()

button1=Button(root, text="Left",fg="purple",bg="pink")
button1.pack(side=LEFT)

button2=Button(root, text="Right",fg="red",bg="pink")
button2.pack(side=RIGHT)

button3=Button(root, text="Top",fg="blue",bg="violet")
button3.pack(side=TOP)

button4=Button(root, text="Bottom",fg="black",bg="violet")
button4.pack(side=BOTTOM)

root.mainloop()
