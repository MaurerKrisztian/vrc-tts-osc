import sounddevice as sd
import numpy as np
import threading
import time
import wave
import soundfile as sf

def list_audio_devices():
    devices = sd.query_devices()
    device_names = [device['name'] for device in devices]
    return device_names

def get_default_input_device_name():
    device_info = sd.query_devices(sd.default.device[0], 'input')
    return device_info['name']

def get_default_output_device_name():
    device_info = sd.query_devices(sd.default.device[1], 'output')
    return device_info['name']

def adjust_volume(samples, volume_percentage):
    volume_multiplier = volume_percentage / 100
    return np.int16(samples * volume_multiplier)

def get_device_by_name(device_name):
    return [d['name'] for d in sd.query_devices()].index(device_name)

def play_mp3_through_device(file_path, device_name, volume_percentage):
    def playback():
        device_id = get_device_by_name(device_name)
        data, samplerate = sf.read(file_path, dtype='int16')
        if data.ndim > 1:  # If stereo, take only one channel
            data = data[:, 0]
        data = adjust_volume(data, volume_percentage)
        sd.play(data, samplerate=samplerate, device=device_id, blocking=True)

    playback_thread = threading.Thread(target=playback)
    
    print("Start audio. Duration: " + str(get_mp3_duration(file_path)) + " second")
    playback_thread.start()
    time.sleep(get_mp3_duration(file_path))
    print("sleep finished")

def get_wav_duration(file_path):
    with wave.open(file_path, 'r') as wav_file:
        frames = wav_file.getnframes()
        rate = wav_file.getframerate()
        duration = frames / float(rate)
    return duration

from mutagen.mp3 import MP3

def get_mp3_duration(file_path):
    audio = MP3(file_path)
    return audio.info.length
