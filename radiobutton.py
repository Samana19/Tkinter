from tkinter import*
root=Tk()

root.geometry("450x250")
root.title('MENU')

def function(value):
    label=Label(root,text=value)

    label.pack()

MENU=[
    ("Pizza","Pizza"),
    ("Burger","Burger"),
    ("Fries","Fries"),
    ("Drinks","Drinks")
]

food=StringVar()
food.set("Pizza")

for text, mode in MENU:
    Radiobutton(root,text=text,variable=food, value=mode).pack(anchor=W)

button=Button(root,text="Order",command=lambda:function(food.get())).pack()

root.mainloop()