from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("welcome")



def open():
    global my_image
    top = Toplevel()
    top.title("New window")
    my_image = ImageTk.PhotoImage(Image.open("koro.png"))
    my_label = Label(top, image=my_image)
    my_label.pack()
    btn = Button(top, text='Open new', command=open1).pack()
button = Button(root, text='Click here', command=open).pack()
def open1():
    global image1

    new = Toplevel()
    new.title("hello")
    image1 = ImageTk.PhotoImage(Image.open("nezuko.png"))
    label = Label(new, image=my_image).pack()
    button1 = Button(new, text='Exit', command=new.destroy).pack()




root.mainloop()
