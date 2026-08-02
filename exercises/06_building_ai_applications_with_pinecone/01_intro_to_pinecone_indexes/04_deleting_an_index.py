# Set up the client with your API key
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# Delete your Pinecone index
pc.delete_index("my-first-index")

# List your indexes
print(pc.list_indexes())