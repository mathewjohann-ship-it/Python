import speech_recognition as sr
import pyttsx3
from googletrans import Translator
import subprocess

def speak_hindi(text):

    subprocess.run(["say", "-v", "Lekha", text])

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
# def translate_text(text, target_language="es"):
#     translator = Translator()
#     translation = translator.translate(text, dest=target_language)
async def translate_text(text, target_language):
    try:
        translator = Translator()
        translation = await translator.translate( text, dest=target_language )
        print(f"🌍 Translated text: {translation.text}") 
        return translation.text 
    except Exception as e:
        print(f"❌ Translation error: {e}")
        return ""
def display_language_options():
    print("???? Available translation languages: ")
    print("1. Hindi (hi)")
    print("2. Bengali (bn)")
    print("3. Marathi (mr)")
    print("4. Malayalam (ml)")

    choice = input("Please select the target language number (1 - 8): ")
    language_dict = {
        "1": "hi",
        "2": "bn",
        "3": "mr",
        "4": "ml"
    }
    return language_dict.get(choice, "es")

async def main():
    target_language = display_language_options()
    original_text = speech_to_text()
    if original_text:
        translated_text = await translate_text(original_text, target_language = target_language)
        if translated_text:
            speak(translated_text, language = target_language)
            print("Translation spoken out!")

            speak_hindi(translated_text)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())