from transformers import AutoModelForSeq2SeqLM, AutoTokenizer,pipeline
import torch

MODEL_PATH = (
    "models/summarizer/models--t5-small/"
    "snapshots/df1b051c49625cf57a3d0d8d3863ed4d13564fe4"
)

from transformers import  pipeline

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)

summarizer = pipeline(
    "summarization",
    model=model,
    tokenizer=tokenizer,
    device=-1  # CPU
)

def summarize_chunks(chunks):
    summaries = []

    for chunk in chunks:
        if not chunk.strip():
            continue

        output = summarizer(
            "summarize: " + chunk,
            max_length=200,
            min_length=80,
            do_sample=False
        )

        summaries.append(output[0]["summary_text"])

    # Join summaries
    summary = " ".join(summaries)

    # ---- Fix capitalization inline ----
    sentences = [s.strip() for s in summary.split(".")]
    sentences = [s.capitalize() for s in sentences if s]
    summary = ". ".join(sentences) + "."

    return summary
