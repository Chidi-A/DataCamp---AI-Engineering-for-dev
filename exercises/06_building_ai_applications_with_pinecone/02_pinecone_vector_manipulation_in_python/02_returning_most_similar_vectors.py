# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))

index = pc.Index('datacamp-index')

# Retrieve the top three most similar records
query_result = index.query(vector=vector, top_k=3)

print(query_result)