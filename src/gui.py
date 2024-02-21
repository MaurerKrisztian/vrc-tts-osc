import tkinter as tk
from tkinter import messagebox, scrolledtext
from audio_utils import list_audio_devices
from tts import generate_and_play_tts
from settings import save_settings, load_settings

def setup_gui(root):
    device_var = tk.StringVar(root)
    volume_var = tk.StringVar(root, value='100')
    token_var = tk.StringVar(root)

    # Load settings
    settings = load_settings()
    device_var.set(settings.get('device_name', 'Default Device Name'))
    token_var.set(settings.get('api_key', ''))
    volume_var.set(settings.get('volume_percentage', '100'))

def on_generate_tts_click(text_widget, device_var, volume_var, token_var):
    text = text_widget.get("1.0", tk.END).strip()
    api_key = token_var.get()
    device_name = device_var.get()
    try:
        volume_percentage = float(volume_var.get())  # Correctly extract and convert the volume
    except ValueError:
        messagebox.showwarning("Warning", "Invalid volume percentage. Please enter a valid number.")
        return

    if not text or not api_key:
        messagebox.showwarning("Warning", "Please enter both text and API key.")
        return

    generate_and_play_tts(text, api_key, device_name, volume_percentage)

def on_save_settings_click(device_var, token_var, volume_var):
    settings = {
        'device_name': device_var.get(),
        'api_key': token_var.get(),
        'volume_percentage': volume_var.get()
    }
    save_settings(settings)
    messagebox.showinfo("Info", "Settings saved successfully.")

def setup_gui(root):
    device_var = tk.StringVar(root)
    volume_var = tk.StringVar(root, value='100')
    token_var = tk.StringVar(root)

    # Load settings
    settings = load_settings()
    device_var.set(settings.get('device_name', 'Default Device Name'))
    token_var.set(settings.get('api_key', ''))
    volume_var.set(settings.get('volume_percentage', '100'))

    # Device selection
    device_label = tk.Label(root, text="Select Audio Device:")
    device_label.pack()
    device_options = list_audio_devices()
    device_menu = tk.OptionMenu(root, device_var, *device_options)
    device_menu.pack()

    # Volume control
    volume_label = tk.Label(root, text="Volume (%):")
    volume_label.pack()
    volume_entry = tk.Entry(root, textvariable=volume_var)
    volume_entry.pack()

    # API Key input
    api_key_label = tk.Label(root, text="API Key:")
    api_key_label.pack()
    api_key_entry = tk.Entry(root, textvariable=token_var)
    api_key_entry.pack()

    # TTS Text input
    tts_text_label = tk.Label(root, text="Text to Synthesize:")
    tts_text_label.pack()
    tts_text = scrolledtext.ScrolledText(root, height=5)
    tts_text.pack()

    # Generate and Play TTS Button
    generate_tts_button = tk.Button(root, text="Generate and Play TTS", command=lambda: on_generate_tts_click(tts_text, device_var, volume_var, token_var))
    generate_tts_button.pack()

    # Save Settings Button
    save_settings_button = tk.Button(root, text="Save Settings", command=lambda: on_save_settings_click(device_var, token_var, volume_var))
    save_settings_button.pack()

