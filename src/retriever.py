import json
import faiss

from src.embedder import create_embeddings
from src.vector_store import search_faiss

INDEX_PATH = "vector_store/faiss.index"
CHUNKS_PATH = "vector_store/chunks.json"


def load_vector_store():
    """
    Load the saved FAISS index and chunk metadata.

    Returns:
        index: FAISS vector index
        chunks: List of chunk metadata
    """

    index = faiss.read_index(INDEX_PATH)

    with open(
        CHUNKS_PATH,
        "r",
        encoding="utf-8"
    ) as file:
        chunks = json.load(file)

    return index, chunks


def retrieve_chunks(query, top_k=5):
    """
    Retrieve the most relevant chunks for a user query.

    Args:
        query: User's question.
        top_k: Number of chunks to retrieve.

    Returns:
        List of retrieved chunks with similarity scores.
    """

    index, chunks = load_vector_store()

    query_embedding = create_embeddings([query])

    distances, indices = search_faiss(
        index,
        query_embedding,
        top_k=top_k
    )

    results = []

    for distance, index_id in zip(distances, indices):

        if index_id < 0:
            continue

        chunk = chunks[index_id].copy()

        chunk["similarity"] = float(distance)

        results.append(chunk)

    return results