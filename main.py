from tkinter import *


def temperature_celsius():
    pass


def temperature_fahrenheit():
    pass


root = Tk()

root.geometry("500x150")
root.title("Temperature Convertor")

label_text = StringVar()

cels = Label(root, text="Celsius To Fahrenheit").grid(row=0, column=1, sticky=W)
fahr = Label(root, text="Fahrenheit to Celsius").grid(row=0, column=3, sticky=W)

e1 = Entry(root)
e2 = Entry(root)

act_cels = Button(root, text="Activate - Celsius to Fahrenheit")
act_fahr = Button(root, text="Activate - Fahrenheit to Celsius")
conver = Button(root, text="Calculate Conversion")
clear = Button(root, text="Clear")
fin = Button(root, text="Exit")

mainloop()
