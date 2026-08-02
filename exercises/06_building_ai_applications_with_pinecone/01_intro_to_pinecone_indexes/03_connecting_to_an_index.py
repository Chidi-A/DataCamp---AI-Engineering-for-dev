# Set up the client with your API key
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# Connect to your index
index = pc.Index("my-first-index")

# Print the index statistics
print(index.describe_index_stats())