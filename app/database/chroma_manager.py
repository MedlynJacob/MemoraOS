import chromadb
from config import CHROMA_DB_PATH, CHROMA_COLLECTION
client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
from sklearn.metrics.pairwise import cosine_similarity


collection = client.get_or_create_collection(
    name=CHROMA_COLLECTION
)

def add_embeddings(document, chunks, embeddings)-> int:
    ids = []
    documents = []
    metadatas = []
    vectors = []
    if len(chunks) != len(embeddings):
        raise ValueError("Chunks and embeddings count do not match.")
    if not chunks:
        return 0
    
    for chunk, embedding in zip(chunks, embeddings):
        ids.append(str(chunk.chunk_id))
        documents.append(chunk.text)
        metadatas.append({
            "document_id": str(document.document_id),
            "chunk_index": chunk.chunk_index,
            "chunk_id": str(chunk.chunk_id),
            "embedding_id": str(embedding.embedding_id),
            "model_name": embedding.model_name,
            "embedded_at": embedding.embedded_at.isoformat(),
            "filename": document.filename,
            "category": document.category or "",
            "company": document.company or "",
            "document_type": document.document_type,
        })
        vectors.append(embedding.vector)    
    collection.add(
        ids=ids,
        documents=documents,
        metadatas=metadatas,
        embeddings=vectors
    )
    return len(ids)

def reset_collection():
    client.delete_collection(CHROMA_COLLECTION)

    global collection
    collection = client.get_or_create_collection(
        name=CHROMA_COLLECTION
    )


def count_embeddings() -> int:
    return collection.count()

def search_embeddings(query_vector: list[float], top_k: int = 5, document_type: str | None = None, company: str | None = None):
    query_args = {
    "query_embeddings": [query_vector],
    "n_results": top_k,
    "include": ["documents", "metadatas", "embeddings"]
    }
    filters = []
    if document_type:
        filters.append({"document_type": document_type})
    if company:
        filters.append({"company": company})
    if len(filters) == 1:
        query_args["where"] = filters[0]
    elif len(filters) > 1:
        query_args["where"] = { "$and": filters }
    
    results = collection.query(**query_args)
    if len(results["embeddings"][0]) == 0:
        results["similarities"] = []
        return results

    matrix = cosine_similarity(
    [query_vector],
    results["embeddings"][0]
)

    results["similarities"] = [
    float(score * 100)
    for score in matrix[0]
]

    return results

