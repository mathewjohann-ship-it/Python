import os
import subprocess
import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS


# -----------------------------
# Speech-to-Text
# -----------------------------
def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("Speak in English...")

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=15
            )

        except sr.WaitTimeoutError:
            print("No speech detected.")
            return ""

    try:
        text = recognizer.recognize_google(
            audio,
            language="en-US"
        )

        print("You said:", text)
        return text

    except sr.UnknownValueError:
        print("I couldn't understand what you said.")
        return ""

    except sr.RequestError as error:
        print("Speech recognition error:", error)
        return ""


# -----------------------------
# Translate English -> Spanish
# -----------------------------
def translate_text(text):
    try:
        translated = GoogleTranslator(
            source="en",
            target="es"
        ).translate(text)

        print("Spanish:", translated)
        return translated

    except Exception as error:
        print("Translation failed:", error)
        return ""


# -----------------------------
# Speak Spanish
# -----------------------------
def speak_spanish(text):
    filename = os.path.join(
        os.path.expanduser("~"),
        "spanish_output.mp3"
    )

    try:
        print("Speaking Spanish...")

        tts = gTTS(
            text=text,
            lang="es"
        )

        tts.save(filename)

        subprocess.run(
            ["afplay", filename],
            check=True
        )

    except Exception as error:
        print("Text-to-speech failed:", error)

    finally:
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except OSError:
                pass


# -----------------------------
# Main Program
# -----------------------------
def main():
    print()
    print("English -> Spanish Voice Translator")
    print("-----------------------------------")

    english_text = speech_to_text()

    if not english_text:
        return

    spanish_text = translate_text(english_text)

    if not spanish_text:
        return

    speak_spanish(spanish_text)


# -----------------------------
# Start Program
# -----------------------------
if __name__ == "__main__":
    main()