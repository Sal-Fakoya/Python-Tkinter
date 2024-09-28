
# This script is about the tkinter Checkbutton

"""
                    Checkbutton: Checkbutton(master=, options)
--> activebackground
--> activeforeground
--> bg
--> bitmap : to display monochrome image on a button
--> bd : size of the border round the indicator. Default size is 2 px
--> command
--> cursor
--> font
--> disabledforegroundcolor
--> fg
--> height
--> highlightcolor
--> image : to display a graphic image on the button
--> justify
--> offvalue: set to 0 when clear
--> onvalue
--> padx, pady
--> relief
--> selectcolor: default color is red
--> selectimage
--> state: default value is normal
--> text: label displayed next to the check button
--> underline: default value of -1, none of the elements in the text are going to be underlined
--> variable: normally an int var where 0 means clear and 1 means set
--> width: default width of the button is determined by the size of the text or image displayed
--> wraplength

                        METHODS:
--> deselect
--> flash
--> invoke
--> select : to set or turn on the check button
--> toggle: inverts the state of the checkbutton

"""

from tkinter import *

root = Tk()

root.geometry('200x200')

check_btn_status = BooleanVar()
check_btn_status.set(True)

def func():
    print("check box")
check_btn = Checkbutton(master=root,
                        text="Check box",
                        variable=check_btn_status,
                        command=func)

check_btn.select()
check_btn.deselect()
check_btn.toggle() # inverts the state of the button
check_btn.grid(row=0, column=0)

root.mainloop()






























