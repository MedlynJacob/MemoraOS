#Testing if the document loader is working properly
from loaders.document_loader import loader_document, ingest_folder
from config import DATA_DIR
documents = ingest_folder(DATA_DIR)

print(f"\nLoaded {len(documents)} document(s).\n")

for doc in documents:
    print("=" * 60)
    print(f"Filename   : {doc.filename}")
    print(f"Type       : {doc.filetype}")
    print(f"ID         : {doc.document_id}")
    print(f"Indexed At : {doc.indexed_at}")
    print(f"Characters : {len(doc.text)}")
    print(f"Preview    : {doc.text[:200]}...")