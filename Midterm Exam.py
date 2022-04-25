def main():
 class TemperatureConversion:
  def __init__(self, temp=1):
   self._temp = temp
 class CelsiusToFahrenheit(TemperatureConversion):
  def conversion(self):
   return (self._temp * 9) / 5 + 32
 class CelsiusToKelvin(TemperatureConversion):
  def conversion(self):
   return self._temp + 273.15

 tempInCelsius = float(input("Enter the temperature in Celsius: "))
 convert = CelsiusToKelvin(tempInCelsius)
 print(str(convert.conversion()) + " Kelvin")
 convert = CelsiusToFahrenheit(tempInCelsius)
 print(str(convert.conversion()) + " Fahrenheit")

main()


def main():
 class TemperatureConversion:
  def __init__(self, temp=1):
   self._temp = temp
 class FahrenheitToCelsius(TemperatureConversion):
  def conversion(self):
   return (self._temp -32)* 5/9

 tempInFar = float(input("\nEnter the temperature in Fahrenheit: "))
 convert = FahrenheitToCelsius(tempInFar)
 print(str(convert.conversion()) + " Celcius ")

main()

def main():
 class TemperatureConversion:
  def __init__(self, temp=1):
   self._temp = temp
 class KelvinToCelsius(TemperatureConversion):
  def conversion(self):
   return self._temp - 273.15

 tempInKel = float(input("\nEnter the temperature in Kelvin: "))
 convert = KelvinToCelsius(tempInKel)
 print(str(convert.conversion()) + " Celsius")

main()

import tkinter
from tkinter import*

window = Tk()
window.title("Midterm in OOP")
window.geometry("500x400")

lbl = Label(window, text="Enter your Fullname:", fg="red")
lbl.place(x=20, y=100)

txtfld = Entry(window, bd=3, font=("verdana", 16))
txtfld.place(x=200, y=100)

txtfld2 = Entry(window, bd=3, font=("verdana", 16))
txtfld2.place(x=200, y=220)

def clicked():
    value=txtfld.get()
    txtfld2.insert(END, str(value))

bttn= Button(window, text="Click to display your Fullname", fg="red", command=clicked)
bttn.place(x=20, y=220)

window.mainloop()