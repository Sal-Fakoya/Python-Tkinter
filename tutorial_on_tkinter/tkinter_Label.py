# This script is about tkinter label:

"""
            tkinter label: Label(master=, options)
--> implements a display box where you can place text or images. Part of the text can also be underlined and spanned
across multiple lines.
--> options: bg, anchor: controls where the text is positioned, bg, bitmap, bd, cursor, font,
            fg (specifies the color of the text), height, image, justify padx, pady, relief,
            text, textvariable, underline (default is underline=-1 meaning no underline), width, wraplength (default
            is wraplength=0 meaning the lines will be broken only at new lines)
"""
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x500")

frame = Frame(master=root, bg="#EBC25E", padx=50, pady=15,
              highlightbackground="#7E77EB", highlightcolor="#EB6537",
              height=100, width=100, borderwidth=10, highlightthickness=10)

frame.pack(side=TOP)

label = Label(master=frame, anchor="center", background="#7E77EB",
              text="Eat this", underline=5, padx=15, pady=15,
              highlightthickness=10)
label.pack(side=TOP)

root.mainloop()






