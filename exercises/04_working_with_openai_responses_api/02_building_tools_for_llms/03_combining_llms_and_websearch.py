# Create a response with web search enabled
response = client.responses.create(
    model="gpt-5.4-mini",
    tools=[{
        "type": "web_search",
    }],
    input="What is the current temperature in Berlin, Germany?"
)

# Print the output text
print(response.output_text)