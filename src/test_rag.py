from src.rag_pipeline import ask_question


question = input("\nEnter your question: ")


result = ask_question(
    question,
    top_k=10
)


print("\n" + "=" * 80)
print("QUESTION")
print("=" * 80)
print(result["question"])


print("\n" + "=" * 80)
print("ANSWER")
print("=" * 80)
print(result["answer"])


print("\n" + "=" * 80)
print("RETRIEVED SOURCES")
print("=" * 80)


for rank, source in enumerate(
    result["sources"],
    start=1
):
    print("\n" + "-" * 80)

    print(f"Rank: {rank}")
    print(f"Chunk ID: {source['chunk_id']}")
    print(
        f"Pages: "
        f"{source['start_page']} - "
        f"{source['end_page']}"
    )
    print(
        f"Similarity: "
        f"{source['similarity']:.4f}"
    )

    print("\nRetrieved text:")
    print(source["text"])