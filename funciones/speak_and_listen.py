import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init()
engine.setProperty("rate", 200)
engine.setProperty("voice", "spanish")

r = sr.Recognizer()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def hear_me():
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language = "es-MX")
            print("He entendido {}".format(text) )
            return text
        except sr.UnknownValueError:
            return
