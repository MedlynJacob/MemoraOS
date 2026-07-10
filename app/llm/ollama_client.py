from ollama import Client

client = Client(host="http://localhost:11434")

def generate_response(prompt: str) -> str:
    if not prompt.strip():
        raise ValueError("Prompt cannot be empty.")
    try:
        response = client.generate(
            model="llama3.2:3b",
            prompt=prompt
        )
    except Exception as e:
        raise RuntimeError(f"Error generating response: {e}")  
    return response["response"]
