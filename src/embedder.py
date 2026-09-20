from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"


def create_embeddings(texts):
    """
    Convert text chunks into vector embeddings.

    Args:
        texts: List of text strings.

    Returns:
        Numpy array containing embeddings.
    """

    model = SentenceTransformer(MODEL_NAME)

    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return embeddings