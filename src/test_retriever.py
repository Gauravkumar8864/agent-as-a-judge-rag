from src.retriever import retrieve_chunks


query = "What is the DevAI benchmark?"

results = retrieve_chunks(
    query,
    top_k=5
)


print(f"Retrieved chunks: {len(results)}")

for rank, result in enumerate(results, start=1):

    print("\n" + "=" * 80)
    print(f"Rank: {rank}")
    print(f"Chunk ID: {result['chunk_id']}")
    print(
        f"Pages: "
        f"{result['start_page']} - "
        f"{result['end_page']}"
    )
    print(
        f"Similarity: "
        f"{result['similarity']:.4f}"
    )
    print("=" * 80)

    print(result["text"][:800])