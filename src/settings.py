import json
from audio_utils import get_default_input_device_name, get_default_output_device_name
class SettingsManager:
    def __init__(self, filename='settings.json'):
        self.filename = filename
        self.settings = self.load_settings()

    def save_settings(self):
        with open(self.filename, 'w') as f:
            json.dump(self.settings, f)

    def load_settings(self):
        try:
            with open(self.filename, 'r') as f:
                settings = json.load(f)
                return settings
        except (FileNotFoundError, json.JSONDecodeError):
            return {
                'device_name': get_default_output_device_name(),
                'device_input_name': get_default_input_device_name(),
                'api_key': '',
                'volume_percentage': '100'
            }

    def update(self, new_settings):
        self.settings.update(new_settings)
        self.save_settings()

    def update_setting(self, key, value):
        print("[settings]: update " + key + " = " + json.dumps(value))
        self.settings[key] = value
        self.save_settings()

    def get(self, key, default=''):
        return self.settings.get(key, default)

settings_manager = SettingsManager()
print("[settings]: loaded settings = " +  json.dumps(settings_manager.settings))
