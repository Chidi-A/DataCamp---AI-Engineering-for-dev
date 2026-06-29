// Zero-shot prompting
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define a multi-line prompt to classify sentiment
prompt = """ classify the sentiment of the statements provided using the numbers 1 to 5 (positive to negative).:
1. Unbelievably good!
2. Shoes fell apart on the second use.
3. The shoes look nice, but they aren't very comfortable.
4. Can't wait to show them off!"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}],
  max_completion_tokens=100
)

print(response.choices[0].message.content)

// One-shot prompting
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define a multi-line prompt to classify sentiment
prompt = """ classify the sentiment of the statements provided using the numbers 1 to 5 (positive to negative).:
1. Unbelievably good! = 5
2. Shoes fell apart on the second use.
3. The shoes look nice, but they aren't very comfortable.
4. Can't wait to show them off!"""

# Create a request to the Chat Completions endpoint with the one-shot prompt
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}],
  max_completion_tokens=100
)

print(response.choices[0].message.content)

// Few-shot prompting
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define a multi-line prompt to classify sentiment
prompt = """ classify the sentiment of the statements provided using the numbers 1 to 5 (positive to negative).:
1. Unbelievably good! = 5
2. Shoes fell apart on the second use. = 1
3. The shoes look nice, but they aren't very comfortable. = 3
4. Can't wait to show them off! = 4"""

# Create a request to the Chat Completions endpoint with the few-shot prompt 
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}],
  max_completion_tokens=100
)

print(response.choices[0].message.content)