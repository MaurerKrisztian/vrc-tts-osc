
import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
from audio_utils import list_audio_devices
from tts import openai_tts, elevenlabs_tts, replay, get_elevenlabs_voices
from settings import settings_manager
from vrc import typing
from stt import listen_and_transcribe
import asyncio
import threading
import json
import multiprocessing

proc = False
def setup_gui(root):
    padding = {'padx': 10, 'pady': 5}
    
    # Group 1: Device Settings
    device_frame = ttk.LabelFrame(root, text="Device Settings")
    device_frame.pack(fill='x', expand=True, **padding)

    device_var = tk.StringVar(value=settings_manager.get('device_name'))
    device_var2 = tk.StringVar(value=settings_manager.get('device_input_name'))
    volume_var = tk.StringVar(value=settings_manager.get('volume_percentage'))

    # Audio Output Device Selection
    ttk.Label(device_frame, text="Select Audio Output Device:").pack(**padding)
    device_options = list_audio_devices()
    tk.OptionMenu(device_frame, device_var, *device_options, command=lambda value: settings_manager.update_setting('device_name', value)).pack(fill='x', **padding)

    # Audio Input Device Selection
    ttk.Label(device_frame, text="Select Audio Input Device:").pack(**padding)
    tk.OptionMenu(device_frame, device_var2, *device_options, command=lambda value: settings_manager.update_setting('device_input_name', value)).pack(fill='x', **padding)

    # Volume Control
    ttk.Label(device_frame, text="Volume (%):").pack(**padding)
    ttk.Entry(device_frame, textvariable=volume_var, width=20).pack(fill='x', **padding)
    volume_var.trace("w", lambda name, index, mode, sv=volume_var: settings_manager.update_setting('volume_percentage', volume_var.get()))

    # Group 2: OpenAI Settings
    openai_frame = ttk.LabelFrame(root, text="OpenAI Settings")
    openai_frame.pack(fill='x', expand=True, **padding)

    openai_key_var = tk.StringVar(value=settings_manager.get('openai_api_key'))
    selected_openai_voice_var = tk.StringVar(value=settings_manager.get('selected_openai_voice'))

    # OpenAI API Key Input
    ttk.Label(openai_frame, text="OpenAI API Key:").pack(**padding)
    openai_key_entry = ttk.Entry(openai_frame, textvariable=openai_key_var, width=50)
    openai_key_entry.pack(fill='x', **padding)
    openai_key_var.trace("w", lambda name, index, mode, sv=openai_key_var: settings_manager.update_setting('openai_api_key', openai_key_var.get()))

    # OpenAI Voice Selection
    ttk.Label(openai_frame, text="Select Voice for OpenAI:").pack(**padding)
    voice_dropdown = ttk.Combobox(openai_frame, textvariable=selected_openai_voice_var, values=["alloy", "echo", "fable", "onyx", "nova", "shimmer"], state="readonly")
    voice_dropdown.pack(fill='x', **padding)
    selected_openai_voice_var.trace("w", lambda name, index, mode, sv=selected_openai_voice_var: settings_manager.update_setting('selected_openai_voice', selected_openai_voice_var.get()))

    # Group 3: ElevenLabs Settings
    elevenlabs_frame = ttk.LabelFrame(root, text="ElevenLabs Settings")
    elevenlabs_frame.pack(fill='x', expand=True, **padding)

    elevenlabs_key_var = tk.StringVar(value=settings_manager.get('elevenlabs_api_key'))
    selected_elevenlabs_voice_var = tk.StringVar(value=settings_manager.get('selected_elevenlabs_voice'))

    # ElevenLabs API Key Input
    ttk.Label(elevenlabs_frame, text="ElevenLabs API Key:").pack(**padding)
    elevenlabs_key_entry = ttk.Entry(elevenlabs_frame, textvariable=elevenlabs_key_var, width=50)
    elevenlabs_key_entry.pack(fill='x', **padding)
    elevenlabs_key_var.trace("w", lambda name, index, mode, sv=elevenlabs_key_var: settings_manager.update_setting('elevenlabs_api_key', elevenlabs_key_var.get()))

    # ElevenLabs Voice Selection
    ttk.Label(elevenlabs_frame, text="Select Voice for ElevenLabs:").pack(**padding)
    elevenlabs_voice_dropdown = ttk.Combobox(elevenlabs_frame, textvariable=selected_elevenlabs_voice_var, values=get_elevenlabs_voices(), state="readonly")
    elevenlabs_voice_dropdown.pack(fill='x', **padding)
    selected_elevenlabs_voice_var.trace("w", lambda name, index, mode, sv=selected_elevenlabs_voice_var: settings_manager.update_setting('selected_elevenlabs_voice', selected_elevenlabs_voice_var.get()))

    # Miscellaneous Settings
    # TTS Service Selection
    service_var = tk.StringVar(value=settings_manager.get('tts_service'))
    service_label = ttk.Label(root, text="Select TTS Service:")
    service_label.pack(**padding)
    service_combo = ttk.Combobox(root, textvariable=service_var, values=['openai', 'elevenlabs'], state="readonly")
    service_combo.pack(fill='x', **padding)
    service_var.trace("w", lambda name, index, mode, sv=service_var: settings_manager.update_setting('tts_service', service_var.get()))


    # AI Enable Switch
    ai_enable_var = tk.BooleanVar(value=False)  # Default to False if not set
    ai_enable_label = ttk.Label(root, text="Enable AI:")
    ai_enable_label.pack(**padding)
    ai_enable_checkbutton = ttk.Checkbutton(root, text="AI Enabled", variable=ai_enable_var, command=lambda: on_ai_enable_toggle())
    ai_enable_checkbutton.pack(**padding)

    def on_ai_enable_toggle():
        global proc
        # This function gets called whenever the checkbox is toggled
        new_value = ai_enable_var.get()  # Get the current value of the variable
        if new_value:
            print("start thread")
            proc = multiprocessing.Process(target=listen_and_transcribe, args=())
            proc.start()
        else:
            print("stop thread")
            proc.terminate()
        print(f"AI Enabled set to: {new_value}")  # Log the new value
        settings_manager.update_setting('ai_enabled', new_value)  # Update the setting


    # TTS Text Input
    tts_text_label = ttk.Label(root, text="Text to Synthesize:")
    tts_text_label.pack(**padding)
    tts_text = scrolledtext.ScrolledText(root, height=5)
    tts_text.pack(fill='both', expand=True, **padding)
    # Assuming check_textbox_content is defined elsewhere to handle content check

    # Generate and Play TTS Button
    generate_tts_button = ttk.Button(root, text="Generate and Play TTS", command=lambda: on_generate_tts_click(tts_text.get("1.0", tk.END).strip(), service_var.get()))
    generate_tts_button.pack(fill='x', **padding)

    # Replay Last TTS Button
    replay_button = ttk.Button(root, text="Replay", command=replay)
    replay_button.pack(fill='x', **padding)


def check_textbox_content(event):
    widget = event.widget  # Access the widget that triggered the event
    content = widget.get("1.0", tk.END).strip()  # Get text box content, stripping leading and trailing whitespaces
    if content:  # If the text box is not empty
        typing(True)
    else:
        typing(False)

def on_generate_tts_click(text, service):
    if not text:
        messagebox.showwarning("Warning", "Please enter text to synthesize.")
        return

    if service == 'openai' and settings_manager.get('openai_api_key'):
        openai_tts(text)
    elif service == 'elevenlabs' and settings_manager.get('elevenlabs_api_key'):
        elevenlabs_tts(text)
    else:
        messagebox.showwarning("Warning", "API key for selected TTS service is missing.")
