import yt_dlp
import os

def download_audio(url: str, output_dir="data") -> str:
    """
    Downloads the audio track from a YouTube video URL and saves it locally as an MP3 file.

    This function uses yt-dlp to extract the best available audio stream
    and converts it to MP3 format using FFmpeg.

    Args:
        url (str): Public YouTube video URL.
        output_dir (str): Directory where the audio file will be saved.

    Returns:
        str: Absolute path to the downloaded MP3 audio file.

    Raises:
        FileNotFoundError: If the audio file is not created successfully.
    """

    # Create the output directory if it does not already exist
    os.makedirs(output_dir, exist_ok=True)

    # Define the output filename template for yt-dlp
    output_template = os.path.join(output_dir, "audio.%(ext)s")

    # yt-dlp configuration options
    ydl_opts = {
        # Select the best available audio-only format
        "format": "bestaudio/best",

        # Specify output file path and naming convention
        "outtmpl": output_template,

        # Post-process the downloaded audio using FFmpeg
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],

        # Suppress yt-dlp console output
        "quiet": True,
        "no_warnings": True,
    }

    # Download the audio using yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Construct the expected final audio file path
    final_audio_path = os.path.join(output_dir, "audio.mp3")

    # Verify that the audio file was successfully created
    if not os.path.exists(final_audio_path):
        raise FileNotFoundError("Audio download failed: audio.mp3 not found")

    return final_audio_path
