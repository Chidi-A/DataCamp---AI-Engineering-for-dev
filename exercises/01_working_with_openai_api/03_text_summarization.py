text = """
Customer: Hi, I'm having trouble with my account.
Agent: I'm sorry to hear that. Can you please provide me with more details?
Customer: Sure, I'm trying to login but I'm getting an error message.
Agent: I see. What is the error message?
Customer: "Invalid username or password."
Agent: I see. Let me help you with that.
"""

prompt = f"""
Summarize the following text:
{text}
"""

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}],
  max_completion_tokens=100
)

print(response.choices[0].message.content)

/*
Caluculate the cost of the response:

#Define price per token
input_token_price = 0.15 / 1,000,000
output_token_price = 0.60 / 1,000,000

#Calculate the number of tokens in the response
input_tokens = response.usage.prompt_tokens
output_tokens = response.usage.completion_tokens

#Calculate the cost of the response
cost = (input_tokens * input_token_price) + (output_tokens * output_token_price)
print(f"The cost of the response is ${cost:.6f}")

*/

// Exercise 3: Text Summarization

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

prompt="""Replace car with plane and adjust phrase:
A car is a vehicle that is typically powered by an internal combustion engine or an electric motor. It has four wheels, and is designed to carry passengers and/or cargo on roads or highways. Cars have become a ubiquitous part of modern society, and are used for a wide variety of purposes, such as commuting, travel, and transportation of goods. Cars are often associated with freedom, independence, and mobility."""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}],
  max_completion_tokens=100
)


# Extract and print the response text
print(response.choices[0].message.content)


// Exercise 4: Text Summarization

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Use an f-string to format the prompt
prompt = f"""Summarize the following text into two concise bullet points:
{finance_text}"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}],
  max_completion_tokens=400
)

print(response.choices[0].message.content)  