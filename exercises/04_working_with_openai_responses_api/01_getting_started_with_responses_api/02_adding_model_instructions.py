# Create a guardrailed AI response
response = client.responses.create(
    model="gpt-5.4-mini",
    instructions="You are a customer support AI that only answers questions about account balances and transaction history. Politely decline any other requests such as password resets.",
    input="Can you help me reset my password?"
)

print(response.output_text)