from pdf_loader import extract_text_from_pdf
from text_splitter import split_text

pdf_path = "data/lorem-ipsum.pdf"
text = extract_text_from_pdf(pdf_path)
chunks = split_text(text)

print("Načteno znaků:", len(text))
print("Ukázka textu:")
print(text[:300])

print("Počet chunků:", len(chunks))
print("První chunk:", chunks[0][:200])