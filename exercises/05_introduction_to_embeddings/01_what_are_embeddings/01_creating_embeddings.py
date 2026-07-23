# Create an OpenAI client
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to obtain embeddings
response = client.embeddings.create(
    input="I love programming",
    model="text-embedding-3-small"
)

# Convert the response into a dictionary
response_dict = response.model_dump()
print(response_dict)

# Extract the total_tokens from response_dict
total_tokens = response_dict["usage"]["total_tokens"]
print(total_tokens)

# Extract the embeddings from response_dict
print(response_dict["data"][0]["embedding"])