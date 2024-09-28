
# This script is on relief styles:

"""
    Relief Styles:
        --> flat
        --> Raised
        --> Sunken
        -- Groove
        --> Ridge

    Bitmaps: is used to display
        --> "error"
        --> "gray75"
        --> "gray50"
        --> "gray12"
        --> "hourglass"
        --> "info"
        --> "questhead"
        --> "question"
        --> "warning"

    Cursors:
        --> "arrow"
        --> "circle:
        --> "clock"
        --> "cross"
        --> "dotbox"
        --> "exchange"
        --> "fleur"
        --> "heart"
        --> "man"
        --> "mouse"
        --> "pirate"
        --> "spider"
        --> "trek"
        --> "watch"
        --> "sizing"
        --> "spraycan"
        --> "star"
"""

from tkinter import *
root = Tk()
b1 = Button(master=root, text="sunken_button", relief=SUNKEN, bitmap="error")
b1.place(x=10, y =10)

b2 = Button(master=root, text="groove", relief=GROOVE, bitmap="hourglass")
b2.place(x=20, y =40)

b2 = Button(master=root, text="ridge", relief=RIDGE, bitmap="questhead")
b2.place(x=30, y =70)

b2 = Button(master=root, text="ridge", relief=RIDGE, bitmap="gray50")
b2.place(x=30, y =100)

root.mainloop()
















