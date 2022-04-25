from tkinter import *

window = Tk()
window.geometry("600x400")
window.title("Midterm in OOP")


lbl1 = Label(window, text = "Enter your fullname:", fg="red")
lbl1.place(x= 40, y=100)

v1= StringVar()
v2= StringVar()

def Click():
    v2.set(v1.get())
txtfld1 = Entry(window,bd= 4, font = ("Verdana",15), textvariable=v1)
txtfld1.place(x= 260, y= 100)

txtfld2 = Entry(window,bd= 4, font = ("Verdana",15), textvariable=v2)
txtfld2.place(x= 260, y= 150)

btn1 = Button(window, text = "Click to display your fullname:", fg="red", command=lambda:Click())
btn1.place(x= 40, y= 155)



window.mainloop()