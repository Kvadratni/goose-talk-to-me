# Goose-Talk-To-Me

A voice interaction plugin for your goose. This project leverages a local copy of Whisper for voice interaction and transcription.

## Project Description

Goose-Talk-To-Me is a project dedicated to enabling voice interactions using state-of-the-art AI technologies. It uses tools and libraries like `goose-ai`, `openai-whisper`, `sounddevice`, and others to provide seamless voice processing capabilities.

## Features

- Voice Interaction using `goose-ai`
- Voice to text transcription
- Real-time voice processing

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

## Installation

Install the dependencies and prepare your environment:

```bash
brew install ffmpeg
brew install portaudio
pipx install goosw & install goose-talk-to-me
```

## Usage

To use `goose-talk-to-me`, follow these steps:

1. Run goose
2. ask it to listen to you
3. Speak your command
