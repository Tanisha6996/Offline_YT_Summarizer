import whisper

model = whisper.load_model(
    "base",
    download_root="models/whisper"
)

def transcribe(audio_path: str) -> str:
    result = model.transcribe(audio_path)
    return result["text"]
