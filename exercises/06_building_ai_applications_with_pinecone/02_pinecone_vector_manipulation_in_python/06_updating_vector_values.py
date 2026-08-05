# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index = pc.Index('datacamp-index')

# Update the values of vector ID 7
index.update(id="7", values=vector)

# Fetch vector ID 7
fetched_vector = index.fetch(ids=['7'])
print(fetched_vector)