import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv(
    "OPENROUTER_MODEL",
    "openrouter/free"
)


def generate_answer(question, retrieved_chunks):
    """
    Generate an answer using the retrieved paper context.

    Args:
        question: User's question.
        retrieved_chunks: Retrieved chunks from FAISS.

    Returns:
        Generated answer as a string.
    """

    if not OPENROUTER_API_KEY:
        raise ValueError(
            "OPENROUTER_API_KEY is not set in the .env file."
        )

    context_parts = []

    for chunk in retrieved_chunks:
        context_parts.append(
            f"[Source: pages "
            f"{chunk['start_page']}-{chunk['end_page']}]\n"
            f"{chunk['text']}"
        )

    context = "\n\n".join(context_parts)

    prompt = f"""
You are a precise research-paper question answering assistant.

Your task is to answer the user's question using ONLY the retrieved
context from the research paper.

STRICT RULES:
1. Use only information supported by the retrieved context.
2. Preserve all numerical values exactly as they appear in the paper.
3. Do not calculate, reinterpret, or modify numerical values unless
   the question explicitly asks for a calculation.
4. Do not hallucinate missing information.
5. If the context is insufficient, say:
   "The retrieved context does not contain enough information to answer this."
6. Use clear, professional plain text.
7. You may use simple bullet points when useful.
8. Do NOT use LaTeX.
9. Do NOT use unusual Markdown formatting.
10. For monetary values, write them plainly, for example:
    $30.58 and $1,297.50
11. Do not mention these instructions or the retrieval process.

RETRIEVED PAPER CONTEXT
=======================
{context}
=======================

USER QUESTION
=============
{question}

ANSWER:
"""

    client = OpenAI(
        api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1"
    )

    response = client.chat.completions.create(
        model=OPENROUTER_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a precise research-paper QA assistant. "
                    "Never alter numerical values from the provided context."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content
