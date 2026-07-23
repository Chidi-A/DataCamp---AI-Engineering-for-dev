# Define an OpenAI API client
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the OpenAI API request
response = client.responses.create(
    model="gpt-5.4-mini",
    input="In simple terms, what is the OpenAI Responses API?",
    reasoning={"effort": "none"},
    max_output_tokens=100
)

# Print the generated text from the response
print(response.output_text)