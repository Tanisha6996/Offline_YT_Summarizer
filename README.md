# Offline YouTube Video Summarizer
## Project Overview

This project is an **end-to-end offline YouTube video summarization system** built as part of a take-home assignment for a Full-Time AI Engineer role.

The application accepts a public YouTube video URL, downloads the audio, transcribes the speech using an offline speech-to-text model, and generates a concise yet detailed summary using an offline text summarization model. All core AI components run entirely offline, without relying on any cloud-based APIs.

The system is implemented as a FastAPI-based web application with a simple UI, ensuring clean separation between backend logic and user interaction.

## Features- 

- Accepts a public YouTube URL
- Downloads and extracts audio locally
- Offline speech-to-text transcription
- Offline abstractive text summarization
- Handles long videos via chunking
- Removes sponsor/irrelevant content from transcripts
- Produces structured, readable summaries
- Fully offline AI inference (no external APIs)

## Tech Stack

- **Backend:** FastAPI
- **YouTube Audio Download:** yt-dlp
- **Speech-to-Text:** OpenAI Whisper (offline)
- **Summarization:** T5 (offline)
- **Frontend:** Simple HTML + CSS (served via FastAPI)
- **Language:** Python 3.10

## Setup and Installation Instructions

### 1. Clone the Repository
   
```
git clone https://github.com/<your-username>/Offline_YT_Summarizer.git
cd Offline_YT_Summarizer
```

The repository is private. Access can be granted upon request.

### 2. Create and Activate a Virtual Environment
```  
python3 -m venv myenv
source myenv/bin/activate
```
### 3. Install Dependencies
```
pip install -r requirements.txt
```
### 4. Download Offline Models (Required)

Model files are not included in the repository due to size constraints since both of the files are over 100 MB.

#### Speech-to-Text (Whisper)

Whisper models will be automatically downloaded on first use or can be pre-downloaded manually.

Recommended model:

* base (good balance between speed and accuracy)

#### Summarization (T5)

* Download the T5 model locally using Hugging Face:
```
python -c "from transformers import AutoModelForSeq2SeqLM, AutoTokenizer; \
AutoTokenizer.from_pretrained('t5-small'); \
AutoModelForSeq2SeqLM.from_pretrained('t5-small')"
```

Models will be cached locally and used fully offline during inference.

### 5. Run the Application
```
uvicorn app.main:app --reload
```

* Open your browser at:
```
http://127.0.0.1:8000
```

## Usage

### 1. Web Interface

1. Paste a valid YouTube video URL into the input field
2. Click Summarize
3. The system will:
      - Download audio
      - Transcribe speech
      - Generate a detailed summary
      - The final summary is displayed on the page

### 2. API Endpoint

#### POST /summarize

**Request Body:**
```
{
  "url": "https://www.youtube.com/watch?v=VIDEO_ID"
}
```

**Response:**
```
{
  "summary": "Generated summary text..."
}
```
## Design Choices and Justification
### Why FastAPI?

FastAPI was chosen for its:
   - High performance and low overhead
   - Clean separation between API logic and ML components
   - Built-in support for async operations (useful for long-running tasks)
   - Automatic API documentation for easy testing and debugging

FastAPI allows the system to remain modular, extensible, and production-friendly.

### Why Whisper for Speech-to-Text?
   - Fully open-source and offline-capable
   - Strong performance on real-world audio
   - Robust to accents, noise, and conversational speech
   - Easy local deployment without external dependencies

**Trade-off:**

Larger Whisper models improve accuracy but require more compute. The selected model balances speed and transcription quality.

### Why T5 for Summarization?
   - Designed specifically for text-to-text tasks
   - Strong abstractive summarization capabilities
   - Lightweight enough for offline CPU inference
   - Performs well on conversational and spoken transcripts

**Trade-off:**

Larger models (e.g., BART-large) can produce more nuanced summaries but significantly increase memory usage and setup complexity. T5 provides a practical balance between quality, speed, and offline usability.

## System Design

The system is structured into clear, independent modules:
   - Downloader: Handles YouTube audio extraction
   - Transcriber: Converts audio to text using Whisper
   - Cleaner: Removes sponsorships and irrelevant content
   - Chunker: Splits long transcripts into manageable segments
   - Summarizer: Generates summaries for each chunk and merges them
   - API Layer: Orchestrates the pipeline and serves results

This modular design improves maintainability and makes future extensions straightforward.

## Challenges Faced and Solutions

### 1. Large Model Files and GitHub Limits

**Challenge:** GitHub blocks files larger than 100 MB.
**Solution:** Excluded model weights from version control and documented local download steps in the README.

### 2. Long Video Transcripts

**Challenge:** Summarization models have context length limits.
**Solution:** Implemented transcript chunking and hierarchical summarization.

### 3. Noisy Transcripts and Sponsorship Content

**Challenge:** Transcripts often include ads and irrelevant sections.
**Solution:** Added transcript-cleaning logic to remove sponsor segments before summarization.

### 4. Offline-Only Constraint

**Challenge:** Avoiding cloud APIs while maintaining quality.
**Solution:** Carefully selected open-source models that run locally with acceptable performance.

## Robustness and Error Handling
   - Validates YouTube URLs
   - Gracefully handles download/transcription failures
   - Supports long videos via chunking
   - Prevents model files from being committed
   - Runs entirely offline once models are available

## Demonstration

A short screencast demonstrating:
   - Entering a YouTube URL
   - Running the summarization pipeline
   - Displaying the final summary

📹 Demo video is included separately as part of the submission.
https://youtu.be/HaGDxPs8z7I

## Final Notes

This project demonstrates:
   - End-to-end AI system design
   - Offline model deployment
   - Clean software engineering practices
   - Robust handling of real-world data

The repository is intentionally kept lightweight, with models downloaded locally as part of setup.

**Author:** Tanisha Das

**Role Targeted:** AI Engineer / Machine Learning Engineer
