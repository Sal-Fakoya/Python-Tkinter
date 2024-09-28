
"""
            Tkinter Canvas: is a rectangular layout for drawing and other complex layouts
--> canvas(master=, option=value)
    options include: bd (for borderwidth), bg, confine, width,
                    scrollregion, xscrollincrement, Xscrollcommand,
                    yscrollincrement, yscrollcommand, Cursor, height,
                    highlightcolor, relief,
--> Standard items supported by canvas widget:
        arc = (x_coord, y_coord), image (using the photoimage class),
        line (to create line item),
        oval (creates a circle or eclipse at the given coordinates),
        polygon (to create a polygon)

"""
from tkinter import *
root = Tk()

c = Canvas(master=root, bg="blue", height=250, width=300)

# creating an arc
coord = 10, 50, 200, 270
arc = c.create_arc(coord, start=0, extent=150, fill="white")
c.pack()

# creating a line
line = c.create_line(108, 120, 400, 17, fill="red")

# creating an oval
oval = c.create_oval(80, 30, 140, 150, fill="orange")

root.mainloop()



















