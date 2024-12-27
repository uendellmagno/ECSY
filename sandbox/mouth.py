from TTS.api import TTS
from pydub import AudioSegment
from pydub.playback import play
import io

# Load the Coqui TTS model
tts_model = "tts_models/multilingual/multi-dataset/your_tts"  # Multilingual model
tts = TTS(model_name=tts_model)

# List available speakers for debugging
available_speakers = tts.speakers
print(f"Available speakers: {available_speakers}")

def who_speaks(phrase, language):
    """
    Generates and plays speech audio for the given phrase in the specified language using Coqui TTS.

    Args:
        phrase (str): The text to be spoken.
        language (str): The language of the text ('pt-BR' for Portuguese or 'en-US' for English).

    Returns:
        None
    """
    # Adjust speaker language (if supported by the model)
    speaker_language = "pt-br" if language.startswith("pt") else "en"

    # Choose an appropriate speaker
    speaker = available_speakers[0]  # Replace with a specific speaker if needed

    print(f"Speaking in {language} ({speaker}): {phrase}")

    # Synthesize speech to a byte buffer
    with io.BytesIO() as audio_buffer:
        tts.tts_to_file(
            text=phrase,
            file_path=audio_buffer,
            language=speaker_language,
            speaker=speaker
        )
        audio_buffer.seek(0)  # Reset buffer to the beginning

        # Load the audio data with pydub
        audio = AudioSegment.from_file(audio_buffer, format="wav")

        # Play the audio directly
        play(audio)
