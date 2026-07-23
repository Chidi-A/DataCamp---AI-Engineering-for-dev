# Create a response with web search enabled and sources included
response = client.responses.create(
    model="gpt-5.4-mini",
    tools=[{"type": "web_search"}],
    input="What is the current stock price of Netflix?",
    include=["web_search_call.action.sources"]
)

# Extract and print sources from web search calls
for item in response.output:
    if item.type == "web_search_call":
        print(item.action.sources)
        
print(response.output_text)