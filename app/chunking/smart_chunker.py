from models.document import Document
from models.chunk import Chunk

def smart_chunk_document(document: Document) -> list[str]:
    if not document.text:
        raise ValueError(f"Document {document.filename} has no text.")

    return smart_chunking(document.text)

def check_boundary(text:str,start:int,end:int,direction:int)-> int| None:
    for i in range(start,end,direction):
        if text[i:i+2]== '\n\n':
                    return i+2
        elif text[i] in ['.','?','!',';']:
            return i+1
        elif text[i] == '\n':
            return i+1
        elif text[i] in ['•','*']:
            return i+1
        elif text[i]==" ":
            return i+1
        
# Function to find the ideal splitting point. 1 is for Backward and 0 is for Forward
def find_boundary(text:str, ideal_position:int,left_limit:int,right_limit:int, backward:int=1)->int:
    if backward == 1:
        check= check_boundary(text,ideal_position,left_limit,-1)
        return check if check else left_limit
    elif backward == 0:
        check= check_boundary(text,ideal_position,right_limit,1)
        return check if check else right_limit
    else:
        raise ValueError("backward must be 0 or 1")


def smart_chunking(document, chunk_size:int=800, overlap:int=200) -> list:
    chunks = []
    chunk_index = 0
    start = 0
    while start < len(document.text):
        end = start + chunk_size
        if end > len(document.text):
            end = len(document.text)
        ideal_position = min(end, len(document.text) - 1)
        right_limit = min(len(document.text), end + overlap)
        boundary_position = find_boundary(document.text, ideal_position ,start, right_limit, backward=1)
        if boundary_position <= start:
            boundary_position = find_boundary(document.text, ideal_position,start,right_limit, backward=0)
        chunk_text = document.text[start:boundary_position].strip()
        if chunk_text:
            chunk=Chunk(
                chunk_index=chunk_index,
                document_id=document.document_id,
                text=chunk_text
            )
            chunks.append(chunk)
            chunk_index+=1
        new_start = boundary_position
        start = new_start

    return chunks
