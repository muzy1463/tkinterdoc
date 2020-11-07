from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Muzybuzzy")

my_img = ImageTk.PhotoImage(Image.open("a.png"))
my_label = Label(image = my_img)
my_label.pack()




button_quit = Button(root, text = "EXIT PROGRAM", command = root.quit)
button_quit.pack()


root.mainloop()
