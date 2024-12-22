import speech_recognition as sr

import sounddevice as sd

import numpy as np

import scipy.io.wavfile as wav


test_file = 'over-radio-countdown_108bpm_A_minor.wav'

FILE_FROM_USER = 'RECORDING.wav'

VOICE_FILE = 'VOICE.txt'


r = sr.Recognizer()


def recognize_speech_from_file(filename):

    with sr.AudioFile(filename) as source:
        audio = r.record(source)
        text = r.recognize_google(audio)
        return text

def record_audio(filename):

    fs = 44100  
    seconds = 5
    myrecording = sd.rec(seconds * fs, samplerate=fs, channels=1, dtype='int32')
    sd.wait()
    print("Recording saved")
    sd.play(myrecording, fs)
    sd.wait()
    print("Recording played", end="")
    wav.write(filename, fs, myrecording)

def save_to_file(text, filename):

    with open(filename, 'w') as f:
        f.write(text)


def main():

    print("Please record your voice for 5 seconds")
    record_audio(FILE_FROM_USER)
    voice_to_text = recognize_speech_from_file(FILE_FROM_USER)
    save_to_file(voice_to_text, VOICE_FILE)


if __name__ == "__main__":
    main()