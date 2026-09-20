from pdf_loader import load_pdf
from chunker import create_chunks
from embedder import create_embeddings


PDF_PATH = "data/agent_as_a_judge.pdf"


# Load PDF
pages = load_pdf(PDF_PATH)

# Create chunks
chunks = create_chunks(
    pages,
    chunk_size=500,
    overlap=80
)

# Extract chunk text
texts = [chunk["text"] for chunk in chunks]

# Create embeddings
embeddings = create_embeddings(texts)


print(f"Total chunks: {len(chunks)}")
print(f"Embedding shape: {embeddings.shape}")
print(f"Embedding data type: {embeddings.dtype}")