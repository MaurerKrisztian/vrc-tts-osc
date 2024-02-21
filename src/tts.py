from audio_utils import play_mp3_through_device
from openai import OpenAI
from vrc import send_text_to_vrchat

def generate_and_play_tts(text, api_key, device_name, volume_percentage):
    if not text or not api_key:
        return  # TODO: Add error handling or UI feedback here

    send_text_to_vrchat(text)
    client = OpenAI(api_key=api_key)
    response = client.audio.speech.create(
        model="tts-1",
        input=text,
        voice="alloy",
    )

    response.stream_to_file("ttsoutput.mp3")

    play_mp3_through_device("ttsoutput.mp3", device_name, volume_percentage)
