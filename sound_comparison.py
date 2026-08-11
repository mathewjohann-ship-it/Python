import threading
import sys
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import speech_recognition as sr
from speech_recognition import AudioData

stop_event = threading.Event()

def wait_for_enter():
    input()
    stop_event.set()

def record_audio(label):
    stop_event.clear()
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 1024)
    frames = []
    print(f"\n???? {label}")
    print("   Press Enter to stop...")
    threading.Thread(target = wait_for_enter, daemon=True).start()

    print("???? Recording", end = "", flush=True)
    while not stop_event.is_set():
        frames.appen(stream.read(1024, exception_on_overflow=False))
        print(".", end = "", flush = True)
    print(" ✅")

    stream.stop_stream()
    stream.close()
    width = p.get_sample_size(pyaudio.paInt16)
    p.terminate()
    return b"".join(frames), 16000, width

def analyze_audio(data, rate):
    samples = np.frombuffer(data, dtype=np.int16)
    return {
        "duration": len(samples)/rate,
        "avg_volume": np.mean(np.abs(samples)),
        "max_volume": np.max(np.abs(samples)),
        "samples": samples
    }

def transcribe(data, rate, width):
    recognizer = sr.Recognizer()
    try:
        return recognizer.recognize_google(AudioData(data, rate, width))
    except:
        return "[Could not transcribe]"

def display_stats(stats, text, label):
    print(f"\n{'-'*40}")
    print(f"???? {label}")
    print(f"{'-' *40}")
    print(f"⏱️ Duration: {stats['duration']:.2f} seconds")
    print(f"???? Avg Amplitude: {stats['avg_volume']:.0f}")
    print(f"???? Max Amplitude: {stats['max_volume']:.0f}")
    print(f"???? Transcription: {text}")

def compare(stats1, stats2):
    print("\n" + "=" * 40)
    print("???? COMPARISON RESULTS")
    print("=" * 40)
    if stats1['duration'] > stats2['duration']:
        longer = "Recording 1"
        diff = ((stats1['duration'] - stats2['duration'])/ stats2['duration']) * 100
    else:
        longer = "Recording 2"
        diff = ((stats2['duration'] - stats1['duration'])/ stats1['duration']) * 100
    print(f"⏱️ {longer} is longer by {diff:.1f}%")
    