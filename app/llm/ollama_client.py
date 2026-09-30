import os

from dotenv import load_dotenv
from ollama import Client as OllamaClient
from huggingface_hub import InferenceClient

load_dotenv()

AI_PROVIDER = os.getenv("AI_PROVIDER", "ollama")

ollama_client = OllamaClient(host="http://localhost:11434")

hf_token = os.getenv("HF_TOKEN")
hf_client = InferenceClient(token=hf_token) if hf_token else None


def _generate_ollama_response(prompt: str) -> str:
    response = ollama_client.generate(
        model="llama3.2:3b",
        prompt=prompt
    )

    return response["response"]


def _generate_huggingface_response(prompt: str) -> str:
    if hf_client is None:
        raise RuntimeError("HF_TOKEN is not configured.")

    response = hf_client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    max_tokens=2000
)

    print("RAW HF RESPONSE:")
    print(response)
    print("CHOICES:")
    print(response.choices)
    print("MESSAGE:")
    print(response.choices[0].message)

    return response.choices[0].message.content



def generate_response(prompt: str) -> str:
    if not prompt.strip():
        raise ValueError("Prompt cannot be empty.")

    try:
        if AI_PROVIDER == "huggingface":
            return _generate_huggingface_response(prompt)

        return _generate_ollama_response(prompt)

    except Exception as e:
        raise RuntimeError(
            f"Error generating response: {e}"
        )