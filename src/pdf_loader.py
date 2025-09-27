import fitz

def extract_text_from_pdf(path: str) -> str:
    text = ""

    with fitz.open(path) as document:    
        for page in document:
            text += page.get_text()
    return text