from tkinter import *
from PIL import ImageTk, Image

root = Tk()
r = IntVar()
r.set("2")


def change(number):
    myLabel = Label(root, text=number)
    myLabel.pack()

Radiobutton(root, text = "Option 1", variable = r, value = 1, command = lambda: change(1)).pack()
Radiobutton(root, text = "Option 2", variable = r, value = 2, command = lambda: change(2)).pack()
Radiobutton(root, text = "Option 3", variable = r, value = 3, command = lambda: change(3)).pack()
Radiobutton(root, text = "Option 4", variable = r, value = 4, command = lambda: change(4)).pack()
Radiobutton(root, text = "Option 5", variable = r, value = 5, command = lambda: change(5)).pack()

myLabel = Label(root, text = r.get())
myLabel.pack()

myButton = Button(root, text= "Click me!", command = lambda: change(1))
myButton.pack()

root.mainloop()
