from tkinter import *

# Initialize history and visibility flag
history = []
history_visible = False


def update_history():
    history_listbox.delete(0, END)
    for item in history:
        history_listbox.insert(END, item)


def toggle_history():
    global history_visible
    if history_visible:
        history_listbox.grid_remove()
        history_button.configure(text="Show History")
    else:
        history_listbox.grid()
        history_button.configure(text="Hide History")
    history_visible = not history_visible


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        history.append(f"{expression} = {total}")
        update_history()
        expression = ""
    except:
        equation.set("error generated")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


def press(num):
    global expression
    expression += str(num)
    equation.set(expression)


def resize(event):
    new_size = min(event.width // 10, event.height // 10)
    for button_x in buttons:
        button_x.config(font=("Helvetica", new_size))


if __name__ == "__main__":
    root = Tk()
    root.configure(background="#55BDF0")
    root.title("Calculator Application")
    root.geometry("300x400")

    equation = StringVar()
    expression = ""
    expression_field = Entry(master=root, textvariable=equation, bd=5)
    expression_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, padx=10, pady=10, sticky="nsew")
    equation.set("Enter your expression: ")

    # Create a list of button texts and their grid positions
    buttons = [
        ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('+', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
        ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('Clear', 4, 2), ('/', 4, 3),
        ('=', 5, 0, 2)
    ]

    # Create buttons using a for-loop
    for (text, row, col, *span) in buttons:
        button = Button(master=root, text=text, fg="white", bg="#0099F0",
                        command=lambda t=text:
                        equalpress() if t == '='
                        else clear() if t == 'Clear'
                        else press(t),
                        height=2, width=7)
        button.grid(row=row, column=col, columnspan=span[0] if span else 1, ipadx=8,
                    ipady=8, padx=5, pady=5, sticky="nsew")

    # Create a listbox to display history
    history_listbox = Listbox(master=root)
    history_listbox.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
    history_listbox.grid_remove()  # Initially hide the history

    # Create a scrollbar and attach it to the listbox
    scrollbar = Scrollbar(master=root)
    scrollbar.grid(row=6, column=4, sticky='ns')
    history_listbox.config(yscrollcommand=scrollbar.set, xscrollcommand=scrollbar.set)
    scrollbar.config(command=history_listbox.yview)

    # Create a button to toggle history visibility
    history_button = Button(master=root, text="Show History", fg="white",
                            bg="#0099F0", command=toggle_history, height=3, width=8)
    history_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

    # Configure grid weights to make widgets expand
    for i in range(7):
        root.grid_rowconfigure(i, weight=1)
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)

    # Bind the resize function to the root window
    root.bind(func=resize)

    root.mainloop()
