
# This script is a short tutorial of PyPDF2

"""
                The PyPDF2 module:
--> It is used for spliting, merging, cropping and transforming pages in PDFs or pdf files.
--> PyPDF2 can also be used to add data, extract text and metadata from PDFs.
--> It is used for rotating pages
--> It is used for overlaying/watermarking pages
--> It is used for encrypting and decrypting

                Pyttsx3:
--> It is used to convert text to speech.
--> You can change voice gender, language, volume, rate of speech, age of voice.
"""
import PyPDF2
import pyttsx3

# paste file path to PDF into empty string
path = ""
# using context manager
with open(path, "rb") as file_object:
    pdf_file_reader = PyPDF2.PdfReader(file_object)

    # extract text from PDF_file
    extracted_text = ""

    # iterate over the number of pages in the file
    for page_num in range(len(pdf_file_reader.pages)):

        # get the page object by indexing the pdf file using the pagenum
        pdf_page_object = pdf_file_reader.pages[page_num]

        # iteration # is for page #:
        extracted_text += pdf_page_object.extract_text()

    print(extracted_text)


# Invoke the pyttsx3.init() to get access pyttsx3 module to convert text to audio
engine_object = pyttsx3.init()

# set the rate, voice,
engine_object.setProperty("rate", 180)
engine_object.setProperty("voice", "f1")
engine_object.setProperty("volume", 1.0)


# text you want the engine to speak
engine_object.say('The quick brown fox jumped over the lazy dog.')

# runAndWait() : Engine is not going to speak unless interpreter encounter runAndWait
engine_object.runAndWait()























