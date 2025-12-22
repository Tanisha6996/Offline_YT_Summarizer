from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
import torch

# Local filesystem path to the pre-downloaded T5 summarization model
# Models are stored locally to ensure fully offline inference
MODEL_PATH = (
    "models/summarizer/models--t5-small/"
    "snapshots/df1b051c49625cf57a3d0d8d3863ed4d13564fe4"
)

# Load tokenizer from local files only (no internet access)
tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)

# Load the T5 model for sequence-to-sequence summarization from local files
model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)

# Initialize the Hugging Face summarization pipeline
# device = -1 ensures the model runs on CPU (offline, hardware-agnostic setup)
summarizer = pipeline(
    "summarization",
    model=model,
    tokenizer=tokenizer,
    device=-1  # CPU
)

def summarize_chunks(chunks):
    """
    Generates a detailed summary from multiple text chunks.

    Each chunk is summarized independently using the T5 model, and the
    individual summaries are then combined into a single coherent summary.
    This approach allows the system to handle long transcripts that exceed
    the model's maximum context length.

    Args:
        chunks (list[str]): List of transcript chunks.

    Returns:
        str: Final combined and formatted summary.
    """

    # List to store summaries generated for each chunk
    summaries = []

    # Iterate through each text chunk
    for chunk in chunks:
        # Skip empty or whitespace-only chunks
        if not chunk.strip():
            continue

        # Generate summary for the current chunk
        output = summarizer(
            "summarize: " + chunk,
            max_length=200,   # Controls maximum summary length
            min_length=80,    # Ensures sufficient detail in summaries
            do_sample=False   # Deterministic output for consistency
        )

        # Extract the generated summary text
        summaries.append(output[0]["summary_text"])

    # Combine all chunk-level summaries into a single text
    summary = " ".join(summaries)

    # --- Post-processing: Fix capitalization and sentence formatting ---
    # Split summary into sentences, capitalize each sentence,
    # and rejoin for improved readability
    sentences = [s.strip() for s in summary.split(".")]
    sentences = [s.capitalize() for s in sentences if s]
    summary = ". ".join(sentences) + "."

    return summary
