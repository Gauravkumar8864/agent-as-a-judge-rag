from src.llm import generate_answer


question = "What is the DevAI benchmark?"

context = [
    {
        "start_page": 11,
        "end_page": 12,
        "text": (
            "DevAI distinguishes itself from other benchmarks by "
            "focusing on realistic user queries that target a complete "
            "development cycle. It includes comprehensive evaluation "
            "with multiple hierarchical requirements and preferences."
        )
    }
]


answer = generate_answer(
    question,
    context
)


print("\nGenerated Answer:")
print("=" * 70)
print(answer)