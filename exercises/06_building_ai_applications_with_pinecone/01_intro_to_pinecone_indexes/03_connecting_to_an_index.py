# Set up the client with your API key
pc = Pinecone(api_key="pcsk_4Sag26_4x7aw6CwJCK6cTp798zjzX2CECFu5Dq4hhF89tnQPkTGpiYZTmTZjCJLpVjvtmr")

# Connect to your index
index = pc.Index("my-first-index")

# Print the index statistics
print(index.describe_index_stats())