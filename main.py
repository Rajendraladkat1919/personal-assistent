import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser
import sys

ear =sr.Recognizer()
assistant= pyttsx3.init()
voices =assistant.getProperty('voices')
assistant.setProperty('voice',voices[1].id)


def speak(text):
    assistant.say(text)
    assistant.runAndWait()

def input_command():
    try:
        with sr.Microphone() as source:
            print("..........")
            ear.adjust_for_ambient_noise(source, duration=0.5)
            audio= ear.listen(source)
            command = ear.recognize_google(audio)
            print(command)
            speak(command)
    except Exception as e:
        print(e)
    return command

def run_assistant():
    command = input_command()

    if 'hello' or 'hi' in command:
        print("Hello Rala I am your friend ralarani. How may I help you?")
        speak("Hello Rala I am your friend ralarani. How may I help you?")

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        speak('current time is'+time)


if __name__=='__main__':
    run_assistant()