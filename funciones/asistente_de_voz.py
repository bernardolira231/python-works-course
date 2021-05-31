import pyttsx3
import re
import speech_recognition as sr


def identify_name(text):
    name = None
    name = re.findall("me llamo ([A-Za-z]+)", text)
    return name

def main():
    engine = pyttsx3.init()
    engine.setProperty("rate", 120)
    engine.setProperty("voice", "spanish")
    engine.say("Hola, como te llamas?")
    engine.runAndWait()

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Puedes Hablar")
        audio = r.listen(source)
        text = r.recognize_google(audio, language = "es-MX")
        name = identify_name(text)
        engine.say("Encantada de conocerte {}".format(name[0]))
        engine.runAndWait()


if __name__ == "__main__":
    main()
