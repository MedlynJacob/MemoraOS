from embeddings.embeddings_model import generate_query_embedding

query = "Machine Learning"

vector = generate_query_embedding(query)

print(f"Dimensions: {len(vector)}")
print()

print("First 10 values:")

for value in vector[:10]:
    print(value)