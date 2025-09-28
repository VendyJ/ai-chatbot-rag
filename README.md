# AI Chatbot s vyhledáváním v dokumentech (RAG)

Tento projekt ukazuje princip **Retrieval-Augmented Generation (RAG)**:  
Uživatel nahraje PDF dokument a chatbot odpovídá na otázky na základě jeho obsahu.

---

# Funkcionalita

- Načtení textu z PDF
- Rozdělení dokumentu na menší části (chunky) s překryvem
- Uložení embeddingů do FAISS vektorového úložiště
- Vyhledání relevantních chunků k uživatelskému dotazu
- Odpověď pomocí OpenAI GPT modelu s využitím kontextu z dokumentu
- Jednoduchý webový frontend postavený na Streamlit

# Ukázka

![Ukázka aplikace](screenshot.png)

# Jak spustit

1. Naklonuj si repozitář:

   git clone https://github.com/VendyJ/ai-chatbot-rag.git
   cd ai-chatbot-rag

2. Vytvoř prostředí (např. Conda):

   conda create -n ai-chatbot-rag python=3.11
   conda activate ai-chatbot-rag
   pip install -r requirements.txt

3. Vytvoř .env soubor v rootu projektu:

   OPENAI_API_KEY=sk-TVŮJ-KLÍČ

   ! -> API klíč si vygeneruj v https://platform.openai.com/
   ! -> Pokud nemáš platební metodu v OpenAI API, je potřeba tak učinit (stačí nabít malá částka, např. 5$)
   ! -> Klíč NIKDY nesdílej veřejně!

4. Spusť ukázku:

   python src/main.py

   NEBO

   Spusť aplikaci v prohlížeči:

   streamlit run src/app.py

# Struktura projektu

ai-chatbot-rag/
│── src/
│   ├── main.py          # Ukázkový skript pro běh z terminálu
│   ├── pdf_loader.py    # Extrakce textu z PDF
│   ├── text_splitter.py # Rozdělení textu na chunky
│   ├── vector_store.py  # FAISS vektorový store
│   └── gpt_query.py     # Funkce pro dotazování GPT
│── app.py               # Streamlit frontend
│── data/                # Testovací PDF
│── .env                 # API klíč (není v Gitu)
│── .gitignore
│── requirements.txt
│── README.md

# Možné vylepšení

- Nasazení aplikace na Streamlit Cloud
- Podpora více formátů (Word, TXT)
- Zvýraznění pasáží v dokumentu, ze kterých odpověď pochází
- Více dotazů v konverzačním režimu