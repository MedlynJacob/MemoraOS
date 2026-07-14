from chatbot.chatbot import get_answer
from memory.conversation import Conversation

print("MemoraOS v0.1")
print("Type 'exit' to quit.\n")

conversation_history = Conversation()

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    conversation_history.add_message(
        role="user",
        content=question
    )

    answer = get_answer(
        question,
        history=conversation_history.get_history()
    )
    

    conversation_history.add_message(
        role="assistant",
        content=answer
    )

    print(f"\nMemoraOS: {answer}\n")