from roastedbyai import Conversation, Style
from tts import elevenlabs_tts
from audio_utils import get_device_by_name
import time

convo = Conversation(Style.adult)
def get_roasted_msg(text):
    return convo.send(text)

import speech_recognition as sr
from settings import settings_manager
from tts import generate_tts_and_play
def listen_and_transcribe():
    # Initialize the recognizer
    r = sr.Recognizer()
    # Use the selected microphone as the audio source
    with sr.Microphone(device_index=get_device_by_name(settings_manager.get("device_input_name"))) as source:
        # Adjust the recognizer sensitivity to ambient noise
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening continuously...")
        # Continuously listen and transcribe
        while True:
            if settings_manager.get("ai_enabled") == False:
                time.sleep(2)
                continue
            try:
                # Listen for the first phrase and extract audio data
                audio = r.listen(source)
                # Recognize speech using Google's speech recognition
                text = r.recognize_google(audio)
                print(f"You said: {text}")
                response = get_roasted_msg(text)
                print(response)
                generate_tts_and_play(response)
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")