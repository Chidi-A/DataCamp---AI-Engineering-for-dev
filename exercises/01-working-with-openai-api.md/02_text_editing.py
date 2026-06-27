prompt = """
Update name to Marteen, pronouns to he/him, and job title to Senior Software Engineer in the following text:

Joanne is a content strategist at a digital marketing agency. She is responsible for creating and implementing content strategies for clients.
"""

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)