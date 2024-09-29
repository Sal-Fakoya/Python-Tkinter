
# This script is on tkinter frames

"""
                    Frame: Frame(master=, options)
options include:
    bg, bd, cursor, height, highlightbackgroundcolor, highlightcolor, highlightthickness, relief, width

"""

from tkinter import *

root = Tk()
root.geometry("500x500")

frame = Frame(master=root, bg="#EB833A", bd=5, height=500, width=500)
# frame.grid(row=0, column=0)
frame.pack(side=RIGHT)

def callback():
    return "this button was clicked."

button = Button(master=frame, bd=5, command=callback, bg="#EBC25E", text="click me")

button.pack(side=RIGHT)

print(button)

root.mainloop()


















