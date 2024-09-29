# This script is about the tkinter listbox


"""
                tkinter Listbox: Listbox(master=, options)
--> option include:
    bg, bd, cursor, font, fg, height (number of lines not px), highlightcolor,
    highlightthickness, relief, selectbackground (background color for selected text),
    selectmode (how many items can be selected and how mouse drag affects selection such as browsemode, singlemode,
        mutliplemode, extended mode),
    width (width of the widget and characters),
    xscrollcommand : if you want list box to scroll horizontally
    yscrollcommand : if you want list box to scroll vertically

                tkinter Listbox Methods:
--> activate(index)
--> cursorselection() : returns a tuple containing the line number of the selected element(s)
--> delete(first=, last=)
--> get(first=, last=)
--> index(some_index)
--> insert(index, *elements)
--> nearest(y) : returns the index of the element closest to the y-coordinate while relative to the listbox
--> see(index): adjusts the position of the listbox so that the new line referred to by the index is visible
--> size() : returns the number of lines in the listbox
--> xview() : makes the listbox horizontally scrollable
--> xview_moveto(fraction) : scrolls the listbox so that the left most fraction (range of 0 to 1)
                            of the widget of the width of its longest line is outside the left side of the listbox
--> xview_scroll(number, what) : to scroll the listbox horizontally for the what argument to scroll by character or
                                pages, or units (to scroll by lines)
--> yview()
--> yview_moveto(fraction)
--> yview_scroll(number, what)
"""
from tkinter import *
from tkinter import ttk

root = Tk()

root.geometry("200x200")

lb = Listbox(master=root, bg="green")
lb.insert(1, "Python")
lb.insert(2, "Ruby")
lb.insert(3, "C")
lb.insert(5, "Java")
lb.insert(END, "Perl")
lb.insert(4, "C#")

lb.delete(first=0,last=3)

s = lb.size()
print(s)

lb.pack()

root.mainloop()
