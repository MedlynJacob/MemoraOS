from chatbot.chatbot import get_answer

print("MemoraOS v0.1")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    answer = get_answer(question)

    print(f"\nMemoraOS: {answer}\n")