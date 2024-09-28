

"""
            Button Syntax:
btn = Button(master, option = value)
    master : window where the button will be added
    where option can be:
        activebackground
        activeforeground
        bd for borderwidth in px
        bg : normal background color
        command
        fb : normal foreground text color
        font : text font used for the button label
        height : height of the button in text lines or px
        Highlightcolor
        image : image to be displayed on the button instead of text
        justify : to center, left-justify or right-justify
        padx : additional padding left and right of the text
        pady : additional padding above and below the text
        relief : specifies the type of the border e.g sunken
        state : to set the state of the button
        underline :
        width : width of the button in px
        wraplength : set to +ve number

                                Button Methods:
        flash: causes the button to flash
        invoke: calls the button's callback

"""
from tkinter import *
from tkinter import ttk

root = Tk()

button = ttk.Button(master = root,
                    text = "Button #1")

button.pack() # adjusts button to the screen

root.mainloop() # runs the code on the root window





























