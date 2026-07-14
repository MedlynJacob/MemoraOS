from embeddings.embeddings_model import generate_query_embedding
from database.chroma_manager import search_embeddings


def retrieve(query: str, top_k: int = 3)-> dict:
    query_vector = generate_query_embedding(query)
    if not query.strip():
        raise ValueError("Query cannot be empty.")

    results = search_embeddings(
        query_vector=query_vector,
        top_k=top_k
    )
    return "\n\n".join(results["documents"][0])