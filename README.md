# Goose-Talk-To-Me

A voice interaction plugin for your [goose](https://github.com/square/goose/tree/main). This project
leverages a local copy of Whisper for voice interaction and transcription.

## Project Description

Goose-Talk-To-Me is a project dedicated to enabling voice interactions using state-of-the-art AI
technologies. It uses tools and libraries like `goose-ai`, `openai-whisper`, `sounddevice`, and
others to provide seamless voice processing capabilities.

## Features

- Voice Interaction using `goose-ai`
- Voice to text transcription
- Real-time voice processing
- Text to speech using `pyttsx4`

## Requirements

- Python >= 3.12
- `goose-ai`
- `openai-whisper`
- `sounddevice`
- `soundfile`
- `numpy`
- `scipy`
- `torch`
- `numba`
- `more-itertools`
- `ffmpeg`
- `pyttsx4`

## Installation

Install the dependencies and prepare your environment:

### Linux

```bash
sudo apt update && sudo apt install espeak ffmpeg libespeak1 portaudio19-dev
pipx install goose & install goose-talk-to-me

### MacOS
```bash
brew install ffmpeg
brew install portaudio
pipx install goose & install goose-talk-to-me  --include-deps
```

## Usage

To use `goose-talk-to-me`, follow these steps:

1. add talk-to-me toolkit to a profile `~/.config/goose/profiles.yaml`
2. start a new goose session with the profile
3. ask goose to talk to you

```
