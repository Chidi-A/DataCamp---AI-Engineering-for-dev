client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(system_prompt, user_prompt):
  # Assign the role and content for each message
  messages = [{"role": system, "content": system_prompt},
      		  {"role": user, "content": user_prompt}]  
  response = client.chat.completions.create(
      model="gpt-4o-mini", messages= messages, temperature=0)
  
  return response.choices[0].message.content

# Try the function with a system and user prompts of your choice 
response = get_response(
    "You are a helpful assistant that answers questions concisely.",
    "What is the difference between a list and a tuple in Python?"
)
print(response)



# Dual-prompting Example - Customer Support Chatbot
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the purpose of the chatbot
chatbot_purpose = "customer support chatbot for an e-commerce company specializing in electronics,  handles customer support, specializes in electronics, and is there to assist with inquiries, order tracking, and troubleshooting"

# Define audience guidelines
audience_guidelines = "target audience are tech-savvy individuals interested in purchasing electronic gadgets"

# Define tone guidelines
tone_guidelines = "use a professional and user-friendly tone while interacting with customers"

system_prompt = chatbot_purpose + audience_guidelines + tone_guidelines
response = get_response(system_prompt, "My new headphones aren't connecting to my device")
print(response)