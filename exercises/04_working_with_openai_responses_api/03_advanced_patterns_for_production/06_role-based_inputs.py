# Convert this request to use role-based messages
response = client.responses.create(
    model="gpt-5.4-mini",
    instructions="You are a product cataloging expert who provides concise descriptions.",
    input="A mustard-yellow colored winter jacket."
)

print(response.output_text)


# Convert this request to use role-based messages
response = client.responses.create(
    model="gpt-5.4-mini",
    input=[
        {"role": "system",
         "content": "You are a product cataloging expert who provides concise descriptions."},
         {"role": "user",
         "content": "A mustard-yellow colored winter jacket."}
    ]
)

print(response.output_text)