
# This script is about tkinter scale

"""
                tkinter Scale: Scale(master=, options): provides graphical object that allows you to select object to scale
--> options include:
    activebackground, bg, bd, command, cursor, digits, fonts, fg (color of text used for labels and annotations),
    from_ (float or integer value that defines one end of the scale's range), highlightbackground,
    highlightcolor, label, length (length of the scale widget, x= for horizontal widget or y= for vertical widget),
    orient (sets the scale to horizontal or vertical), relief, repeatdelay (controls how long the button has to be
    held down before the slider starts moving in the direction repeatedly), resolution, showvalue (shows the current
    value of the scale), sliderlength (normally the slider is 30px to the left of the scale), state, takefocus,
    tickinterval (displays the tickinterval at the interval the slider should move), troughcolor, to, variable, width

                Scale Methods:
--> .get() : returns current value of the scale
--> .set() : sets the value of the scale
"""

from tkinter import *

root = Tk()
root.geometry("500x500")

var = DoubleVar()
var.set(50)

def sel():
    global var
    selection = f"Value : {var.get()}"
    label.config(text=selection)


scale = Scale(master=root, variable=var, from_=20, to=100, orient=HORIZONTAL,
              tickinterval=10, sliderlength=100,
              length=500)
scale.pack(anchor=CENTER)

button = Button(master=root, text="Get Scale Value", command=sel)
button.pack(anchor=CENTER)

label = Label(master=root)
label.pack()

root.mainloop()
































