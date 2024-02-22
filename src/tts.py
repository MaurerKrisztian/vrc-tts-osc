from audio_utils import play_mp3_through_device
from openai import OpenAI
from vrc import send_text_to_vrchat
from settings import settings_manager

def openai_tts(text, api_key):
    if not text or not api_key:
        return  # TODO: Add error handling or UI feedback here

    print("[tts]: try to generate speach: " + text)
    send_text_to_vrchat(text)
    client = OpenAI(api_key=api_key)
    response = client.audio.speech.create(
        model="tts-1",
        input=text,
        voice= settings_manager.get("selected_openai_voice") or "alloy",
    )

    print("[tts]: save generated speach.. ")
    response.stream_to_file("ttsoutput.mp3")

    print("[tts]: play generated speach")
    play_mp3_through_device("ttsoutput.mp3", settings_manager.get("device_name"),  int(settings_manager.get("volume_percentage")))

def replay():
    play_mp3_through_device("ttsoutput.mp3", settings_manager.get("device_name"),  int(settings_manager.get("volume_percentage")))




from elevenlabs.client import ElevenLabs
from elevenlabs import generate, voices

def elevenlabs_tts(text, api_key):
    print("[elevenlabs]: play generated speach ->  " + text)
    
    audio = generate(
        text=text,
        voice= settings_manager.get("selected_elevenlabs_voice") or "Rachel",
        model="eleven_multilingual_v2",
        api_key=api_key
        )

    with open('./ttsoutput.mp3', "wb") as audio_file:
        audio_file.write(audio)
    print("[tts]: play generated speach")
    play_mp3_through_device("ttsoutput.mp3", settings_manager.get("device_name"),  int(settings_manager.get("volume_percentage")))

def get_elevenlabs_voices():
    return [voice.name for voice in voices()]

print(get_elevenlabs_voices())