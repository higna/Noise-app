let mediaRecorder;
let audioChunks = [];

function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.start();

            mediaRecorder.addEventListener("dataavailable", event => {
                audioChunks.push(event.data);
            });

            mediaRecorder.addEventListener("stop", () => {
                const audioBlob = new Blob(audioChunks);
                const formData = new FormData();
                formData.append('audio_data', audioBlob);

                fetch('/upload', {
                    method: 'POST',
                    body: formData
                })
                .then(response => response.json())
                .then(data => console.log(data));

                audioChunks = [];
            });

            document.getElementById("status").innerText = "Status: Monitoring";
            document.getElementById("startButton").disabled = true;
            document.getElementById("stopButton").disabled = false;
        });
}

function stopRecording() {
    mediaRecorder.stop();
    document.getElementById("status").innerText = "Status: Not Monitoring";
    document.getElementById("startButton").disabled = false;
    document.getElementById("stopButton").disabled = true;
}