from pdf_loader import load_pdf
from chunker import create_chunks


PDF_PATH = "data/agent_as_a_judge.pdf"


# Step 1: Extract PDF
pages = load_pdf(PDF_PATH)

print(f"Total pages: {len(pages)}")


# Step 2: Create chunks
chunks = create_chunks(
    pages,
    chunk_size=500,
    overlap=80
)

print(f"Total chunks: {len(chunks)}")


# Step 3: Display first 3 chunks
for chunk in chunks[:3]:

    print("\n" + "=" * 80)

    print(f"Chunk ID: {chunk['chunk_id']}")
    print(f"Pages: {chunk['start_page']} - {chunk['end_page']}")

    print("=" * 80)

    print(chunk["text"][:1500])