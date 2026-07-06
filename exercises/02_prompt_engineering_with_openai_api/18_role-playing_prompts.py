client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft the system_prompt using the role-playing approach
system_prompt = " role of a personalized learning advisor, to receive queries from learners about their background, experience, and goals, and accordingly, recommends a learning path of textbooks, including both beginner-level and more advanced options."

user_prompt = "Hello there! I'm a beginner with a marketing background, and I'm really interested in learning about Python, data analytics, and machine learning. Can you recommend some books?"

response = get_response(system_prompt, user_prompt)
print(response)


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

base_system_prompt = "Act as a learning advisor who receives queries from users mentioning their background, experience, and goals, and accordingly provides a response that recommends a tailored learning path of textbooks, including both beginner-level and more advanced options."

# Define behavior guidelines
behavior_guidelines = "ask a user about their background, experience, and goals, whenever any of these is not provided in the prompt."

# Define response guidelines
response_guidelines = "recommend no more than three textbooks."

system_prompt = base_system_prompt + behavior_guidelines + response_guidelines
user_prompt = "Hey, I'm looking for courses on Python and data visualization. What do you recommend?"
response = get_response(system_prompt, user_prompt)
print(response)