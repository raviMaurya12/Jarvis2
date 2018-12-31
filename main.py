import speech_recognition as sr
import pyttsx3


def say(audio):
    print(audio)
    engine = pyttsx3.init()
    engine.say(audio)
    engine.setProperty('rate', 100)
    engine.setProperty('volume', 0.9)
    engine.runAndWait()


def hear():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
#       recognizer.pause_threshold(1)
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = hear()

    return command


say("Welcome sir.")
say("Command mode Activated.")
while True:
    text_command = hear()
    say(text_command)
