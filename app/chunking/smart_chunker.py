
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

def smart_chunking(text:str, chunk_size:int=800, overlap:int=200) -> list:
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        if end > len(text):
            end = len(text)
        ideal_position = min(end, len(text) - 1)
        right_limit = min(len(text), end + overlap)
        boundary_position = find_boundary(text, ideal_position ,start, right_limit, backward=1)
        if boundary_position <= start:
            boundary_position = find_boundary(text, ideal_position,start,right_limit, backward=0)
        chunk_text = text[start:boundary_position].strip()
        if chunk_text:
            chunks.append(chunk_text)
        new_start = boundary_position
        start = new_start

    return chunks
