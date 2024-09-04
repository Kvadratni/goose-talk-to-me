import pytest
from unittest.mock import patch, MagicMock
import unittest
from talk_to_me import TalkToMeGoose


@pytest.fixture
def talk_to_me_toolkit() -> TalkToMeGoose:
    mock_model = MagicMock()
    toolkit = TalkToMeGoose(
        model_path="base", notifier=MagicMock(), requires=None, model=mock_model, input_stream=MagicMock()
    )
    return toolkit


def test_system_message(talk_to_me_toolkit: TalkToMeGoose) -> None:
    message = talk_to_me_toolkit.system()
    assert "speech to text" in message.lower()


@patch("builtins.print")
def test_convert_speech_to_text(mock_print: any, talk_to_me_toolkit: TalkToMeGoose) -> None:
    mock_result = {"text": "Hello world"}
    talk_to_me_toolkit.model.transcribe.return_value = mock_result

    with patch("os.path.exists", return_value=True), patch(
        "builtins.open", unittest.mock.mock_open(read_data=b"fake audio data")
    ):
        result = talk_to_me_toolkit.convert_speech_to_text("dummy_audio.wav")

    talk_to_me_toolkit.model.transcribe.assert_called_once_with("dummy_audio.wav")
    assert result == "Hello world"


@patch("pyttsx3.init")
def test_speak(mock_pyttsx3_init: any, talk_to_me_toolkit: TalkToMeGoose) -> None:
    engine_mock = MagicMock()
    mock_pyttsx3_init.return_value = engine_mock

    text = "Hello, world!"
    talk_to_me_toolkit.speak(text)

    mock_pyttsx3_init.assert_called_once_with()
    engine_mock.say.assert_called_once_with(text)
    engine_mock.runAndWait.assert_called_once_with()
