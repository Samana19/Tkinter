from tkinter import*
from PIL import ImageTk, Image

root=Tk()
root.title("welcome")
root.iconbitmap('chopper.ico')

def open():
    global my_image
    top=Toplevel()
    top.title("New window")
    my_image = ImageTk.PhotoImage(Image.open("koro.png"))
    my_label=Label(top, image=my_image)
    my_label.pack()
    btn=Button(top,text='Exit', command=top.destroy ).pack()


button=Button(root,text='Click here', command=open ).pack()

root.mainloop()

