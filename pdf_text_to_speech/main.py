import pyttsx3
import PyPDF2

myFile = open('On-the-Origin-of-Species.pdf', 'rb')
myReader = PyPDF2.PdfReader(myFile)
numPages = len(myReader.pages)
print("Number of pages in the PDF: ", numPages)

speaker = pyttsx3.init()

speaker.say("Hello everyone, welcome to the create audiobook app")
speaker.runAndWait()