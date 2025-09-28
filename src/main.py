from dotenv import load_dotenv
from pdf_loader import extract_text_from_pdf
from text_splitter import split_text
from vector_store import create_vector_store, search_vector_store
from gpt_query import answer_query

load_dotenv()

pdf_path = "data/lorem-ipsum.pdf"
text = extract_text_from_pdf(pdf_path)

chunks = split_text(text)

#vytvoříme vektorový index
store = create_vector_store(chunks)

#dotaz
query = "O čem je tento dokument?"
answer = answer_query(query, store)

print("Načteno znaků:", len(text))
#print("Ukázka textu:")
#print(text[:300])

print("Počet chunků:", len(chunks))
#print("První chunk:", chunks[0][:200])

#print("Výsledky: ")
#for r in results:
    #print(r.page_content[:200]) #ukázka textu

print("Odpověď: ", answer)
