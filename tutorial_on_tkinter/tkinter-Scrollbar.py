
# This script is about Tkinter Scrollbar

"""
                    tkinter Scrollbar: Scrollbar(master=, options)
--> options include:
        activebackrgound, bg, bd, command (function to be called whenever the scroll bar is moved),
        cursor, elementborderwidth (default value is -1), highlightbackground, highlightcolor, highlightthickness,
        jump (controls what happens when a user drages the slider. Default value is set to 0. At jump=0, every small
        drag of the slider causes the command callback to be called. At jump=1, the callback is not called until the
        user releases the button), orient (orient=HORIZONTAL for horizontal scrollbar, orient=VERTICAL), repeatdelay
        (default value is 300 in milliseconds), takefocus, troughcolor, width

                        Scrollbar Methods:
--> .get() : returns two numbers, x and y, the position of the scrollbar
--> .set(first, last)
"""

from tkinter import *
from tkinter import ttk


root = Tk()
# set root size
root.geometry("200x200")

#  Create a scrollbar
scrollbar = Scrollbar(master=root)
# creates a listbox

scrollbar.pack(side=RIGHT, fill=Y)
# specify the geometry management for the scrollbar

# yscrollcommand=scrollbar.set: .set connects and sets the scrollbar to the listbox widget
my_list = Listbox(master=root, yscrollcommand=scrollbar.set)

for line in range(100):
    my_list.insert(END, f"This is line number {line}")

my_list.pack(side=LEFT, fill=BOTH)

# configures the scrollbar using the object through which the listbox is created.
scrollbar.config(command=my_list.yview)

root.mainloop()


























