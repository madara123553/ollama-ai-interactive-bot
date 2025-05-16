import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import os
import webbrowser

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # You can change the voice here
engine.setProperty("rate", 170)  # Speed of speech

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to user input and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            speak("Could not request results. Check your internet connection.")
            return ""

def open_application(command):
    """Open applications based on user command."""
    if "notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")
    elif "calculator" in command:
        speak("Opening Calculator")
        os.system("calc")
    elif "chrome" in command:
        speak("Opening Google Chrome")
        os.system("start chrome")
    elif "firefox" in command:
        speak("Opening Firefox")
        os.system("start firefox")
    elif "edge" in command:
        speak("Opening Microsoft Edge")
        os.system("start msedge")

    elif "Gmail" in command:
        os.system("start Gmail")

    else:
        speak("Application not found.")

def run_jarvis():
    """Process voice commands and perform actions."""
    command = listen()

    if "play" in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "who is" in command or "what is" in command:
        query = command.replace("who is", "").replace("what is", "").strip()
        try:
            info = wikipedia.summary(query, sentences=2)
            speak(info)
        except wikipedia.exceptions.DisambiguationError:
            speak("There are multiple results. Please be more specific.")
        except wikipedia.exceptions.PageError:
            speak("Sorry, I couldn't find any information.")

    elif "open" in command:
        app_name = command.replace("open", "").strip()
        open_application(app_name)

    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "Gmail" in command:
        speak("opening gmail")
        webbrowser.open("https://mail.google.com/")

    elif "exit" in command or "stop" in command:
        speak("Goodbye! Have a nice day.")
        exit()
    
    else:
        speak("I'm not sure how to respond to that.")

# Welcome Message
speak("Hello, I am Shivananda How can I help you?")

# Continuous Loop for Commands
while True:
    run_jarvis()