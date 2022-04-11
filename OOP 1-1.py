from tkinter import *
window = Tk()

window.geometry("500x400+30+20")
window.title("Welcome to Python Programming")

#add button widget

btn = Button(window, text="add name!", fg="black")
btn.place(x=80, y=100)

#add label widget

lbl = Label(window, text="Student Personal Information", fg="black", bg="light blue")
lbl.place(x=80, y=50)
lbl2 = Label(window, text="Gender:", fg="black")
lbl2.place(x=80, y=150)

#Add text field widget

txtfld = Entry(window, bd=3, font=("verdana", 16))
txtfld.place(x=150, y=100)

#add radio button

v1 = StringVar()
v2 = StringVar()
r1 = Radiobutton(window, text="Male", value=v1)
r1.place(x=150, y=150)

r2 = Radiobutton(window, text="Female", value=v2)
r2.place(x=250, y=150)

v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
chckbx1 = Checkbutton(window, text="Basketball", variable=v3)
chckbx2 = Checkbutton(window, text="Tennis", variable=v4)
chckbx3 = Checkbutton(window, text="Swimming", variable=v5)

chckbx1.place(x=80, y=230)
chckbx2.place(x=210, y=230)
chckbx3.place(x=320, y=230)

lbl3 = Label(window, text="Sports:")
lbl3.place(x=80, y=200)
lbl4 = Label(window, text="Subject:")
lbl4.place(x=80, y=280)

var = StringVar()
var.set("arithmetic")
data1 = "arithmetic"
data2 = "reading"
data3 = "writing"
lstbox = Listbox(height=4, selectmode='single')
lstbox.insert(END, data1, data2, data3)
lstbox.place(x=150, y=285)

window.mainloop()
