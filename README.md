# AI Chatbot s vyhledáváním v dokumentech (RAG)

Tento projekt ukazuje princip **Retrieval-Augmented Generation (RAG)**:  
Uživatel nahraje PDF dokument a chatbot odpovídá na otázky na základě jeho obsahu.

---

## Jak spustit

1. Naklonuj si repozitář:
   ```bash
   git clone https://github.com/VendyJ/ai-chatbot-rag.git
   cd ai-chatbot-rag

2. Vytvoř prostředí (např. Conda):
   conda create -n ai-chatbot-rag python=3.11
   conda activate ai-chatbot-rag
   pip install -r requirements.txt

3. Vytvoř .env soubor v rootu projektu:
   OPENAI_API_KEY=sk-VÁŠ-KLÍČ

4. Spusť ukázku:
   python src/main.py
