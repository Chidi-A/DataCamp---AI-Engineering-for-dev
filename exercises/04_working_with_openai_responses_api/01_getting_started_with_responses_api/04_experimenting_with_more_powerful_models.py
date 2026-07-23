# Prompt gpt-5.4-nano with no reasoning
response = client.responses.create(
    model="gpt-5.4-nano",
    input='Write the same sentence in three tones: professional, sarcastic, and poetic. The sentence is: "The meeting could have been an email."',
  reasoning={"effort": "none"}
)

print(response.output_text)

# Prompt gpt-5.4-mini with no reasoning
response = client.responses.create(
    model="gpt-5.4-mini",
    input='Write the same sentence in three tones: professional, sarcastic, and poetic. The sentence is: "The meeting could have been an email."',
  reasoning={"effort": "none"}
)

print(response.output_text)

# Prompt gpt-5.5 with no reasoning
response = client.responses.create(
    model="gpt-5.5",
    input='Write the same sentence in three tones: professional, sarcastic, and poetic. The sentence is: "The meeting could have been an email."',
  reasoning={"effort": "none"}
)

print(response.output_text)