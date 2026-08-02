# Import ServerlessSpec
from pinecone import ServerlessSpec

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# Create your Pinecone index
pc.create_index(
    name="my-first-index", 
    dimension=256, 
    spec=ServerlessSpec(
        cloud='aws', 
        region='us-east-1'
    )
)