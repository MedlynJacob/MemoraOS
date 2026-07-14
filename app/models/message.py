from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID
from uuid import uuid4


def generate_id():
    return uuid4()

@dataclass
class Message:
    role: str          
    content: str
    timestamp: datetime = field(default_factory=datetime.now)
    message_id: UUID = field(default_factory=generate_id)
