import speech_recognition as sr
import pyttsx3
from googletrans import Translator
import asyncio

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
        print("???? PLease speak now in English...")
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

"""def translate_text(text, target_language="es"):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f"???? Translated text: {translation.text}")
    return translation.text"""

async def translate_text_async(text, target_language="es"):
    translator = Translator()
    translation = await translator.translate(text, dest=target_language)
    print(f"Translated text: {translation.text}")
    return translation.text


def display_language_options():
    print("???? Available translation languages: ")
    print("???? Available translation languages: ")
    print("1. Hindi (hi)")
    print("2. Marathi (mr)")
    print("3. Malayalam (ml)")
    print("4. Punjabi (pa)")
    choice = input("Please select the target language number (1-8): ")
    language_dict = {
        "1": "hi",
        "2": "mr",
        "3": "ml",
        "4": "pa",
    }

    return language_dict.get(choice, "es")

def main():
    """target_language = display_language_options()
    original_text = speech_to_text
    if original_text:
        translated_text = translate_text(original_text, target_language=target_language)
        speak(translated_text, language="en")
        print("Translation spoken out!")"""
    target_language = display_language_options()

    original_text = speech_to_text()

    if original_text:
        translated_text = asyncio.run(translate_text_async(original_text, "es"))
        speak(translated_text, language="es")
        print("Translation spoken out!")

if __name__ == "__main__":
    main()