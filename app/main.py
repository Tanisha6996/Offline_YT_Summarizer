from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.downloader import download_audio
from app.transcriber import transcribe
from app.chunker import chunk_text
from app.summarizer import summarize_chunks
from app.summarizer_utils import clean_transcript


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/summarize", response_class=HTMLResponse)
def summarize(request: Request, url: str = Form(...)):
    try:
        audio_path = download_audio(url)
        transcript = transcribe(audio_path)
        transcript = clean_transcript(transcript)
        chunks = chunk_text(transcript)
        summary = summarize_chunks(chunks)

        return templates.TemplateResponse(
            "index.html",
            {"request": request, "summary": summary}
        )

    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "error": str(e)}
        )
