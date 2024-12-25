import pyttsx3
import PyPDF2

myFile = open('On-the-Origin-of-Species.pdf', 'rb')

speaker = pyttsx3.init()

speaker.say("Hello everyone, welcome to the create audiobook app")
speaker.runAndWait()