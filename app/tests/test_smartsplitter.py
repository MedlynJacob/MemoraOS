from loaders.document_loader import ingest_folder
from chunking.smart_chunker import smart_chunking
from config import DATA_DIR
documents = ingest_folder(DATA_DIR)

if not documents:
    print("No documents found.")
    exit()

document = documents[0]


print(f"\nDocument: {document.filename}")

chunks = smart_chunking(document.text)

print(f"Chunks: {len(chunks)}\n")

for i, chunk in enumerate(chunks):
    print("=" * 70)
    print(f"Chunk {i}")
    print("=" * 70)
    print(chunk)
    print()