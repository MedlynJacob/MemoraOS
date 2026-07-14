from models.chunk import Chunk

def check_boundary(text:str,start:int,end:int,direction:int)-> int| None:
    for i in range(start,end,direction):
        if text[i:i+2]== '\n\n':
                    return i+2
        elif text[i] in ['•']:
            return i+1
        elif text[i] in ['.','?','!']:
            return i+1
        elif text[i] == '\n':
            return i+1
        elif text[i] == ';':
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
        end = min(start + chunk_size, len(document.text))
        ideal_position = min(end, len(document.text)-1)
        right_limit = min(len(document.text), end)
        search_start = start + (overlap if start > 0 else 0)
        boundary_position = find_boundary(
            document.text,
            ideal_position,
            search_start,
            right_limit,
            backward=1
        )
        if boundary_position <= search_start:
            boundary_position = find_boundary(
                document.text,
                ideal_position,
                search_start,
                right_limit,
                backward=0
            )

        if boundary_position == start:
            break
        
        print(
            f"""
        START: {start}
        END: {boundary_position}
        SIZE: {boundary_position-start}

        ENDING TEXT:
        {document.text[boundary_position-50:boundary_position+50]}

        {'='*50}
        """
        )

        chunk_text = document.text[start:boundary_position].strip()

        if chunk_text:
            chunks.append(
                Chunk(
                    chunk_index=chunk_index,
                    document_id=document.document_id,
                    text=chunk_text
                )
            )

            chunk_index += 1
        if boundary_position >= len(document.text):
           break

        new_start = boundary_position - overlap

        if new_start <= start:
            new_start = boundary_position

        start = new_start

    return chunks
