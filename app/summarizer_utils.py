def clean_transcript(text: str) -> str:
    sponsor_markers = [
        "brilliant",
        "sponsored",
        "scan the qr code",
        "link in the description",
        "annual premium subscription",
        "thanks again to",
        "thanks again for watching",
        "see you in the next video"
    ]

    lower_text = text.lower()

    for marker in sponsor_markers:
        idx = lower_text.find(marker)
        if idx != -1:
            return text[:idx].strip()

    return text

