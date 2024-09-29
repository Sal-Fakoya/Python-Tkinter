
# This script is about tkinter Toplevel widget

"""
            tkinter Toplevel: Toplevel(options)
--> work as windows that are directly managed by the windows manager. They do not necessarily
    have a parent widget, so a tkinter application can use any number of Toplevel windows.

--> options include:
        bg, bd, cursor, class_ (Normally, text selected within a text widget is exported to be the selection in the
        window manager. Set class_ = 0 if you don't want the behaviour), font, fg, height, relief, width

--> Methods include:
        .deiconify() : displays the window after using eith iconify or the withdraw methods
        .frame() : returns a system specific window identifier.
        .group(window) : adds a window to the window group that is administered by the given window
        .iconify() : turns the window into an icon
        .protocol(name, function) : registers a function as a callback which will be called for the given protocol
        .state : returns the current state of the given window e.g normal, iconic, withdrawn and icon
        .transient(master) : takes in parameter master and turns the window into a temporary transient window
                            for the given master or to the windows parennt when no argument is given to the function.
        .withdraw(start, end) : removes the window from the screen without destroying that window
        .maxsize(width, height) : sets the maximum size for the window
        .minsizze(width, height):  sets the minimum size for the window
        .positionfrom(who) : defines the position controller
        .reseizable(width, height) : controls the resize flag which control whether the window can be resized or not
        .sizefrom(who) : defines the size controller
        .title(string) : defines the window's title
"""

from tkinter import *


root = Tk()
root.geometry("200x200")

top = Toplevel()
top.title("Top Level Window")
top.mainloop()

root.mainloop()

