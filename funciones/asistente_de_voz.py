import re
from speak_and_listen import speak, hear_me


def identify_name(text):
    name = None
    patterns = ["me llamo ([A-Za-z]+)", "mi nombre es ([A-Za-z]+)", "^([A-Za-z]+)$"]
    for pattern in patterns:
        try:
            name = re.findall(pattern, text)
        except IndexError:
            print("no me ha dicho su nombre")
    return name


def main():
    speak("Hola, Como te llamas?")

    text = hear_me()
    name = identify_name(text)

    if name:
        speak("Encantada de conocerte {}".format(name))
    else:
        speak("La verdad no te entiendo")


if __name__ == "__main__":
    main()
