
# This script is about the tkinter Radiobutton

"""
                tkinter Radiobutton: Radibutton(master=, options)
--> options include:
    activebackground, activeforeground, anchor, bg, bitmap, borderwidth, command, cursor, font, fg
    height, highlightbackground, highlightcolor, image, justify, pady, padx, relief,
    selectcolor, selectimage, state, text, textvariable, underline, value, variable, width, wraplength

                    tkinter Radiobutton Methods
--> deselect()
--> flash()
--> invoke()
--> select()
"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("200x200")

var = IntVar()


def sel():
    global var
    selection = f"You have selected {var.get()}"
    label.config(text=selection)


r1 = Radiobutton(master=root, text="Option1", variable=var, value=1, command=sel)
r1.pack(anchor=W)

r2 = Radiobutton(master=root, text="Option2", variable=var, value=2, command=sel)
r2.pack(anchor=W)

r3 = Radiobutton(master=root, text="Option3", variable=var, value=3, command=sel)
r3.pack(anchor=W)

# r2.select()
r2.deselect()
r3.flash()
label = Label(master=root)
label.pack()

root.mainloop()


































