from pdf_loader import load_pdf
from chunker import create_chunks
from embedder import create_embeddings
from vector_store import create_faiss_index, search_faiss


PDF_PATH = "data/agent_as_a_judge.pdf"


# 1. Load PDF
pages = load_pdf(PDF_PATH)

# 2. Create chunks
chunks = create_chunks(
    pages,
    chunk_size=500,
    overlap=80
)

# 3. Create embeddings
texts = [chunk["text"] for chunk in chunks]
embeddings = create_embeddings(texts)

# 4. Create FAISS index
index = create_faiss_index(embeddings)

print(f"Total chunks: {len(chunks)}")
print(f"FAISS index size: {index.ntotal}")
print(f"Embedding dimension: {index.d}")


# 5. Test query
query = "What is the DevAI benchmark?"

query_embedding = create_embeddings([query])

distances, indices = search_faiss(
    index,
    query_embedding,
    top_k=5
)


print("\nTop retrieved chunks:")

for rank, (distance, index_id) in enumerate(
    zip(distances, indices),
    start=1
):
    chunk = chunks[index_id]

    print("\n" + "=" * 70)
    print(f"Rank: {rank}")
    print(f"Chunk ID: {chunk['chunk_id']}")
    print(f"Pages: {chunk['start_page']} - {chunk['end_page']}")
    print(f"Similarity: {distance:.4f}")
    print("=" * 70)
    print(chunk["text"][:500])