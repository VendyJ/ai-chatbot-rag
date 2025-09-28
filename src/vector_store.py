from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

def create_vector_store(chunks: list[str]) -> FAISS:
    # inicializace embedderu (OpenAI)
    embeddings = OpenAIEmbeddings()

    # vytvoření FAISS indexu přímo z chunků
    store = FAISS.from_texts(chunks, embeddings)

    return store

def search_vector_store(query, store, k=3):
    # vyhledání podobných chunků
    results = store.similarity_search(query, k=k)
    return results
