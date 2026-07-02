from dataclasses import dataclass, field
from uuid import UUID
from uuid import uuid4

def generate_id():
    return uuid4()


#Chunk dataclass to hold the chunk
@dataclass
class Chunk:
    chunk_index: int 
    document_id: UUID
    text: str
    chunk_id: UUID = field(default_factory=generate_id)
    