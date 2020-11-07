from tkinter import *
from PIL import ImageTk, Image

root = Tk()

MODES = [
    ("Pepperoni","P"),
    ("Cheese","C"),
    ("Mushroom","M"),
    ("Onion","O"),
    ("Margaritta","MA"),
]

pizza = StringVar()
pizza.set("P")

for text, mode in MODES:
    Radiobutton(root, text = text, variable = pizza, value = mode, anchor = W).pack()

def change(number):
    myLabel = Label(root, text=number)
    myLabel.pack()

myLabel = Label(root, text = pizza.get())
myLabel.pack()

myButton = Button(root, text= "Click me!", command = lambda: change(pizza.get()))
myButton.pack()

root.mainloop()
