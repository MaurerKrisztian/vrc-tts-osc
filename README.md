# VRC Text-to-Speech With OSC Integration & AI bot

## Overview
This project offers a text-to-speech application specifically designed for VRChat users, integrating seamlessly with the Open Sound Control (OSC) protocol. It allows users to convert typed text into speech, which is then played through a virtual audio device, mimicking a microphone input. Plus, it also include an AI. You can use this AI as a game bot or just to chat locally, depending on how you set up the virtual devices.

## Features
- **Text-to-Speech**: Leverage the OpenAI API or ElevenLabs API for high-quality text-to-speech generation.
- **Virtual Audio Device Support**: Play the synthesized speech through a virtual audio device to simulate microphone input in VRChat.
- **VRChat Chatbox Integration**: Simultaneously displays the entered text within VRChat and plays the corresponding audio, creating a cohesive visual and auditory experience.
- **VRChat Typing Effect**: Displays a typing animation in VRChat when typing in the application.
- **Simultaneous Text Display and Speech in VRChat**: As the text is spoken, it also appears in VRChat, synchronized with the voice playback.
- **AI**: Talk to AI using your voice. This feature is still being tested and might not work perfectly yet. It uses the same AI model as https://www.roastedby.ai/, so it will make fun of you.


![image](https://github.com/MaurerKrisztian/vrc-tts-osc/assets/48491140/358cf2f8-c24a-4152-967b-a634b1a1fc3f)
## Setup Requirements
Before using this application, you must have a virtual audio cable software, such as Voicemeeter, set up on your system. This is necessary to route the application's audio output through your microphone input, allowing the synthesized speech to be heard in VRChat as if you were speaking.

### Steps:
1. Install a virtual audio cable software, e.g., Voicemeeter.
2. Configure the virtual audio device as your default microphone input in your system's sound settings.

## Installation
You'll have to start with the source code. The alpha version (an executable file) will be available soon.

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

# Text-to-Speech Setup Guide

This section explains how to set up text-to-speech (TTS) functionality for your game using virtual audio cables. The setup allows the TTS audio to be played through the app and be recognized as game input.

## Required Setup
For this setup, you only need one virtual cable, which simplifies the process. If you haven't already, you can get a virtual cable from [VB-Cable](https://vb-audio.com/Cable/index.htm) for free or use similar services.

### Setup Steps
1. Set the game's input device to Virtual Cable 1 (A).
2. In your TTS application, set the output device to Virtual Cable 1 (A).

This configuration ensures that the audio from the text-to-speech application is directed into the game as if it were coming from a microphone input.

By doing so, any text you convert to speech in the app will be heard in the game, allowing for an immersive experience or facilitating communication with other players using TTS technology.

## Setup Requirements for AI

I'm still working on this setup. If anyone knows a better or easier way, please open up an issue, and we can discuss it. This solution should work with any game or app.

### Creating an AI Bot
To create an AI bot, you will need two virtual devices. Unfortunately, the VB-Cable package only includes one virtual cable for free. You will need to purchase the A+B package from [VB-Cable A+B](https://shop.vb-audio.com/en/win-apps/12-vb-cable-ab.html?SubmitCurrency=1&id_currency=1) or use other services.

### Setup Steps
1. Set the game's output device to Virtual Cable 1 (A).
2. In the program, select the input device as Virtual Cable 1 (A). This will mimic the in-game sound as a mic input to the program.
3. Set the program's output device to Virtual Cable 2 (B). We will play the AI speech result through this virtual device.
4. Set the game's input device to Virtual Cable 2 (B).

The following sketch should help you understand the setup:
![image](https://github.com/MaurerKrisztian/vrc-tts-osc/assets/48491140/61d8f3be-6ee5-4246-8946-829923237521)
![image](https://github.com/MaurerKrisztian/vrc-tts-osc/assets/48491140/47897ca5-a1f1-4f80-9e66-bb5082cc8a60)

![image](https://github.com/MaurerKrisztian/vrc-tts-osc/assets/48491140/6825c370-8f05-41a2-a184-14067c93eaf1)
![image](https://github.com/MaurerKrisztian/vrc-tts-osc/assets/48491140/5a738b21-9244-4ae2-b281-c4634d9d92e2)
## Development Stage
Please note that this application is in the early stages of development. Features and functionality are subject to change as we refine and expand the project. Feedback and contributions are welcome to help improve the application.

## Contribution
Your feedback and contributions are invaluable to us as we aim to improve and expand this application. Feel free to submit issues or pull requests on our GitHub repository.

