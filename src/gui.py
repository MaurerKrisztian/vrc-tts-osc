import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
from audio_utils import list_audio_devices
from tts import openai_tts, elevenlabs_tts, replay, get_elevenlabs_voices
from settings import settings_manager
from vrc import typing

def setup_gui(root):
    settings = settings_manager.load_settings()

    device_var = tk.StringVar(value=settings.get('device_name', 'Default Device Name'))
    volume_var = tk.StringVar(value=settings.get('volume_percentage', '100'))
    openai_key_var = tk.StringVar(value=settings.get('openai_api_key', ''))
    elevenlabs_key_var = tk.StringVar(value=settings.get('elevenlabs_api_key', ''))

    service_var = tk.StringVar(value=settings.get('tts_service', 'openai'))  # Default to 'openai'

    # Device selection
    device_label = tk.Label(root, text="Select Audio Device:")
    device_label.pack()
    device_options = list_audio_devices()
    device_menu = tk.OptionMenu(root, device_var, *device_options, command=lambda value: settings_manager.update_setting('device_name', value))
    device_menu.pack()

    # Volume control
    volume_label = tk.Label(root, text="Volume (%):")
    volume_label.pack()
    volume_entry = tk.Entry(root, textvariable=volume_var)
    volume_entry.bind("<FocusOut>", lambda event: settings_manager.update_setting('volume_percentage', volume_var.get()))
    volume_entry.pack()

    # OpenAI API Key input
    openai_key_label = tk.Label(root, text="OpenAI API Key:")
    openai_key_label.pack()
    openai_key_entry = tk.Entry(root, textvariable=openai_key_var)
    openai_key_entry.bind("<FocusOut>", lambda event: settings_manager.update_setting('openai_api_key', openai_key_var.get()))
    openai_key_entry.pack()

    # Voice selection dropdown for openai
    openai_voice_label = tk.Label(root, text="Select Voice for openai:")
    openai_voice_label.pack()
    selected_openai_voice_var = tk.StringVar(value=settings.get('selected_elevenlabs_voice_var', ''))
    voice_dropdown = ttk.Combobox(root, textvariable=selected_openai_voice_var, values=["alloy", "echo", "fable", "onyx", "nova","shimmer"])

    # Here we bind the selection event to automatically update the setting
    voice_dropdown.bind("<<ComboboxSelected>>", lambda event: settings_manager.update_setting('selected_openai_voice', selected_openai_voice_var.get())) 
    voice_dropdown.pack()

    # ElevenLabs API Key input
    elevenlabs_key_label = tk.Label(root, text="ElevenLabs API Key:")
    elevenlabs_key_label.pack()
    elevenlabs_key_entry = tk.Entry(root, textvariable=elevenlabs_key_var)
    elevenlabs_key_entry.bind("<FocusOut>", lambda event: settings_manager.update_setting('elevenlabs_api_key', elevenlabs_key_var.get()))
    elevenlabs_key_entry.pack()


   # Voice selection dropdown for ElevenLabs
    voice_label = tk.Label(root, text="Select Voice for ElevenLabs:")
    voice_label.pack()
    selected_elevenlabs_voice_var = tk.StringVar(value=settings.get('selected_elevenlabs_voice_var', ''))
    voice_dropdown = ttk.Combobox(root, textvariable=selected_elevenlabs_voice_var, values=get_elevenlabs_voices())

    # Here we bind the selection event to automatically update the setting
    voice_dropdown.bind("<<ComboboxSelected>>", lambda event: settings_manager.update_setting('selected_elevenlabs_voice', selected_elevenlabs_voice_var.get())) 
    voice_dropdown.pack()

    # TTS Service Selection
    service_label = tk.Label(root, text="Select TTS Service:")
    service_label.pack()
    service_combo = ttk.Combobox(root, textvariable=service_var, values=['openai', 'elevenlabs'])
    service_combo.pack()

    # TTS Text input
    tts_text_label = tk.Label(root, text="Text to Synthesize:")
    tts_text_label.pack()
    tts_text = scrolledtext.ScrolledText(root, height=5)
    tts_text.bind("<KeyRelease>", check_textbox_content)
    tts_text.pack()

    # Button to generate and play TTS
    generate_tts_button = tk.Button(root, text="Generate and Play TTS", command=lambda: on_generate_tts_click(tts_text.get("1.0", tk.END).strip(), service_var.get()))
    generate_tts_button.pack()

    # Button to replay last TTS
    replay_button = tk.Button(root, text="Replay", command=lambda: replay())
    replay_button.pack()

    # Save Settings Button
    save_settings_button = tk.Button(root, text="Save Settings", command=lambda: settings_manager.save_settings())
    save_settings_button.pack()


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
        openai_tts(text, settings_manager.get('openai_api_key'))
    elif service == 'elevenlabs' and settings_manager.get('elevenlabs_api_key'):
        elevenlabs_tts(text, settings_manager.get('elevenlabs_api_key'))
    else:
        messagebox.showwarning("Warning", "API key for selected TTS service is missing.")
