# Initialize the Pinecone client using your API key
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index = pc.Index('datacamp-index')

# Retrieve the MOST similar vector with genre and year filters
query_result = index.query(
    vector=vector,
    top_k=1,
    filter={"genre": {"$eq": "thriller"}, "year": {"$lt": 2018}}
)
print(query_result)