client = OpenAI(api_key="<OPENAI_API_TOKEN>")

prompt = "My friend's father is twice my friend's age, and my friend is 20. How old will my friend's father be in 10 years? Let's think step by step."

response = get_response(prompt)
print(response)

// Exercise 2: One-shot chain-of-thought prompts
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the example 
example = """Q: Sum the even numbers in the following set: {9, 10, 13, 4, 2}.
             A: Even numbers: 10, 4, 2. Adding them: 10 + 4 + 2 =16"""

# Define the question
question = """Q: Sum the even numbers in the following set: {15, 13, 82, 7, 14} 
              A:"""

# Create the final prompt
prompt = "Let's think step by step."
response = get_response(prompt)
print(response)