import os
import json

from src.pdf_loader import load_pdf
from src.chunker import create_chunks
from src.embedder import create_embeddings
from src.vector_store import create_faiss_index


PDF_PATH = "data/agent_as_a_judge.pdf"
VECTOR_STORE_DIR = "vector_store"

INDEX_PATH = os.path.join(
    VECTOR_STORE_DIR,
    "faiss.index"
)

CHUNKS_PATH = os.path.join(
    VECTOR_STORE_DIR,
    "chunks.json"
)


def build_index():
    print("Loading PDF...")

    pages = load_pdf(PDF_PATH)

    print(f"Pages loaded: {len(pages)}")

    print("Creating chunks...")

    chunks = create_chunks(
        pages,
        chunk_size=300,
        overlap=60
    )

    print(f"Chunks created: {len(chunks)}")

    print("Creating embeddings...")

    texts = [chunk["text"] for chunk in chunks]

    embeddings = create_embeddings(texts)

    print(f"Embeddings shape: {embeddings.shape}")

    print("Creating FAISS index...")

    index = create_faiss_index(embeddings)

    print(f"FAISS index size: {index.ntotal}")

    os.makedirs(
        VECTOR_STORE_DIR,
        exist_ok=True
    )

    print("Saving FAISS index...")

    import faiss

    faiss.write_index(
        index,
        INDEX_PATH
    )

    print("Saving chunk metadata...")

    with open(
        CHUNKS_PATH,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            chunks,
            file,
            ensure_ascii=False,
            indent=2
        )

    print("\nIndex building completed successfully!")

    print(f"FAISS index: {INDEX_PATH}")
    print(f"Chunk metadata: {CHUNKS_PATH}")


if __name__ == "__main__":
    build_index()