from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Import application-specific modules
from app.downloader import download_audio
from app.transcriber import transcribe
from app.chunker import chunk_text
from app.summarizer import summarize_chunks
from app.summarizer_utils import clean_transcript


# Initialize the FastAPI application
app = FastAPI()

# Configure Jinja2 for HTML templating
templates = Jinja2Templates(directory="templates")

# Mount the static directory for CSS and frontend assets
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    """
    Renders the home page with the input form.

    Args:
        request (Request): Incoming HTTP request object.

    Returns:
        HTMLResponse: Rendered HTML page.
    """
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/summarize", response_class=HTMLResponse)
def summarize(request: Request, url: str = Form(...)):
    """
    Handles the summarization pipeline for a given YouTube URL.

    Workflow:
        1. Download audio from the YouTube video.
        2. Transcribe audio to text using an offline STT model.
        3. Clean the transcript by removing sponsor and irrelevant content.
        4. Split the transcript into smaller chunks.
        5. Generate summaries for each chunk and combine them.

    Args:
        request (Request): Incoming HTTP request object.
        url (str): YouTube video URL submitted via the form.

    Returns:
        HTMLResponse: Rendered HTML page with either the summary or an error message.
    """
    try:
        # Download audio from the provided YouTube URL
        audio_path = download_audio(url)

        # Transcribe the downloaded audio into text
        transcript = transcribe(audio_path)

        # Remove sponsorships and irrelevant segments from the transcript
        transcript = clean_transcript(transcript)

        # Split long transcripts into smaller chunks
        chunks = chunk_text(transcript)

        # Generate a combined summary from all transcript chunks
        summary = summarize_chunks(chunks)

        # Render the page with the generated summary
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "summary": summary}
        )

    except Exception as e:
        # Gracefully handle errors and display them on the UI
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "error": str(e)}
        )
