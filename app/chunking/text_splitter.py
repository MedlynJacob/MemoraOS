from config import CHUNK_SIZE, CHUNK_OVERLAP
from models.chunk import Chunk

def split_document(document,chunk_size=CHUNK_SIZE,overlap=CHUNK_OVERLAP):
    text=document.text
    chunks=[]
    chunk_index=0
    start=0
    overlap_size=overlap
    while start<len(text):
        end=start+chunk_size
        if end>len(text):
            end=len(text)
        while end>start and text[end-1]!=" ":
            end-=1
        if end == start:
            end = min(start + chunk_size, len(text))
        chunk_text=text[start:end].strip()
        if chunk_text:
            chunk=Chunk(
                chunk_index=chunk_index,
                document_id=document.document_id,
                text=chunk_text
            )
            chunks.append(chunk)
            chunk_index+=1
        start=max(0,end-overlap_size)
        while start < len(text) and text[start] != " ":
            start += 1
        if end == len(text):
            break
    return chunks
