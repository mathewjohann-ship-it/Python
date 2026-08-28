import speech_recognition as sr
import pyttsx3
from googletrans import Translator

def speak(text, language="en"):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')

    if language == "en":
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)
    
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("???? Please speak now in English....")
        audio = recognizer.listen(source)
    
    try:
        print("???? Recognizing speech...")
        text = recognizer.recognize_google(audio, language = "en-US")
        print(f"You said {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print(f"API Error: {e}")
        return ""

def translate_text(text, target_language = "es"):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f"???? Translated text: {translation.text}")
    return translation.text