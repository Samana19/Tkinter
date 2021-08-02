from tkinter import*

root=Tk()

root.title('Calculator')
root.iconbitmap('calculator.ico')

quit_button=PhotoImage(file='C:\Users\hp\Desktop\nezuko.jpg')
img_label=Label(image=quit_button)
img_label.pack(pady=20)


my_image=ImageTk.PhotoImage(Image.open('calcu.jpg'))
my_label=Label(image=my_image)
my_label.pack()


root.mainloop()

