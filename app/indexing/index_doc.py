from loaders.document_loader import ingest_folder
from chunking.smart_chunker import smart_chunking
from embeddings.embeddings_model import generate_embeddings
from database.chroma_manager import add_embeddings, reset_collection


documents = ingest_folder("../data")
if not documents:
    raise RuntimeError("No documents found.")

reset_collection()

total_chunks = 0

for document in documents:
    try:
        chunks = smart_chunking(document)
        embeddings = generate_embeddings(chunks)
        stored = add_embeddings(document, chunks, embeddings)
        total_chunks += stored
    except Exception as e:
        print(f"Error processing document {document.filename}: {e}")
        continue

print(f"\nIndexed {len(documents)} documents.")
print(f"Stored {total_chunks} chunks.")

print("Indexing complete!")