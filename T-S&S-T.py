import pyttsx3   #for text-to-speech conversion
import speech_recognition as sr

def sptotext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning.....")
        audio = recognizer.listen(source)
        try:
            print("Recognising...")
            data = recognizer.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:
            print("Doesn't Understand")
sptotext()
#Uptill now, we are done with speech to text conversion

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) #Male voice
    rate = engine.setProperty('rate', 120)
    sound = engine.setProperty('sound', 1)
    engine.say(x)
    engine.runAndWait()
speechtx("I'm Repeating the text as said")
#done with text-to-speech
