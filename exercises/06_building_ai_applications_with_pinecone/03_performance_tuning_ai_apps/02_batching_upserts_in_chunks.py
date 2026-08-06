# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index = pc.Index('datacamp-index')

# Upsert vectors in batches of 100
for chunk in chunks(vectors):
    index.upsert(vectors=chunk) 

# Retrieve statistics of the connected Pinecone index
print(index.describe_index_stats())