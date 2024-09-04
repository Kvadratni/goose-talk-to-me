from goose.toolkit import Toolkit
from goose.toolkit.base import tool
from exchange import Message
from whisper import load_model
from soundfile import write
import numpy as np
import pyttsx4


class TalkToMeGoose(Toolkit):
    """Provides speech to text functionality using Whisper"""

    def __init__(
        self,
        model_path: str = "base",
        notifier: any = None,
        requires: any = None,
        model: any = None,
        input_stream: any = None,
    ) -> None:
        super().__init__(notifier=notifier, requires=requires)
        self.input_stream = input_stream or __import__("sounddevice").InputStream
        self.model_path = model_path
        self.model = model
        self.tts_engine = None

    @tool
    def convert_speech_to_text(self, audio_file: str) -> str:
        """Converts speech from the given audio file to text.

        Arguments:
            audio_file (str): Path to the audio file

        Returns:
            result (str): Transcribed text from the audio file
        """
        if self.model is None:
            self.model = load_model(self.model_path)
        result = self.model.transcribe(audio_file)
        self.notifier.log(f"Transcribed text: {result['text']}")
        return result["text"]

    @tool
    def start_listening(self) -> str:
        """Starts listening to the microphone and records audio until 2 seconds of silence is detected.

        Returns:
            result (str): The transcribed text from the recorded audio
        """

        self.channels = 1
        self.rate = 44100
        self.silence_threshold = 2  # seconds of silence
        self.silence_level = 0.02  # threshold for silence detection

        def is_silence(data: np.ndarray, threshold: float = self.silence_level) -> bool:
            return np.max(np.abs(data)) < threshold

        self.notifier.log("Recording...")
        frames = []
        silence_len = 0

        with self.input_stream(samplerate=self.rate, channels=self.channels) as stream:
            while True:
                data, overflowed = stream.read(int(0.1 * self.rate))
                frames.append(data)
                if is_silence(data):
                    silence_len += 0.1
                else:
                    silence_len = 0
                if silence_len >= self.silence_threshold:
                    break

        audio_data = np.concatenate(frames, axis=0)
        audio_file = "recorded_audio.wav"
        write(audio_file, audio_data, self.rate)
        self.notifier.log(f"Audio saved as {audio_file}")

        return self.convert_speech_to_text(audio_file)

    @tool
    def speak(self, text: str) -> None:
        """Speaks the given text using text-to-speech.

        Arguments:
            text (str): The text to be spoken aloud
        """
        if self.tts_engine is None:
            self.tts_engine = pyttsx4.init(driverName='nsss')
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    def system(self) -> str:
        return str(Message.load("prompts/talk_to_me.jinja").text)
