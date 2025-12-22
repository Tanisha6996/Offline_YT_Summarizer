def clean_transcript(text: str) -> str:
    """
    Removes sponsorship and irrelevant trailing content from a transcript.

    The function searches for common sponsor or outro markers and truncates
    the transcript at the first occurrence. This helps ensure that the
    summarization model focuses only on meaningful content.

    Args:
        text (str): Full transcript text generated from speech-to-text.

    Returns:
        str: Cleaned transcript with sponsor and outro sections removed.
    """

    # Common phrases that typically indicate the start of sponsorships or outros
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

    # Convert transcript to lowercase for case-insensitive matching
    lower_text = text.lower()

    # Iterate through sponsor markers to find the earliest occurrence
    for marker in sponsor_markers:
        idx = lower_text.find(marker)

        # If a sponsor marker is found, truncate the transcript at that point
        if idx != -1:
            return text[:idx].strip()

    # Return the original transcript if no sponsor content is detected
    return text
