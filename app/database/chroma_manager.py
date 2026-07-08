import chromadb
from config import CHROMA_DB_PATH, CHROMA_COLLECTION
client = chromadb.PersistentClient(path=CHROMA_DB_PATH)

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