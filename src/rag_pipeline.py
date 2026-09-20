from src.retriever import retrieve_chunks
from src.llm import generate_answer

def ask_question(question, top_k=5):
    """
    Complete RAG pipeline.

    Flow:
        Question
        -> Retrieval
        -> Prompt construction
        -> LLM generation
        -> Answer + evidence
    """

    # Step 1: Retrieve relevant chunks
    retrieved_chunks = retrieve_chunks(
        question,
        top_k=top_k
    )

    # Step 2: Generate answer using retrieved context
    answer = generate_answer(
        question,
        retrieved_chunks
    )

    # Step 3: Return both answer and evidence
    return {
        "question": question,
        "answer": answer,
        "sources": retrieved_chunks
    }