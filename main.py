import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser
import sys
import requests
import playsound

from gtts import gTTS
import os

ear =sr.Recognizer()
assistant= pyttsx3.init()
voices =assistant.getProperty('voices')
assistant.setProperty('voice',voices[1].id)


def speak(text):
    assistant.say(text)
    assistant.runAndWait()

# def input_command():
#     try:
#         with sr.Microphone() as source:
#             print("..........")
#             ear.adjust_for_ambient_noise(source, duration=0.5)
#             audio= ear.listen(source)
#             command = ear.recognize_google(audio)
#             print(command)
#             speak(command)
#     except Exception as e:
#         print(e)
#     return command

# def run_assistant():
#     command = input_command()

#     if 'hello' or 'hi' in command:
#         print("Hello Rala I am your friend ralarani. How may I help you?")
#         speak("Hello Rala I am your friend ralarani. How may I help you?")

#     elif 'time' in command:
#         time = datetime.datetime.now().strftime('%I:%M %p')
#         print(time)
#         speak('current time is'+time)




def talk():
    input=sr.Recognizer()
    with sr.Microphone() as source:
        audio=input.listen(source)
        data=""
        try:
            data=input.recognize_google(audio)
            print("Your question is, "+data)
        except sr.UnknownValueError:
            print("Sorry I did not hear your question, Please repeat again.")
    return data 


def respond(output):
    num=0
    print(output)
    num +=1
    response=gTTS(text=output, lang='en')
    file = str(num)+".mp3"
    response.save(file)
    playsound.playsound(file,True)
    os.remove(file)

if __name__=='__main__':
    #run_assistant()
    respond("Hello,Rala. I am Ralani. Your Personal Desktop Assistent")

    while(1):
        respond("How can I help you ?")
        text=talk().lower()

        if text ==0:
            continue

        if "stop" in str(text) or "exit" in str(txt) or "bye" in str(text):
            respond("Okey !! bye and take care.")
            break