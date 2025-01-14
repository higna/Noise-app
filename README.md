# Noise App

## Overview
The Noise App is a Python-based application designed to detect loud audio levels and provide feedback through sound notifications. It utilizes audio input to monitor sound levels and generates a beep when the sound exceeds a specified threshold.

## Project Structure
```
Noise-app
├── frontend
│   ├── index.html       # Main HTML document for the front end
│   ├── styles.css       # Styles for the HTML elements
│   └── script.js        # JavaScript code for user interactions
├── app.py               # Main Python application for audio processing
├── requirements.txt     # Python dependencies for the application
└── README.md            # Documentation for the project
```

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd Noise-app
   ```

2. **Install dependencies**:
   Make sure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Execute the following command to start the audio processing:
   ```
   python app.py
   ```

## Usage
- The application will start recording audio and will beep when loud sounds are detected.
- Open `frontend/index.html` in a web browser to access the front-end interface.

## Contributing
Feel free to submit issues or pull requests for improvements and bug fixes.