import sounddevice as sd
import numpy as np
import wave
import openai
import tempfile
import os
import threading



import numpy as np
from vrc import send_text_to_vrchat
from settings import settings_manager

# Function to calculate the RMS of the audio signal
def audio_rms(audio):
    return np.sqrt(np.mean(np.square(audio, dtype=np.float64)))

# Function to call when silence is detected
def on_silence_detected():
    global final_record
    final_record = "[YOU]"
    send_text_to_vrchat("[system] Silence detecte for about 5 seconds.")
    print("Silence detected for about 5 seconds.")


# Function to record audio with a selected device
def record_audio(duration, samplerate=44100, device=None):
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2, dtype='float64', device=device)
    sd.wait()
    return recording

# Function to save recording to a file
def save_recording(recording, filename, samplerate=44100):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(2)
    wf.setsampwidth(2)
    wf.setframerate(samplerate)
    wf.writeframes(np.int16(recording * 32767).tobytes())
    wf.close()

final_record = "[you said]: "
# Function to transcribe audio
def transcribe_audio(file_path, client):
    with open(file_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    print(transcript.text)  # Adjust based on actual attribute/method
    global final_record
    final_record = final_record + transcript.text
    print(final_record)
    send_text_to_vrchat(final_record)

    os.unlink(file_path)  # Clean up the temporary file after transcription

# Function to handle recording and transcription in a separate thread
def handle_recording(duration, client, device):
    recording = record_audio(duration=duration, device=device)
    rms_value = audio_rms(recording)
    
    # Threshold for silence; you might need to adjust this based on testing
    silence_threshold = 0.001
    
    if rms_value < silence_threshold:
        on_silence_detected()
    else:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmpfile:
            save_recording(recording, tmpfile.name)
            threading.Thread(target=transcribe_audio, args=(tmpfile.name, client,)).start()


# Function to list and choose audio input devices
def choose_audio_device():
    print("Available audio input devices:")
    devices = sd.query_devices()
    for i, device in enumerate(devices):
        if device['max_input_channels'] > 0:  # List only input devices
            print(f"{i}: {device['name']}")
    device_index = int(input("Select an input device by number: "))
    return device_index

# Main loop to continuously record and transcribe audio
def test_stt():
    client = openai.OpenAI(api_key=settings_manager.get("openai_api_key"))
    duration = 5  # Duration of each recording in seconds
    
    # Let the user choose the recording device
    device_index = choose_audio_device()
    
    print("Starting recording and transcription loop...")
    while True:
        handle_recording(duration, client, device=device_index)
