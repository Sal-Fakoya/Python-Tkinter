
# This script is about geometry management in tkinter gui

"""
Geometry management: have the purpose of organizing parent throughout the widget area
    Geometry management methods:
        --> .pack() : organizes the widget in blocks before placing them in the parent widget
        --> .grid() : organized the widget in a table-like structure in a parent widget
        --> .place()


"""

import tkinter
from tkinter import *


# -----------------------------------------------------------
# .pack() : some_widget.pack(pack_options)
#     --> pack_options can be: expand = True or False,
#                                       fill = x, fill = y
#                                       side = "top", "bottom", "left", "right"
root = Tk()
# frame = Frame(root)
# frame.pack()
#
# button_frame = Frame(root)
# button_frame.pack(side=BOTTOM)
#
# red_button = Button(master=frame, text="red", fg="red")
# red_button.pack(side=LEFT)
#
# green_button = Button(master=frame, text="green", fg="green")
# green_button.pack(side=LEFT)
#
# blue_button = Button(master=frame, text="blue", fg="blue")
# blue_button.pack(side=LEFT)
#
# black_button = Button(master=button_frame, text="black", fg="black")
# black_button.pack(side=BOTTOM)


# -----------------------------------------------------------------------
# .grid() : widget.grid(grid_options)
#     grid_options: column, columnspan, ipadx, ipady, padx, pady, row, rowspan, sticky

for r in range(3):
    for c in range(4):
        label = Label(root, text=f"R{r}/C{c}", borderwidth=1)
        label.grid(row=r, column=c)




# ----------------------------------------------------------------------------
# .place() : widget.place(place_options) : places objects in a specific position in a parent window
#       place_options include:
#           --> anchor, bordermode, height, width, relwidth, relheight, relx, rely, x, y

button = Button(master=root,
                text="Hi")

button.place(x=100, y=100) # x = 20, y = 20 is button position


root.mainloop()





