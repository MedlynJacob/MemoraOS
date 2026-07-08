from embeddings.embeddings_model import generate_query_embedding
from database.chroma_manager import search_embeddings

query = "Machine Learning"

query_vector = generate_query_embedding(query)

results = search_embeddings(query_vector)

print("Query:")
print(query)

print("\nResults")
print("=" * 60)

documents = results["documents"][0]
metadatas = results["metadatas"][0]
distances = results["distances"][0]

for i, (doc, meta, distance) in enumerate(zip(documents, metadatas, distances), start=1):
    print(f"\nResult #{i}")
    print(f"Distance: {distance:.4f}")
    print(f"File: {meta['filename']}")
    print(f"Chunk Index: {meta['chunk_index']}")
    print("-" * 60)
    print(doc[:300])