from embeddings.embeddings_model import generate_query_embedding
from database.chroma_manager import search_embeddings
from retrieval.query_classifier import detect_document_type

def retrieve(query: str, top_k: int = 3, document_type: str | None = None, company: str | None = None)-> dict:
    if not query.strip():
        raise ValueError("Query cannot be empty.")
    # Detect document type if not specified
    if document_type is None:
        document_type = detect_document_type(query)
    query_vector = generate_query_embedding(query)


    results = search_embeddings(
        query_vector=query_vector,
        top_k=top_k,
        document_type=document_type,
        company=company
    )
    return {
    "documents": results["documents"][0],
    "metadatas": results["metadatas"][0],
    "similarities": results["similarities"]
}
