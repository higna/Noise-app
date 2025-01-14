let mediaRecorder;
let audioChunks = [];

console.log("Script executed");

function startRecording() {
    console.log("Start button clicked");
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            console.log("Audio stream captured");
            mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.start();

            mediaRecorder.addEventListener("dataavailable", event => {
                console.log("Data available");
                audioChunks.push(event.data);
            });

            mediaRecorder.addEventListener("stop", () => {
                console.log("Recording stopped");
                const audioBlob = new Blob(audioChunks);
                const formData = new FormData();
                formData.append('audio_data', audioBlob);

                fetch('/upload', {
                    method: 'POST',
                    body: formData
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    const indicator = document.getElementById("indicator");
                    indicator.classList.remove("green", "orange", "red");
                    if (data.status === "extreme") {
                        indicator.classList.add("red");
                    } else if (data.status === "medium") {
                        indicator.classList.add("orange");
                    } else {
                        indicator.classList.add("green");
                    }
                });

                audioChunks = [];
            });

            document.getElementById("status").innerText = "Status: Monitoring";
            document.getElementById("startButton").disabled = true;
            document.getElementById("stopButton").disabled = false;
        })
        .catch(error => {
            console.error("Error capturing audio stream:", error);
        });
}

function stopRecording() {
    console.log("Stop button clicked");
    mediaRecorder.stop();
    document.getElementById("status").innerText = "Status: Not Monitoring";
    document.getElementById("startButton").disabled = false;
    document.getElementById("stopButton").disabled = true;
}
