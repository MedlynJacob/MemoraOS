from loaders.document_loader import ingest_folder
from chunking.text_splitter import split_document
from config import DATA_DIR
documents = ingest_folder(DATA_DIR)

if not documents:
    print("No documents found.")
    exit()

document = documents[0]

chunks = split_document(document)

print(f"\nDocument: {document.filename}")
print(f"Total Chunks: {len(chunks)}\n")

for chunk in chunks:
    print("=" * 70)
    print(f"Chunk #{chunk.chunk_index}")
    print(f"Chunk ID: {chunk.chunk_id}")
    print(f"Document ID: {chunk.document_id}")
    print(f"Characters: {len(chunk.text)}")
    print("-" * 70)
    print(chunk.text[:250])   # Preview
    print()