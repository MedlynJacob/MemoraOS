from loaders.document_loader import ingest_folder
from chunking.text_splitter import split_document
from embeddings.embeddings_model import generate_embeddings
from database.chroma_manager import add_embeddings, collection


documents = ingest_folder("../data/resumes")

if not documents:
    raise RuntimeError("No documents found.")

document = documents[0]

chunks = split_document(document)
embeddings = generate_embeddings(chunks)

stored = add_embeddings(document, chunks, embeddings)

print(f"\nStored {stored} embeddings.")
print(f"Collection Count: {collection.count()}")