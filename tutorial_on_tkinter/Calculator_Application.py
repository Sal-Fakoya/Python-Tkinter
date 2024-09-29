# This is a Calculator application using python : and tkinter library
"""
1. Import necessary library
2. Create the driver code: set the GUI window, configurations, title and geometry for the main GUI window
3. The expression field and buttons
"""

from tkinter import *

expression = ""


def press(num):
    global expression
    expression = f"{expression}{num}"
    equation.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        # set expression = "" after calculating total
        expression = ""
    except:
        equation.set("error generated")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


# create the driver. This helps us regulate the code and everything
# here is executed first.
if __name__ == "__main__":
    root = Tk()

    # configure root window of the application
    root.configure(background="#55BDF0")

    # set title of the application
    root.title("Calculator Application")

    # set the geometry of the application
    root.geometry("270x220")

    # create the expression variable name using the StringVar()
    equation = StringVar()

    # set the expression field
    expression_field = Entry(master=root, textvariable=equation, bd=5)

    # place the expression field in grid-like structure
    expression_field.grid(row=1, columnspan=5, ipadx=70, ipady=30)

    # set the variable
    equation.set("Enter your expression: ")

    # ------------------------------------------------------------------------------------------
    # create buttons at a particular location inside the window: buttons will be from 0-9

    # button 1
    button1 = Button(master=root, text='1', fg="white",
                     background="#0099F0", command=lambda: press(1),
                     height=1, width=7)
    button1.grid(row=2, column=0)

    # button2
    button2 = Button(master=root, text='2', fg="white",
                     background="#0099F0", command=lambda: press(2),
                     height=1, width=7)
    button2.grid(row=2, column=1)

    # button 3
    button3 = Button(master=root, text='3', fg="white",
                     background="#0099F0", command=lambda: press(3),
                     height=1, width=7)
    button3.grid(row=2, column=2)

    # button 4
    button4 = Button(master=root, text='4', fg="white",
                     background="#0099F0", command=lambda: press(4),
                     height=1, width=7)
    button4.grid(row=3, column=0)

    # button 5
    button5 = Button(master=root, text='5', fg="white",
                     background="#0099F0", command=lambda: press(5),
                     height=1, width=7)
    button5.grid(row=3, column=1)

    # button 6
    button6 = Button(master=root, text='6', fg="white",
                     background="#0099F0", command=lambda: press(6),
                     height=1, width=7)
    button6.grid(row=3, column=2)

    # button 7
    button7 = Button(master=root, text='7', fg="white",
                     background="#0099F0", command=lambda: press(7),
                     height=1, width=7)
    button7.grid(row=4, column=0)

    # button 8
    button8 = Button(master=root, text='8', fg="white",
                     background="#0099F0", command=lambda: press(8),
                     height=1, width=7)
    button8.grid(row=4, column=1)

    # button 9
    button9 = Button(master=root, text='9', fg="white",
                     background="#0099F0", command=lambda: press(9),
                     height=1, width=7)
    button9.grid(row=4, column=2)

    # button 10
    button0 = Button(master=root, text='0', fg="white",
                     background="#0099F0", command=lambda: press(0),
                     height=1, width=7)
    button0.grid(row=5, column=0)

    # --------------------------------------------------------------------------------------------
    # Buttons for Operators (+,-,=,/,*,clear, decimal(.))

    # + button
    plus = Button(master=root, text="+", fg="white", bg="#0099F0",
                  command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    # - button
    minus = Button(master=root, text="-", fg="white", bg="#0099F0",
                   command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    # * button:
    multiply = Button(master=root, text="*", fg="white", bg="#0099F0",
                      command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    # / button:
    divide = Button(master=root, text="/", fg="white", bg="#0099F0",
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    # = button:
    equal = Button(master=root, text="=", fg="white", bg="#0099F0",
                   command= equalpress, height=1, width=7)
    equal.grid(row=5, column=2)

    # clear button:
    clear = Button(master=root, text="Clear", fg="white", bg="#0099F0",
                   command= clear, height=1, width=7)
    clear.grid(row=5, column=1)

    # decimal button
    decimal = Button(master=root, text=".", fg="white", bg="#0099F0",
                     command=lambda: press("."), height=1, width=7)
    decimal.grid(row=6, column=0)

    # execute the code
    root.mainloop()
