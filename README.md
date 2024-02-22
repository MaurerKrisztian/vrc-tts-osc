# VRC Text-to-Speech With OSC Integration

## Overview
This project offers a text-to-speech application specifically designed for VRChat users, integrating seamlessly with the Open Sound Control (OSC) protocol. It allows users to convert typed text into speech, which is then played through a virtual audio device, mimicking a microphone input.

## Features
- **Text-to-Speech**: Leverage the OpenAI API or ElevenLabs API for high-quality text-to-speech generation.
- **Virtual Audio Device Support**: Play the synthesized speech through a virtual audio device to simulate microphone input in VRChat.
- **VRChat Chatbox Integration**: Simultaneously displays the entered text within VRChat and plays the corresponding audio, creating a cohesive visual and auditory experience.
- **VRChat Typing Effect**: Displays a typing animation in VRChat when typing in the application.
- **Simultaneous Text Display and Speech in VRChat**: As the text is spoken, it also appears in VRChat, synchronized with the voice playback.

## Setup Requirements
Before using this application, you must have a virtual audio cable software, such as Voicemeeter, set up on your system. This is necessary to route the application's audio output through your microphone input, allowing the synthesized speech to be heard in VRChat as if you were speaking.

### Steps:
1. Install a virtual audio cable software, e.g., Voicemeeter.
2. Configure the virtual audio device as your default microphone input in your system's sound settings.

## Installation

### Clone the Repository
```bash
git clone https://github.com/MaurerKrisztian/vrc-tts-osc.git
```
### Install Dependencies
Navigate to the cloned repository's directory and run:
```bash
pip install -r requirements.txt
```
Note: There may be additional dependencies not listed in requirements.txt. Ensure all dependencies are resolved.

### Start the Program
```bash
python ./src/main.py
```
## Usage
1. Upon launching the program, select your virtual audio device from the list, e.g., "CABLE Input (VB-Audio Virtual Cable)".
2. Enter your OpenAI or ElevenLabs API key in the settings. These keys are necessary for accessing the text-to-speech services.
3. Choose a voice from the available options.
4. Type your message into the text field and click "Generate and play". The application will create an audio file and play it through the selected virtual audio device.

### Why Virtual Audio Is Necessary
This setup is crucial because VRChat captures audio from microphone inputs. By using a virtual audio device, we can seamlessly inject the synthesized speech into VRChat, providing a more immersive and customizable experience for users. Without this, directly playing synthesized speech in VRChat would not be possible.

## Development Stage
Please note that this application is in the early stages of development. Features and functionality are subject to change as we refine and expand the project. Feedback and contributions are welcome to help improve the application.

## Contribution
Your feedback and contributions are invaluable to us as we aim to improve and expand this application. Feel free to submit issues or pull requests on our GitHub repository.

