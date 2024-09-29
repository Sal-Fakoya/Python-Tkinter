
# This script is about entry widgets

"""
                    Entry Widget: Entry(master, options)
    options include:
        bg, bd, command, cursor, font, exportselection, fg, highlightcolor,
        justify, relief, selectbackground, selectborderwidth, selectforeground,show,
        state, textvariable, width, xscrollcommand, yscrollcomand

    Methods include:
        .delete(first=some_index, last=some_index)
        .get() : returns the entry's current text as a string
        .icursor(index) : sets the insertion cursor just before the character at the given index
        .index(index) : shifts the content of the entry so that the character at the given index is the left-most
                        visible character.
        .insert(index, s) : inserts a string "s" before a character at a given index.
        .select_adjust(index) : takes in one parameter and makes sure the selection includes the character at a
                                specified index
        .select_clear() : clears the selection. If there is no selection, select_clear() has no effect.
        .select_from(index) : takes in index and sets the anchor index position to the character selected by index
                            and selects that character
        .select_present(): if there is a selection, select_present returns boolean true or false
        .select_range(start, end): sets the selection under the program control. It selects the text starting at the
                                    index up to but not including the character at the end index.
        .select_to(index) : selects all the text from the anchor position up to but not including
                            the character at the given index
        .xview(index) : useful in linking the entry widget to a horizontal scrollbar.
        .xview_scroll(number, what) : used to scroll the entry in the horizontal direction.
                                    number=+ve to scroll from left to right.
                                    number=-ve to scroll from right to left.
"""

from tkinter import *

root = Tk()
root.geometry("200x200")

label1 = Label(master=root, text="Username")

label1.pack(side=LEFT)

entry1 = Entry(master=root, bd=5, show="*")
entry1.pack(side=RIGHT)
# entry1.insert(0, "Password: ")
# entry1.delete(0, 6)
s = entry1.get()
print(s)



root.mainloop()
















