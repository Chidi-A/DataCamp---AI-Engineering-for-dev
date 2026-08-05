# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index = pc.Index('datacamp-index')

# Retrieve the MOST similar vector with the year 2024
query_result = index.query(vector=vector, filter={"year": 2024}, top_k= 1)
print(query_result)