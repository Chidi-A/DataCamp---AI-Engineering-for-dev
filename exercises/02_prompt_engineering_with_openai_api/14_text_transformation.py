# Exercise 1: Text Transformation - Translation for multilingual communication
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that translates
prompt = f"translate the {marketing_message} from English to French, Spanish, and Japanese"
 
response = get_response(prompt)

print("English:", marketing_message)
print(response)

# Exercise 2: Text Transformation - Tone Transformation
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to change the email's tone
prompt = f" transform the {sample_email} by changing its tone to be professional, positive, and user-centric."

response = get_response(prompt)

print("Before transformation: \n", sample_email)
print("After transformation: \n", response)

# Exercise 3: Text Transformation - Writing improvement
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to transform the text
prompt = f"""Perform the following steps on the text delimited by triple backticks:
Step 1 - Proofread the text without changing its structure.
Step 2 - Adjust the tone to be formal and friendly.
```{text}```"""

response = get_response(prompt)

print("Before transformation:\n", text)
print("After transformation:\n", response)