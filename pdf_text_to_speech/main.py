import pyttsx3
import PyPDF2

myFile = open('On-the-Origin-of-Species.pdf', 'rb')
myReader = PyPDF2.PdfFileReader(myFile)
numPages = len(myReader.pages)

speaker = pyttsx3.init()

speaker.say("Hello everyone, welcome to the create audiobook app")
speaker.runAndWait()