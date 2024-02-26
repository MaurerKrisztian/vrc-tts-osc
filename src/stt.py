from roastedbyai import Conversation, Style
from tts import elevenlabs_tts
from audio_utils import get_device_by_name
import time
from vrc import send_text_to_vrchat
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
                send_text_to_vrchat("[system]: Listening continuously...")
                # Listen for the first phrase and extract audio data
                audio = r.listen(source)
                # Recognize speech using Google's speech recognition
                text = r.recognize_google(audio)
                print(f"You said: {text}")
                send_text_to_vrchat("[You said]: " + text)
                response = get_roasted_msg(text)
                print("[AI response]: " + response)
                generate_tts_and_play(response)
                # time.sleep(time_to_speak(text))
            except sr.UnknownValueError:
                send_text_to_vrchat("[system]: Could not understand audio. Try again")
                time.sleep(1)
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")


def time_to_speak(text):
    average_seconds_per_character = 0.3
    return len(text) * average_seconds_per_character