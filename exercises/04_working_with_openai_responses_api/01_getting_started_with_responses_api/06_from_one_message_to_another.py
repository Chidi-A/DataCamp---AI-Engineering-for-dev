# Create the first request
response1 = client.responses.create(
    model="gpt-5.4-mini",
    input="Draft a short LinkedIn post announcing that I'm learning about the OpenAI Responses API to upskill in AI engineering on DataCamp!",
    reasoning={"effort": "none"}
)

# Extract the ID from response1
conversation_id = response1.id

# Create the second request
response2 = client.responses.create(
    model="gpt-5.4-mini",
    input="Rewrite the LinkedIn post to include a call to action for readers to learn more about the OpenAI Responses API on DataCamp.",
    reasoning={"effort": "none"},
    previous_response_id=conversation_id,
)

print("Revised post:", response2.output_text)


sys_prompt = "..."
latest_response_id = None 

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        break

    response = client.responses.create(
        model="gpt-5.4-mini",
        instructions=sys_prompt,
        input=user_input,
        previous_response_id=latest_response_id,
    )

    print(f"Assistant: {response.output_text}")
    latest_response_id = response.id