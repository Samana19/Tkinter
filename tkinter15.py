from tkinter import*
root=Tk()
root.title("Slider")
 #vertical slider
vertical=Scale(root,from_=0, to=450)
vertical.pack()
 #Horizontal slider
horizontal=Scale(root,from_=0,to=450, orient=HORIZONTAL)
horizontal.pack()

def slider():
    my_label=Label(root,text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))
my_btn=Button(root, text="Click me", command=slider).pack()


root.mainloop()