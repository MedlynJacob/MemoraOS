from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID
from uuid import uuid4

def generate_id():
    return uuid4()



#Document dataclass to hold the document information
@dataclass
class Document:
    filename: str
    filepath: str
    filetype: str
    text: str
    category: str = "Uncategorized" 
    company: str | None = None 
    document_id: UUID = field(default_factory=generate_id)
    indexed_at: datetime = field(default_factory=datetime.now)