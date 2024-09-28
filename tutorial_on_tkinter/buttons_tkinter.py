

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

                                Callback Function:
        arg* command = some_function_name
        OR button.config(command=some_function)


"""
from tkinter import *
from tkinter import ttk

root = Tk()
def callback():
    print("A button was clicked!")

button = ttk.Button(master=root,
                    text="Click Me",
                    command=callback)

button1 = Button(master=root,
                 text="Click another me",
                 relief=SUNKEN)

button.config(command=callback)

for i in range(5):
    button.invoke()

button1.place(x=50, y=50)

button.pack() # adjusts button to the screen

path = "C:\\Users\\fakoy\Text_to_Audio_App\\tutorial_on_tkinter"
logo = PhotoImage(file=f"{path}\\sakomoto_days.jpg")
button.config(image=logo, compound=LEFT)
#
#
x = logo.subsample(7, 7)
button.config(image=x)

button.state(['disabled'])
button_state = button.instate(['disabled'])
print(button_state)

button_state1 = button.instate(["!disabled"])
print(button_state1)

root.mainloop()
# runs the code on the root window





























