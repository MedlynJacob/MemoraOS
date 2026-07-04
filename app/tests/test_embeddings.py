from loaders.document_loader import ingest_folder
from chunking.text_splitter import split_document
from embeddings.embeddings_model import generate_embeddings


documents = ingest_folder("../data")

if not documents:
    print("No documents found.")
    exit()

document = documents[0]

chunks = split_document(document)

embeddings = generate_embeddings(chunks)

print(f"\nDocument: {document.filename}")
print(f"Chunks: {len(chunks)}")
print(f"Embeddings: {len(embeddings)}")

print("\nFirst Embedding")
print("=" * 60)

embedding = embeddings[0]

print(f"Chunk ID: {embedding.chunk_id}")
print(f"Embedding ID: {embedding.embedding_id}")
print(f"Model: {embedding.model_name}")
print(f"Dimensions: {len(embedding.vector)}")

print("\nFirst 10 values:")

for value in embedding.vector[:10]:
    print(value)