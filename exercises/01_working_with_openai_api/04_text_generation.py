// Exercise 4: Text Generation
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": "slogan"}],
  max_completion_tokens=100
)

print(response.choices[0].message.content)

// Exercise 5: Text Generation

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a detailed prompt
prompt = """
Create a detailed prompt to generate a product description for SonicPro headphones, including:

Active noise cancellation (ANC)

40-hour battery life

Foldable design
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    # Experiment with max_completion_tokens and temperature settings
    max_completion_tokens=400,
    temperature=0.7
)

print(response.choices[0].message.content)
