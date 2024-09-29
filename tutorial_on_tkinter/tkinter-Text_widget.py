
from tkinter import *
"""
This script is a tutorial on the Tkinter Text Widget

"""

"""
                    tkinter Text Widget : Text(master=, options)
--> provides advanced capabilities that allows us to add a multi-line text 
and we can also use elegant structures like tabs and marks to locate specific sections of the text and 
apply changes to those areas. Moreover, you can embed windows and images because the Text widget is designed to 
handle both plain and formatted text.

--> options include:
        bg, bd. cursor, exportselection, font, fg (color used for text and bitmap within the region), 
        height (height of the widget in lines), highlightbackground, highlightcolor, highlightthickness, 
        insertbackground, insertborderwidth, insertofftime (number of milliseconds the insertion cursor is off. 
        Default time is 300), insertontime (number of milliseconds the insertion cursor is on during its blink cycle),
        insertwidth, padx, pady, relief (default value is SUNKEN), selectbackground, selectborderwidth, 
        spacing 1 (how much extra vertical space is put above each line of a text. If a line wraps, 
        this space is added only. Default value is 0), 
        spacing 2 (how much extra vertical space to add between displayed lines of text when a logical line wraps. 
        Default value is 0), 
        spacing 3 (how much extra vertical space to add below each line of a text. If a line wraps, this space is 
        added only after the last line it occupies on the display, and the default value is 0)
        state = ["Normal"], ["Disabled"], ["!disabled"]
        tabs, width, wrap (set wrap to a word and it will break after the last word that will fit),
        xscrollcommand, yscrollcommand
        
--> Methods include:
        .delete(start, end)
        .get(start, end)
        .index(index)
        .insert(index, string) : to insert a string at a specific index location
        .see(index) : returns True if the text located at the index location is visible
        .index(mark) : to bookmark positions between two characters within a given text
        .mark_gravity(mark, gravity) : returns the gravity of a given mark
        .mark_names() : is used to return all marks from the text widget set already
        .mark_set(mark, index) : is used to set the mark that takes in two parameters "mark" and "index" 
                                that informs a new position to the given mark
        .mark_unset(mark) : removes the given mark from the text widget
        .tag_add(tagname, start, end) : tags either the position that is defined by the start index, or a range 
                                        delimited by the positions: start index and end index
        .tag_config() : to configure the tag properties such as justify, tabs, underline
        .tag_delete(tagname) : used to delete and remove a given tag
        .tag_remove(tagname, start, end) : removes the given tag from the provided area without deleting 
                                            the actual tag definition
"""




root = Tk()
root.geometry("200x200")

text = Text(master=root, fg="red")
text.insert(INSERT, "Hello World\n")
text.insert(END, "Good Bye")
text.pack()

text.tag_add("tag", "1.0", "1.5")
text.tag_add("tag1", "1.7", "1.12")

text.tag_config("tag", background="#ED7CB0", foreground="white")
text.tag_config("tag1", background="#ED7CB0", foreground="white")
root.mainloop()



























