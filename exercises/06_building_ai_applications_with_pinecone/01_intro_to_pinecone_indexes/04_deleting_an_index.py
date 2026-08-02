# Set up the client with your API key
pc = Pinecone(api_key="pcsk_4Sag26_4x7aw6CwJCK6cTp798zjzX2CECFu5Dq4hhF89tnQPkTGpiYZTmTZjCJLpVjvtmr")

# Delete your Pinecone index
pc.delete_index("my-first-index")

# List your indexes
print(pc.list_indexes())