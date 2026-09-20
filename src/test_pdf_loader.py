from pdf_loader import load_pdf


PDF_PATH = "data/agent_as_a_judge.pdf"


pages = load_pdf(PDF_PATH)

print(f"Total pages extracted: {len(pages)}")

for page in pages[:3]:
    print("\n" + "=" * 60)
    print(f"PAGE {page['page']}")
    print("=" * 60)
    print(page["text"][:1000])