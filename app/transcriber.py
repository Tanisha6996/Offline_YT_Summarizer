import whisper

# Load the Whisper speech-to-text model locally
# The model is downloaded once and reused for all transcriptions
# download_root ensures the model is stored locally for offline use
model = whisper.load_model(
    "base",
    download_root="models/whisper"
)

def transcribe(audio_path: str) -> str:
    """
    Transcribes an audio file into text using an offline Whisper model.

    This function performs speech-to-text conversion on the provided
    audio file and returns the transcribed text.

    Args:
        audio_path (str): Path to the local audio file.

    Returns:
        str: Transcribed text output from the audio.
    """

    # Perform transcription using the Whisper model
    result = model.transcribe(audio_path)

    # Extract and return the transcribed text
    return result["text"]
