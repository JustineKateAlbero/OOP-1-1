from tkinter import *
window = Tk()
window.geometry("500x40+30+20")
window.title("Welcome to Python Programming")

#add Button widget

btn = Button(window, text = "Click to add name", fg="blue")
btn.place(x= 80, y= 150)

#Add Label widget

lbl1 = Label(window, text = "Student's Personal Information", fg="blue", bg="orange")
lbl1.place(relx= .5, y=50, anchor ="center")

lbl2 = Label(window, text = "Gender", fg="pink", bg="black")
lbl2.place(x= 105, y=200, anchor ="center")



#Add text field widget

txtfld = Entry(window,bd= 3, font = ("verdana",16))
txtfld.place(x= 150, y= 150)

#Add radio button

v1 = StringVar()
v1.set(1)
r1 = Radiobutton(window,text="Male",value= v1)
r1.place(x= 120, y= 220)

v2 = StringVar()

r2 = Radiobutton(window,text="Female",value= v2)
r2.place(x= 180, y= 220)

#Add check box

lbl3 = Label(window, text = "Sports", fg="pink", bg="black")
lbl3.place(x= 105, y=300, anchor ="center")

v3 = IntVar()
v4 = IntVar()
v5 = IntVar()

chkbox = Checkbutton(window,text="basketball",variable=v3)
chkbox2 = Checkbutton(window,text="volleyball",variable=v4)
chkbox3 = Checkbutton(window,text="badminton",variable=v5)

chkbox.place(x= 120, y= 325)
chkbox2.place(x= 120, y= 350)
chkbox3.place(x= 120, y= 375)


#Add List box

lbl4 = Label(window, text = "Subjects", fg="pink", bg="black")
lbl4.place(x= 105, y=420, anchor ="center")

var = StringVar()
data1 = "CPEN 60"
data2 = "MATH 12"
data3 = "FITT 2"
data4 = "PHYS 14"
data5 = "DCEE 21"

lstbox = Listbox(window, height=5, selectmode="single")
#lstbox = Listbox(window, height=5, selectmode="multiple")
lstbox.insert(END,data1, data2, data3, data4, data5)
lstbox.place(x= 120, y= 450)


window.mainloop()