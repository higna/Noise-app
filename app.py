from flask import Flask, render_template, request, jsonify
import numpy as np
import io
import wave

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
    try:
        audio_data = request.files['audio_data']
        print("Audio data received")
        
        # Read the audio data
        audio_bytes = io.BytesIO(audio_data.read())
        print("Audio bytes read")
        
        # Process the audio data
        with wave.open(audio_bytes, 'rb') as wf:
            frames = wf.readframes(wf.getnframes())
            audio = np.frombuffer(frames, dtype=np.int16)
            rms = np.sqrt(np.mean(audio**2))
            db = 20 * np.log10(rms)
            print(f"Audio data processed, RMS: {rms}, dB: {db}")
        
        # Detect loud noise
        extreme_threshold = -10  # in dB
        medium_threshold = -20  # in dB
        if db > extreme_threshold:
            print("Extreme noise detected")
            return jsonify({"status": "extreme"})
        elif db > medium_threshold:
            print("Medium noise detected")
            return jsonify({"status": "medium"})
        else:
            print("Good noise level")
            return jsonify({"status": "good"})
    except Exception as e:
        print(f"Error processing audio data: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

# Ensure the app runs only when executed directly
if __name__ == "__main__":
    app.run(debug=True)

# Export the app for Vercel
app = app
