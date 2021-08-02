from tkinter import*
#place() geometry
top=Tk()

top.geometry("400x250")
name=Label(top, text="Name").place(x=30,y=60)
name1=Entry(top).place(x=80,y=60)

address=Label(top, text="Address").place(x=30,y=90)
address1=Entry(top).place(x=80,y=90)

contact=Label(top, text="Contact").place(x=30,y=120)
contact1=Entry(top).place(x=80,y=120)

top.mainloop()