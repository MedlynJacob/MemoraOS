from embeddings.embeddings_model import generate_query_embedding
from database.chroma_manager import search_embeddings


def retrieve(query: str, top_k: int = 3, document_type: str | None = None)-> dict:
    if not query.strip():
        raise ValueError("Query cannot be empty.")
    query_vector = generate_query_embedding(query)


    results = search_embeddings(
        query_vector=query_vector,
        top_k=top_k,
        document_type=document_type
    )
    return {
    "documents": results["documents"][0],
    "metadatas": results["metadatas"][0],
    "similarities": results["similarities"]
}