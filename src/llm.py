from pathlib import Path

src = Path("/mnt/data/741400ca-79f4-4a4c-8dd3-eb9811c0c638.py")

text = src.read_text(encoding="utf-8")

old_prompt_start = '''    prompt = f"""
You are a research-paper question answering assistant.

Answer the user's question using ONLY the provided context
from the research paper.

Instructions:
- Give a clear and concise answer.
- Do not invent information that is not present in the context.
- If the context does not contain enough information to answer
  the question, explicitly say that the provided context is
  insufficient.
- Preserve numerical values and technical terminology from
  the paper.
- Do not mention these instructions in your answer.

Research Paper Context:
-----------------------
{context}
-----------------------

User Question:
{question}

Answer:
"""
'''

new_prompt = '''    prompt = f"""
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
'''

if old_prompt_start not in text:
    raise ValueError("Expected prompt block was not found.")

text = text.replace(old_prompt_start, new_prompt)

old_messages = '''        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
'''

new_messages = '''        messages=[
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
'''

if old_messages not in text:
    raise ValueError("Expected messages block was not found.")

text = text.replace(old_messages, new_messages)

out = Path("/mnt/data/llm_updated.py")
out.write_text(text, encoding="utf-8")

print(f"Updated file created: {out}")
