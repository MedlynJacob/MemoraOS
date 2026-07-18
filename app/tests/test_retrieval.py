from embeddings.embeddings_model import generate_query_embedding
from database.chroma_manager import search_embeddings

query = "Machine Learning"

query_vector = generate_query_embedding(query)

results = search_embeddings(query_vector,document_type="resume")

print("Query:")
print(query)

print("\nResults")
print("=" * 60)

documents = results["documents"][0]
metadatas = results["metadatas"][0]
similarities = results["similarities"]
for i, (doc, meta, similarity) in enumerate(zip(documents, metadatas, similarities), start=1):
    print(f"\nResult #{i}")
    print(f"Similarity: {similarity:.2f}%")
    print(f"File: {meta['filename']}")
    print(f"Chunk Index: {meta['chunk_index']}")
    print("-" * 60)
    print(doc[:300])