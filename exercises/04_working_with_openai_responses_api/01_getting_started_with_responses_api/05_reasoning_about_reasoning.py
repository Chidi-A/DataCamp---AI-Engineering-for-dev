start_time = time.time()
prompt = "How many of the letter 's' are in the sentence, 'Mississippi are possessive over their successes?'"

# Complete the challenge!
response = client.responses.create(
    model="gpt-4o-mini",
    input=prompt,
    reasoning={"effort": "none"},
    max_output_tokens=1000,
)

runtime = time.time() - start_time

print(response.output_text)
print(f"\nRuntime: {runtime:.2f} seconds")