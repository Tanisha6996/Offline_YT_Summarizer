import yt_dlp
import os

def download_audio(url: str, output_dir="data") -> str:
    os.makedirs(output_dir, exist_ok=True)

    output_template = os.path.join(output_dir, "audio.%(ext)s")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_template,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "quiet": True,
        "no_warnings": True,

    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    final_audio_path = os.path.join(output_dir, "audio.mp3")

    if not os.path.exists(final_audio_path):
        raise FileNotFoundError("Audio download failed: audio.mp3 not found")

    return final_audio_path
