from tkinter import *
from tkinter import messagebox


from PIL import ImageTk, Image

def popup():
    response = messagebox.askyesno("This is my Popup!", "Hello World!")
    Label(root, text = response).pack()

    if response == 1:
        Label(root, text= "You clicked yes!").pack()
    else:
        Label(root, text="You clicked no!").pack()
    #showinfo, showWarning, showerror, askquestion, askokcancel, askyesno



"""def popup2():
    messagebox.showwarning("This is my Popup!", "Hello World!")
    #showinfo, showWarning, showerror, askquestion, askokcancel, askyesno

def popup3():
    messagebox.showerror("This is my Popup!", "Hello World!")
    # showinfo, showWarning, showerror, askquestion, askokcancel, askyesno

def popup4():
    messagebox.askquestion("This is my Popup!", "Hello World!")

def popup5():
    messagebox.askokcancel("This is my Popup!", "Hello World!")

def popup6():
    messagebox.askyesno("This is my Popup!", "Hello World!")"""
root = Tk()
root.title("Muzzybuzzy")

Button(root, text = "Popup", command = popup).pack()

"""Button(root, text = "Popup2", command = popup2).pack()

Button(root, text = "Popup3", command = popup3).pack()

Button(root, text = "Popup4", command = popup4).pack()

Button(root, text = "Popup5", command = popup5).pack()

Button(root, text = "Popup6", command = popup6).pack()
"""


root.mainloop()


