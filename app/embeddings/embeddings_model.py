import os

from dotenv import load_dotenv
from ollama import Client as OllamaClient
from huggingface_hub import InferenceClient

from models.chunk import Chunk
from models.embeddings import Embedding

load_dotenv()

AI_PROVIDER = os.getenv("AI_PROVIDER", "ollama")

ollama_client = OllamaClient(host="http://localhost:11434")

hf_token = os.getenv("HF_TOKEN")
hf_client = InferenceClient(token=hf_token) if hf_token else None


def _generate_ollama_embedding(text: str) -> list[float]:
    response = ollama_client.embed(
        model="nomic-embed-text",
        input=text
    )

    return response["embeddings"][0]


def _generate_huggingface_embedding(text: str) -> list[float]:
    if hf_client is None:
        raise RuntimeError("HF_TOKEN is not configured.")

    response = hf_client.feature_extraction(
        text,
        model="BAAI/bge-small-en-v1.5"
    )

    return response.tolist()


def generate_embeddings(chunks: list[Chunk]) -> list[Embedding]:
    embeddings = []

    for chunk in chunks:
        try:
            if AI_PROVIDER == "huggingface":
                vector = _generate_huggingface_embedding(chunk.text)
                model_name = "BAAI/bge-small-en-v1.5"
            else:
                vector = _generate_ollama_embedding(chunk.text)
                model_name = "nomic-embed-text"

        except Exception as e:
            print(f"Error embedding chunk {chunk.chunk_id}: {e}")
            continue

        embedding = Embedding(
            chunk_id=chunk.chunk_id,
            vector=vector,
            model_name=model_name,
        )

        embeddings.append(embedding)

    if not embeddings:
        raise RuntimeError("No embeddings were generated.")

    return embeddings


def generate_query_embedding(query: str) -> list[float]:
    if not query.strip():
        raise ValueError("Query cannot be empty.")

    try:
        if AI_PROVIDER == "huggingface":
            return _generate_huggingface_embedding(query)

        return _generate_ollama_embedding(query)

    except Exception as e:
        raise RuntimeError(
            f"Error generating query embedding: {e}"
        )