from ollama import Client
from models.chunk import Chunk
from models.embeddings import Embedding

client = Client(host="http://localhost:11434")


def generate_embeddings(chunks: list[Chunk]) -> list[Embedding]:
    embeddings = []

    for chunk in chunks:
        try:
            response = client.embed(
                model="nomic-embed-text",
                input=chunk.text
            )
        except Exception as e:
            print(f"Error embedding chunk {chunk.chunk_id}: {e}")
            continue

        embedding = Embedding(
            chunk_id=chunk.chunk_id,
            vector=response["embeddings"][0],
            model_name="nomic-embed-text",
        )

        embeddings.append(embedding)
    if not embeddings:
        raise RuntimeError("No embeddings were generated.")

    return embeddings
