def chunk_text(text, max_words=350):
    """
    Splits a long text into smaller chunks of fixed word length.

    This is useful when processing long transcripts that exceed the
    maximum context length of summarization models.

    Args:
        text (str): The full input text to be split.
        max_words (int): Maximum number of words per chunk.

    Returns:
        list[str]: A list of text chunks, each containing up to max_words words.
    """

    # Split the full text into individual words
    words = text.split()

    # List to store the resulting text chunks
    chunks = []

    # Iterate over the words list in steps of max_words
    for i in range(0, len(words), max_words):
        # Join a slice of words back into a single string
        chunk = " ".join(words[i:i + max_words])

        # Append the chunk to the chunks list
        chunks.append(chunk)

    return chunks
