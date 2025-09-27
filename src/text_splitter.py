def split_text(text, chunk_size=500, overlap=50):
    chunks = []
    index = 0
    while index < len(text):
        substring = text[index:index+chunk_size]
        chunks.append(substring)
        index += (chunk_size - overlap)
    return chunks