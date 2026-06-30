// Exercise 1: Iterative Prompt Engineering - Standard prompt
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Refine the following prompt
prompt = "Provide a table of the top 10 pre-trained language models, with columns for the model name, release year, and owning company."

response = get_response(prompt)
print(response)

// Exercise 2: Iterative Prompt Engineering - Few shot prompt engineering
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Refine the following prompt
prompt = """
Receiving a promotion at work made me feel on top of the world -> Happiness
The movie's ending left me with a heavy feeling in my chest -> Sadness
Walking alone in the dark alley sent shivers down my spine -> Fear
____
____
They sat and ate their meal ->
"""

response = get_response(prompt)
print(response)