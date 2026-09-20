import pymupdf


def load_pdf(pdf_path):
    """
    Extract text from a PDF page by page.

    Returns:
        list[dict]: Each dictionary contains:
            - page: page number
            - text: extracted page text
    """

    document = pymupdf.open(pdf_path)

    pages = []

    for page_number, page in enumerate(document, start=1):
        text = page.get_text("text")

        if text.strip():
            pages.append({
                "page": page_number,
                "text": text.strip()
            })

    document.close()

    return pages