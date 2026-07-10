from llm.ollama_client import generate_response

answer = generate_response(
    "Explain machine learning in one sentence."
)

print(answer)