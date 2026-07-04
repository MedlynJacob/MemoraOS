from dataclasses import dataclass, field
from uuid import UUID
from uuid import uuid4
from datetime import datetime

def generate_id():
    return uuid4()
@dataclass
class Embedding:
    chunk_id: UUID
    vector: list[float]
    model_name: str
    embedded_at: datetime = field(default_factory=datetime.now)
    embedding_id: UUID = field(default_factory=generate_id)