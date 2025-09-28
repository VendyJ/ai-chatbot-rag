import streamlit as st
from dotenv import load_dotenv
from src.pdf_loader import extract_text_from_pdf
from src.text_splitter import split_text
from src.vector_store import create_vector_store
from src.gpt_query import answer_query

load_dotenv()

st.title("AI Chatbot s dokumenty")

# Upload PDF
uploaded_file = st.file_uploader("Nahraj PDF", type = "pdf")

if uploaded_file is not None:
    # Načíst text
    text = extract_text_from_pdf(uploaded_file)
    chunks = split_text(text)
    store = create_vector_store(chunks)
    st.success(f"Načteno {len(chunks)} chunků z PDF")

    # Dotaz
    query = st.text_input("Zadej dotaz k dokumentu: ")
    if query:
        answer = answer_query(query, store)
        st.markdown(f"**Odpověď:** {answer}")