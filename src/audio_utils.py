import sounddevice as sd
import numpy as np
from pydub import AudioSegment
import threading

def list_audio_devices():
    devices = sd.query_devices()
    device_names = [device['name'] for device in devices]
    return device_names

def adjust_volume(samples, volume_percentage):
    volume_multiplier = volume_percentage / 100
    return np.int16(samples * volume_multiplier)

def get_device_by_name(device_name):
    return [d['name'] for d in sd.query_devices()].index(device_name)

def play_mp3_through_device(file_path, device_name, volume_percentage):
    def playback():
        device_id = get_device_by_name(device_name)
        audio = AudioSegment.from_file(file_path, format="mp3")
        frame_rate = audio.frame_rate
        audio = audio.set_channels(2)
        samples = np.array(audio.get_array_of_samples())
        if audio.sample_width == 2:
            samples = samples.astype(np.int16)
        elif audio.sample_width == 4:
            samples = samples.astype(np.int32)
        samples = samples.reshape((-1, 2))
        samples = adjust_volume(samples, volume_percentage)
        sd.play(samples, samplerate=frame_rate, device=device_id, blocking=True)

    playback_thread = threading.Thread(target=playback)
    playback_thread.start()
