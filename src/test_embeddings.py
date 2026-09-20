from pdf_loader import load_pdf
from chunker import create_chunks
from embedder import create_embeddings


PDF_PATH = "data/agent_as_a_judge.pdf"


# Step 1: Load PDF
pages = load_pdf(PDF_PATH)

print(f"Total pages: {len(pages)}")


# Step 2: Create chunks
chunks = create_chunks(
    pages,
    chunk_size=500,
    overlap=80
)

print(f"Total chunks: {len(chunks)}")


# Step 3: Extract chunk text
texts = [chunk["text"] for chunk in chunks]


# Step 4: Create embeddings
embeddings = create_embeddings(texts)


print("\nEmbedding test successful!")
print(f"Embedding shape: {embeddings.shape}")
print(f"Embedding dimension: {embeddings.shape[1]}")