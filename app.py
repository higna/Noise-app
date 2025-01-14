from flask import Flask, render_template, request, jsonify
from pydub import AudioSegment
import numpy as np
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_recording():
    print("Recording started...")
    return "Recording started"

@app.route('/stop', methods=['POST'])
def stop_recording():
    print("Recording stopped...")
    return "Recording stopped"

@app.route('/upload', methods=['POST'])
def upload_audio():
    audio_data = request.files['audio_data']
    audio = AudioSegment.from_file(io.BytesIO(audio_data.read()), format="wav")
    
    # Detect loud noise
    extreme_threshold = -10  # in dBFS
    medium_threshold = -20  # in dBFS
    if audio.dBFS > extreme_threshold:
        print("Extreme noise detected")
        return jsonify({"status": "extreme"})
    elif audio.dBFS > medium_threshold:
        print("Medium noise detected")
        return jsonify({"status": "medium"})
    else:
        return jsonify({"status": "good"})

# Ensure the app runs only when executed directly
if __name__ == "__main__":
    app.run(debug=True)

# Export the app for Vercel
app = app
