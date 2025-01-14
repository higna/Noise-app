import pyaudio
import numpy as np
import sounddevice as sd
import time
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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

@app.route('/start', methods=['POST'])
def start_recording():
    global stream
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("Recording started...")
    return "Recording started"

@app.route('/stop', methods=['POST'])
def stop_recording():
    global stream
    stream.stop_stream()
    stream.close()
    print("Recording stopped...")
    return "Recording stopped"

# Ensure the app runs only when executed directly
if __name__ == "__main__":
    app.run()

# Export the app for Vercel
app = app
