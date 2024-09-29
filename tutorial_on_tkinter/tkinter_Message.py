# This script is about the tkinter Message widget


"""
                    tkinter Message: Message(master=, options)
--> This widget displays a multi-line and non-editable object that displays text to the user.
    It automatically breaks lines and justify their content.
--> options include:
        anchor (specifies the position of the text if the widget has more space than the text name),
        bg, bitmap, bd, cursor, font, fg, height, image, justify, padx, pady, relief, text, textvariable (displays
        the var.set() message in the widget),
        underline, width (of the message bar in characters not px), wraplength
"""
from tkinter import *
from tkinter import ttk


root = Tk()

# create a string variable to store the message
var = StringVar()

label = Message(master=root, textvariable=var, relief=RAISED)
var.set("This is a tkinter message widget tutorial")

label.pack()
root.mainloop()







