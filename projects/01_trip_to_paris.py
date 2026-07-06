# Start your code here!
import os
from openai import OpenAI

# Define the model to use
model = "gpt-4o-mini"

# Define the client
client = OpenAI()

# Start coding here
# Add as many cells as you like

conversation = [
    {"role": "system",
     "content": "You are a knowledgeable Parisian tour guide who answers tourists' questions about Paris."}
]
questions = [
    "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
    "Where is the Arc de Triomphe?",
    "What are the must-see artworks at the Louvre Museum?"
]

for question in questions:
    # Add the user's question to the running conversation
    conversation.append({"role": "user", "content": question})
    # Send the WHOLE conversation each time so the model keeps context
    response = client.chat.completions.create(
        model=model,
        messages=conversation,
        temperature=0.0,
        max_tokens=100
    )

     # Extract the answer and add it back into the conversation
    answer = response.choices[0].message.content

    conversation.append({"role": "assistant", "content": answer})
    
    print(f"Q: {question}")
    print(f"A: {answer}\n")