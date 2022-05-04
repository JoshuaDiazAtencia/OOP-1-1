from tkinter import *

window = Tk()
window.title("Simple Calculator")
window.geometry("400x300+20+10")

class MyWindow:
    def __init__(self, window):
        self.lbl1 = Label(window, text="Simple calculator")
        self.lbl1.grid(row=0, column=0, columnspan=3, sticky=W)

        self.lbl2 = Label(window, text="Enter 1st number:")
        self.lbl2.grid(row=1, column=0)
        self.txt2 = Entry(window, bd=3)
        self.txt2.grid(row=1, column=1)

        self.lbl3 = Label(window, text="Enter 2nd number:", bd=3)
        self.lbl3.grid(row=2, column=0)
        self.txt3 = Entry(window, bd=3)
        self.txt3.grid(row=2, column=1)

        self.btn1 = Button(window, text="addition", command=self.add)
        self.btn1.grid(row=3, column=0)
        self.btn1.bind("<Button-1>", self.add)

        self.btn2 = Button(window, text="subtraction", command=self.subtract)
        self.btn2.grid(row=3, column=1)
        self.btn2.bind("<Button-1>", self.subtract)

        self.btn3 = Button(window, text="multiplication", command=self.multiply)
        self.btn3.grid(row=3, column=2)
        self.btn3.bind("<Button-1>", self.multiply)

        self.btn4 = Button(window, text="division", command=self.divide)
        self.btn4.grid(row=3, column=3)
        self.btn4.bind("<Button-1>", self.divide)

        self.lblblnk = Label(window, text="", bd=3)
        self.lblblnk.grid(row=4, column=0)

        self.lbl4 = Label(window, text="Result:", bd=3)
        self.lbl4.grid(row=5, column=0)
        self.txt4 = Entry(window, bd=3)
        self.txt4.grid(row=5, column=1)


    def add(self):
        self.txt4.delete("0", END)
        num1 = int(self.txt2.get())
        num2 = int(self.txt3.get())
        answer = num1+num2
        self.txt4.insert(END, str(answer))

    def subtract(self):
        self.txt4.delete("0", END)
        num1 = int(self.txt2.get())
        num2 = int(self.txt3.get())
        answer = num1-num2
        self.txt4.insert(END, str(answer))

    def multiply(self):
        self.txt4.delete("0", END)
        num1 = int(self.txt2.get())
        num2 = int(self.txt3.get())
        answer = num1*num2
        self.txt4.insert(END, str(answer))

    def divide(self):
        self.txt4.delete("0", END)
        num1 = int(self.txt2.get())
        num2 = int(self.txt3.get())
        answer = num1/num2
        self.txt4.insert(END, str(answer))


mywin = MyWindow(window)
window.mainloop()
