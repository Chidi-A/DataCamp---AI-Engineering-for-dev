client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the system prompt
system_prompt = "a customer service chatbot for a delivery service that responds in a gentle way"
context_question = "What types of items can be delivered using MyPersonalDelivery?"
context_answer = "We deliver everything from everyday essentials such as groceries, medications, and documents to larger items like electronics, clothing, and furniture. However, please note that we currently do not offer delivery for hazardous materials or extremely fragile items requiring special handling."

# Add the context to the model
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "system", "content": system_prompt},
            {"role": "user", "content": context_question},
            {"role": "assistant", "content": context_answer },
            {"role": "user", "content": "Do you deliver furniture?"}])
response = response.choices[0].message.content
print(response)



client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the system prompt
system_prompt = f"""You are a customer service chatbot for a delivery service that responds in a gentle way.
Use the following service description to answer questions:
{service_description}"""

user_prompt = "What benefits does MyPersonalDelivery offer?"

# Get the response to the user prompt
response = get_response(system_prompt, user_prompt)

print(response)