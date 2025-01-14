# FILE: /Noise-app/Noise-app/app.py
import pyaudio
import numpy as np
import sounddevice as sd
import time
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Audio input settings
FORMAT = pyaudio.paInt16  # 16-bit resolution
CHANNELS = 1              # Mono channel
RATE = 44100              # Sampling rate
CHUNK = 1024              # Buffer size
THRESHOLD = 35.0          # Threshold in dB for loud audio detection
BEEP_DURATION = 0.2       # Duration of the beep sound in seconds

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Function to generate a beep sound
def beep():
    beep_freq = 1000  # Frequency of the beep sound
    beep_duration = BEEP_DURATION  # Duration of the beep sound
    sample_rate = 44100  # Sample rate

    t = np.linspace(0, beep_duration, int(beep_duration * sample_rate), endpoint=False)
    beep_signal = 0.5 * np.sin(2 * np.pi * beep_freq * t)
    sd.play(beep_signal, samplerate=sample_rate)
    sd.wait()

# Open the stream
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Recording...")
def calculate_decibels(data):
    audio_data = np.frombuffer(data, dtype=np.int16)
    rms = np.sqrt(np.mean(np.square(audio_data)))
    decibels = 20 * np.log10(rms) if rms > 0 else -np.inf
    return decibels

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/audio')
def audio_stream():
    data = stream.read(CHUNK)
    decibels = calculate_decibels(data)
    if decibels > THRESHOLD:
        beep()
    return jsonify({'decibels': decibels})

if __name__ == '__main__':
    app.run(debug=True)