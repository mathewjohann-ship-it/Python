import speech_recognition as sr
import pyttsx3
from datetime import datetime


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("???? Speak now...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Could not understand")
        except sr.RequestError as e:
            print(f"API Error: {e}")
    return ""

def respond_to_command(command):
    if "hello" in command:
        speak("Hi there! How can I help you today?")
    elif "how are you doing" in command:
        speak("I am doing great! What about you?")
    elif "great" in command or("good" in command and "not good" not in command):
        speak("That's great to hear.")
    elif "not good" in command or "having a bad day" in command or "not great" in command:
        speak("Oh, that's sad to hear. Hope it gets better for you")
    elif "your name" in command:
        speak("I am your python Voice assistant.")
    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")
    elif "where are you from" in command or "where do you live" in command:
        speak("I am based in the UK!")
    elif "your favourite sport" in command:
        speak("I don't have a favourite sport as im your voice assistant but I would like to play football!")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        return False
    else:
        speak("I'm not sure how to help with that.")
    return True

def main():
    speak("Voice assistant activated. Say something!")
    while True:
        command = get_audio()
        if command and not respond_to_command(command):
            break


if __name__ == "__main__":
    main()