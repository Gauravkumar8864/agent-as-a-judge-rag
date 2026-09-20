import faiss
import numpy as np


def create_faiss_index(embeddings):
    """
    Create a FAISS similarity search index.

    Args:
        embeddings: Numpy array of normalized embeddings.

    Returns:
        FAISS index.
    """

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(dimension)

    embeddings = np.asarray(embeddings, dtype="float32")

    index.add(embeddings)

    return index


def search_faiss(index, query_embedding, top_k=5):
    """
    Search the FAISS index for the most similar chunks.

    Args:
        index: FAISS index.
        query_embedding: Query vector.
        top_k: Number of results to retrieve.

    Returns:
        distances and indices of the retrieved chunks.
    """

    query_embedding = np.asarray(
        query_embedding,
        dtype="float32"
    )

    if query_embedding.ndim == 1:
        query_embedding = query_embedding.reshape(1, -1)

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    return distances[0], indices[0]