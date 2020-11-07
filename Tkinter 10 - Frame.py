from tkinter import *

root = Tk()
root.title("Frame")




frame = LabelFrame(root, text = "This is my Frame...", padx = 5, pady = 5)
frame.pack(padx = 10, pady = 10)

b = Button(frame, text = "Don't Click Here!")
b.pack()

root.mainloop()