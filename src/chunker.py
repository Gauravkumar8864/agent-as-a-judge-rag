def create_chunks(pages, chunk_size=800, overlap=120):
    """
    Split extracted PDF pages into overlapping word-based chunks.

    Args:
        pages: List of dictionaries containing page number and text.
        chunk_size: Maximum number of words in each chunk.
        overlap: Number of overlapping words between consecutive chunks.

    Returns:
        List of dictionaries containing:
            - chunk_id
            - text
            - start_page
            - end_page
    """

    chunks = []

    current_words = []
    current_pages = []

    chunk_counter = 0

    for page in pages:
        page_number = page["page"]
        words = page["text"].split()

        for word in words:
            current_words.append(word)
            current_pages.append(page_number)

            if len(current_words) >= chunk_size:
                chunk_counter += 1

                chunks.append({
                    "chunk_id": f"chunk_{chunk_counter:04d}",
                    "text": " ".join(current_words),
                    "start_page": min(current_pages),
                    "end_page": max(current_pages)
                })

                # Keep overlap words for the next chunk
                current_words = current_words[-overlap:]
                current_pages = current_pages[-overlap:]

    # Add remaining words
    if current_words:
        chunk_counter += 1

        chunks.append({
            "chunk_id": f"chunk_{chunk_counter:04d}",
            "text": " ".join(current_words),
            "start_page": min(current_pages),
            "end_page": max(current_pages)
        })

    return chunks