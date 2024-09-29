
# This script is about tkinter Menubutton and Menu

"""
                    tkinter Menubutton: Menubutton(master, options)
--> is used to creat drop down button.
--> options include:
    bg, activebackground, activeforeground, anchor, bg, bitmap, bd, cursor, direction (sets the direction: use
    direction=LEFT to display the menu to the left of the button, RIGHT, ABOVE),
    disabledforeground, fg (foreground color: when the mouse is not over the menu button),
    height (height of the menu button in lines of text), highlightcolor (color shown in the focus highlight when the
    widget has the focus), image (displays an image on the menubutton), justify (=LEFT, =CENTER, = RIGHT
    controls where the text is located),
    menu, padx, pady, state, relief, text, textvariable, underline, width, wraplength

"""

"""
                    tkinter Menu: Menu(master=
variable_name.menu = Menu(master=, option):
    option include:
        activebackground, activeborderwidth, activeforeground, bg, bd, cursor, disabledforeground, font, fg,
        postcommand (set this option to a procedure that gets called every time the menu is selected), relief,
        image, selectcolor, tearoff=0 (choices will be added starting at position zero), title
        
                    tkinter menu methods:
--> .add_command(options): adds a menu item to the menu
--> .add_radiobutton(options) : adds a radio button menu item
--> .add_checkbutton(options) : creates a checkbutton menu item
--> .add_cascade(options) : creates a new hierachical menu by associating a given menu to a parent menu
--> .add_separator() : add a separator line to the menu
--> .add(type, options) : adds a specific type of item to the menu
--> .delete(start, end) : deletes menu items ranging from start to end
--> .entryconfig(index, options) : allows you to modify menu items identified by index
--> .index(item) : returns the index number of the given item label
--> .insert_separator(index) : inserts a new separator at the position that is specified by the index parameter
--> .invoke(index) : calls the command callback associated with the choice at position index. if a check button, 
    the state is toggled between set and clear, if a radio button, the choice is set
--> .type(index) : returns the type of the choice specified by the index that can be either cascade, checkbutton, 
    command, radiobutton, a separator or a tearoff                               
"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("200x200")

# creating the main menu
menubar = Menu(master=root)

# creating the file menu
file_menu = Menu(master=menubar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_command(label="Close")
file_menu.add_separator()
file_menu.add_command(label="Exit")

# adding file_menu to the main menu bar
menubar.add_cascade(label="File", menu=file_menu)

# creating the edit menu
edit_menu = Menu(master=menubar, tearoff=0)
edit_menu.add_command(label="Undo")
edit_menu.add_separator()
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Delete")

# adding edit_menu to the main menu bar
menubar.add_cascade(label="Edit", menu=edit_menu)

# creating the help menu
help_menu = Menu(master=menubar, tearoff=0)
help_menu.add_command(label="Help Desk")
help_menu.add_command(label="About")
help_menu.add_command(label="Version Info")
help_menu.add_command(label="Online Help")

# adding help_menu to the main menu bar
menubar.add_cascade(label="Help", menu=help_menu)

# displaying the menu bar to the tkinter app
root.config(menu=menubar)

root.mainloop()


























