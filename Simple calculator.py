from tkinter import *

window = Tk()
window.title("Super simple calculator")
window.geometry("400x300+20+10")

class MyWindow:
    def __init__(self, window):
        self.lbl1 = Label(window, text="Super standard calculator", fg="black")
        self.lbl1.place(relx=0.50, y=50, anchor="center")

        self.lbl2 = Label(window, text="Input 1st number")
        self.lbl2.place(x=50, y=80)

        self.lbl3 = Entry(window, bd=3)
        self.lbl3.place(x=180, y=80)

        self.lbl4 = Label(window, text="Input 2nd number")
        self.lbl4.place(x=50, y=120)

        self.lbl5 = Entry(window, bd=3)
        self.lbl5.place(x=180, y=120)

        self.btn1 = Button(window, text="addition", command=self.add)
        self.btn1.place(x=50, y=150)
        self.btn1.bind("<Button-1>", self.add)

        self.btn2 = Button(window, text="subtraction", command=self.sub)
        self.btn2.place(x=120, y=150)

        self.btn3 = Button(window, text="multiplication", command=self.mult)
        self.btn3.place(x=200, y=150)

        self.btn4 = Button(window, text="division", command=self.divd)
        self.btn4.place(x=300, y=150)

        self.lbl6 = Label(window, text="Result:")
        self.lbl6.place(x=50, y=200)

        self.lbl7 = Entry(window, bd=3)
        self.lbl7.place(x=100, y=200)

    def add(self):
        self.lbl7.delete("0", END)
        num1 = int(self.lbl3.get())
        num2 = int(self.lbl5.get())
        answer = num1+num2
        self.lbl7.insert(END, str(answer))

    def sub(self):
        self.lbl7.delete("0", END)
        num1 = int(self.lbl3.get())
        num2 = int(self.lbl5.get())
        answer = num1-num2
        self.lbl7.insert(END, str(answer))

    def mult(self):
        self.lbl7.delete("0", END)
        num1 = int(self.lbl3.get())
        num2 = int(self.lbl5.get())
        answer = num1*num2
        self.lbl7.insert(END, str(answer))

    def divd(self):
        self.lbl7.delete("0", END)
        num1 = int(self.lbl3.get())
        num2 = int(self.lbl5.get())
        answer = num1/num2
        self.lbl7.insert(END, str(answer))

mywin = MyWindow(window)
window.mainloop()
