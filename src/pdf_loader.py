import fitz #PyMuPDF

def extract_text_from_pdf(file) -> str:
    text = ""
    if hasattr(file, "read"):
    # Streamlit soubor (má .read)
        bytes_data = file.read()
        pdf_document = fitz.open(stream = bytes_data, filetype = "pdf")
    else:
        # Lokální soubor podle cesty
        pdf_document = fitz.open(file)

    for page in pdf_document:
            text += page.get_text()   
        
    return text