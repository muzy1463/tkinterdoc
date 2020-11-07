from tkinter import *

alphabet = {"A":0, "B":1,"C":2, "D":3, "E":4, "F": 5, "G": 6, "H": 7, "I": 8, "J":9, "K": 10, "L": 11, "M": 12, "N": 13, "O":14, "P": 15, "Q": 16, "R": 17, "S":18,"T":19,"U":20, "V":21, "W":22, "X" : 23, "Y": 24, "Z":25}
alphabet_reverse = {0:"A", 1:"B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J", 10: "K", 11: "L", 12: "M", 13: "N",14: "O", 15: "P", 16: "Q" , 17: "R", 18: "S",19: "T",20: "U", 21: "V", 22: "W", 23: "X", 24: "Y", 25: "Z"}
root = Tk()
root.title("Muzy Password Generator")

def generate():
    x = (e.get()).upper()
    e.delete(0, END)
    y = ""
    for i in x:

        if i == " ":
            pass

        elif alphabet[i] <= 22:
            y = y + alphabet_reverse[alphabet[i] + 3]
        else:
            y = y + alphabet_reverse[alphabet[i] - 26 + 3]

    e.insert(0, y)

myLabel1 = Label(root, text = "Please enter your password below. We will encode it.")
myLabel1.grid(row=0,column=0)


e = Entry(root, width = 50, borderwidth = 5)
e.grid(row = 1, column = 0)

myButton = Button(root, text = "Generate", command = generate, fg = "black", bg = "white")
myButton.grid(row = 3, column = 0)

myLabel2 = Label(root, text = """All the feedbacks are appreciated:
mustafa.bodur@metu.edu.tr""")
myLabel2.grid(row=2,column=0)










root.mainloop()