from tkinter import*
from tkinter import filedialog
from PIL import ImageTk, Image
root=Tk()
root.title("Hello")
root.iconbitmap("chopper.ico")

def open():
    global my_image
    root.filename=filedialog.askopenfilename(initialdir="/Downloads",
                                             title="Select a file",
                                             filetypes=(("png files", "*.png"),
                                                        ("all files", "*.*")))
    label=Label(root,text=root.filename).pack()
    my_image=ImageTk.PhotoImage(Image.open(root.filename))
    my_label=Label(image=my_image).pack()

my_button=Button(root, text="Open File", command=open).pack()

root.mainloop()