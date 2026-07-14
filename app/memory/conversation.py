from dataclasses import dataclass, field

from models.message import Message


@dataclass
class Conversation:
    messages: list[Message] = field(default_factory=list)

    def add_message(self, role: str, content: str)-> None:
        self.messages.append(
            Message(
                role=role,
                content=content
            )
        )

    def get_history(self)-> list[Message]:
        return self.messages

    def clear(self)-> None:
        self.messages.clear()