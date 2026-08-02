# Import ServerlessSpec
from pinecone import ServerlessSpec

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_4Sag26_4x7aw6CwJCK6cTp798zjzX2CECFu5Dq4hhF89tnQPkTGpiYZTmTZjCJLpVjvtmr")

# Create your Pinecone index
pc.create_index(
    name="my-first-index", 
    dimension=256, 
    spec=ServerlessSpec(
        cloud='aws', 
        region='us-east-1'
    )
)