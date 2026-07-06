// Exercise 1: Text Analysis - Ticket Classification

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to classify the ticket
prompt = f"classify the {ticket} as technical issue, billing inquiry, or product feedback, without providing anything else in the response."

response = get_response(prompt)

print("Ticket: ", ticket)
print("Class: ", response)

# Exercise 2: Text Analysis - Ticket Entities Extraction

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a few-shot prompt to get the ticket's entities
prompt = f"""Ticket: {ticket_1}
Entities: {entities_1}
Ticket: {ticket_2}
Entities: {entities_2}
Ticket: {ticket_3}
Entities: {entities_3}
Ticket: {ticket_4}
Entities:"""

response = get_response(prompt)

print("Ticket: \n", ticket_4)
print("Entities: \n", response)