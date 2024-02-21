import json

def save_settings(settings):
    with open('settings.json', 'w') as f:
        json.dump(settings, f)

def load_settings():
    try:
        with open('settings.json', 'r') as f:
            settings = json.load(f)
            return settings
    except (FileNotFoundError, json.JSONDecodeError):
        return {'device_name': 'Default Device Name', 'api_key': '', 'volume_percentage': '100'}
