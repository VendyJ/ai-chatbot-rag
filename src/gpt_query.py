from langchain_openai import ChatOpenAI
from vector_store import search_vector_store

def answer_query(query: str, store, k: int = 3) -> str:
    # Najdi relevantní chunky
    results = search_vector_store(query, store, k = k)

    # Sestav prompt pro model
    context = "\n".join([doc.page_content for doc in results])
    prompt = f"Odpověz na otázku na základě následujícího textu:\n{context}\n\nOtázka: {query}\nOdpověď: "

    # Zavolej GPT
    llm = ChatOpenAI(model = "gpt-4o-mini")
    response = llm.invoke(prompt)

    # Vrať výsledek
    return response.content