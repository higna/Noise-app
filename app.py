from flask import Flask, render_template, request, jsonify

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
    # Process the audio data here
    print("Audio data received")
    return jsonify({"status": "success"})

# Ensure the app runs only when executed directly
if __name__ == "__main__":
    app.run()

# Export the app for Vercel
app = app
