# Exercise 1: Structured outputs and conditional formats

text = "Once upon a time, in a land far, far away, there was a king who ruled with wisdom and justice. He was known for his kindness and generosity, and he was loved by his people. One day, a young girl came to him with a problem. She was a poor farmer's daughter, and she was in need of help. The king listened to her story and felt sorry for her. He gave her some money and told her to go home and live a happy life. The girl was overjoyed and thanked the king for his kindness. From that day on, the king was known as the king of the good deeds."

instructions = "You will be provided with a text delimited by triple backticks. Generate a suitable title for it."

output_format = """Use the following format for the output:
        - Text: <text we want to title>
        - Title: <the generated title>
        """


prompt = instructions + output_format + f"```{text}```"
print(get_response(prompt))


text = "Le printemps est arrivé. Les fleurs commencent à pousser. Les oiseaux reviennent. Les animaux se réveillent. Les enfants sont heureux."

prompt = f"""You will be provided with a text delimited by triple backticks. If the text is written in English, suggest a suitable title for it. If the text is written in French, suggest a suitable title for it. Otherwise, write 'I only understand English.'
```{text}```"""

print(get_response(prompt))


// Exercise 2: Structured outputs and conditional formats

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the instructions
instructions = "determine the language and generate a suitable title for the pre-loaded text excerpt that will be provided using triple backticks delimiters."

# Create the output format
output_format = """Use the following format for the output:
        - Text: <text>
        - Language: <language>
        - Title: <title>
        """

# Create the final prompt
prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)


// Exercise 3: Structured outputs and conditional formats

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the instructions
instructions = "infer the language and the number of sentences of the given delimited text; then if the text contains more than one sentence, generate a suitable title for it, otherwise, write 'N/A' for the title"

# Create the output format
output_format = """Use the following format for the output on a separate line:
        - Text: <text>
        - Language: <language>
        - Title: <title>
        number of sentences
        """

prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)