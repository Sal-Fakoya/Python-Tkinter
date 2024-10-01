
# This is a text-to-audio app built using tkinter

from tkinter import *
from tkinter import filedialog
import PyPDF2
import pyttsx3
import threading

# Global flag to control the speech
continue_speaking = True



def extract_text():
    """
    extract_text(): extracts texts from PDF pages
    parameters: 
    """
    global text_extracted

    file = filedialog.askopenfile(parent=root, mode="rb", title="Choose a PDF File: ")

    if file is not None:
        with open(file.name, file.mode) as file_object:
            pdf_file_reader = PyPDF2.PdfReader(file_object)
            text_extracted = ""

            for page_num in range(len(pdf_file_reader.pages)):
                pdf_page_object = pdf_file_reader.pages[page_num]
                text_extracted += pdf_page_object.extract_text()


def speak_text():
    """
    speak_text(): sets the read voice to male and female voice, and has a subfunction
    parameter: 
    """
    global continue_speaking

    rate_value = int(rate.get())
    engine.setProperty("rate", rate_value)

    male_value = int(male.get())
    female_value = int(female.get())

    all_voices = engine.getProperty("voices")
    male_voice, female_voice = all_voices[0].id, all_voices[1].id

    if (male_value == 0 and female_value == 0) or (male_value == 1 and female_value == 1):
        engine.setProperty("voice", male_voice)
    elif male_value == 0 and female_value == 1:
        engine.setProperty("voice", female_voice)
    else:
        engine.setProperty("voice", male_voice)

    continue_speaking = True

    
    def run_speech():
        """
        run_speech(): controls speaking upon play button 
        parameter: 
        """
        for line in text_extracted.split('\n'):
            if not continue_speaking:
                break
            engine.say(line)
            engine.runAndWait()

    # create a new thread object for the run_speech function with .start() method
    # so that the program can play again when the audio stopped and played again
    threading.Thread(target=run_speech).start()


def stop_speaking():
    """
    stop_speaking(): controls the stop playing button. 
    """
    global continue_speaking
    print("Stop button pressed")
    continue_speaking = False
    engine.stop()


def Application(root):
    """
    Application(root): is the function for the GUI of the App. Takes the "root" Tk() window as an argument.
    parameter: root
    """
    
    global rate, male, female

    root.geometry("700x600")
    root.resizable(width=False, height=False)
    root.title("PDF to AUDIO")
    root.configure(background="#E1DCB5")

    frame1 = Frame(master=root, width=500, height=200, bg="#E0BA80")
    frame1.pack(side=TOP, fill=BOTH)

    name1 = Label(master=frame1, text="PDF to AUDIO", fg="black", bg="#48CCE0", font="Arial 28 bold")
    name1.pack()

    name2 = Label(master=frame1, text="Hear your PDF file", fg="#AE48E0", bg="#E0D493", font="Calibre 25 bold")
    name2.pack()

    frame2 = Frame(master=root, width=500, height=450, bg="#E1DCB5")
    frame2.pack(side=TOP, fill="y")

    btn = Button(master=frame2, text="Select PDF File: ", activeforeground="red", command=extract_text, padx=70,
                 pady=10, fg="white", bg="#E05C48", font="Arial 12")
    btn.grid(row=0, pady=20, columnspan=2)

    rate_text = Label(master=frame2, text="Enter the rate of speech: ", fg="black", bg="#E05C48", font="Arial 12")
    rate_text.grid(row=1, column=0, pady=15, padx=0, sticky=W)

    rate = Entry(master=frame2, fg="black", bg="white", font="Arial 12")
    rate.grid(row=1, column=1, pady=15, padx=30, sticky=W)
    rate.insert(0, "200")  # Default rate value

    voice_text = Label(master=frame2, text="Select Voice: ", fg="black", bg="#E05C48", font="Arial 12")
    voice_text.grid(row=2, column=0, padx=0, pady=15, sticky=W)

    male = IntVar()
    female = IntVar()

    male_option = Checkbutton(master=frame2, text="Male", bg="#E5AF7D", variable=male, onvalue=1, offvalue=0)
    male_option.grid(row=2, column=1, padx=30, pady=0, sticky=W)

    female_option = Checkbutton(master=frame2, text="Female", bg="#E5AF7D", variable=female, onvalue=1, offvalue=0)
    female_option.grid(row=3, column=1, padx=30, pady=0, sticky=W)

    submit_btn = Button(master=frame2, text="Play PDF file", command=speak_text, activeforeground="#E5AF7D", padx=60,
                        pady=10, fg="white", bg="black", font="Arial 12")
    submit_btn.grid(row=4, column=0, pady=65)

    stop_btn = Button(master=frame2, text="Stop Playing", command=stop_speaking, activeforeground="#E5AF7D", padx=60,
                      pady=10, fg="white", bg="black", font="Arial 12")
    stop_btn.grid(row=4, column=1, pady=65)


# Create the driver for the application to set up the window. This function will always run first.
if __name__ == '__main__':
    text_extracted = ""
    engine = pyttsx3.init()

    root = Tk()
    Application(root)
    root.mainloop()
