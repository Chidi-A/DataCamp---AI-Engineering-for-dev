# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
index = pc.Index('datacamp-index')

# Upsert vector_set1 to namespace1
index.upsert(
  vectors=vector_set1,
  namespace="namespace1"
)

# Upsert vector_set2 to namespace2
index.upsert(
  vectors=vector_set2,
  namespace="namespace2"
)

# Print the index statistics
print(index.describe_index_stats())


# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))

index = pc.Index('datacamp-index')

# Query namespace1 with the vector provided
query_result = index.query(vector=vector, namespace='namespace1', top_k=3)
print(query_result)