# Exercise 1: Code Generation - Function Definition
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that asks the model for the function
prompt = " write a Python function that receives a list of 12 floats representing monthly sales data as input and, returns the month with the highest sales value as output."

response = get_response(prompt)
print(response)


# Exercise 2: Code Generation - Function Inference
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

examples="""input = [10, 5, 8] -> output = 23
input = [5, 2, 4] -> output = 11
input = [2, 1, 3] -> output = 6
input = [8, 4, 6] -> output = 18
"""

# Craft a prompt that asks the model for the function
prompt = f"Infer the Python function that maps the inputs to the outputs based on the following examples:\n{examples}"

response = get_response(prompt)
print(response)


# Exercise 3: Code Generation - Function Modification
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

function = """def calculate_area_rectangular_floor(width, length):
					return width*length"""

# Craft a multi-step prompt that asks the model to adjust the function
prompt = f"""modify the {function} according to the specified requirements:
- test if the inputs to the functions are positive
- if not, display appropriate error messages
- otherwise return the area and perimeter of the rectangle """

response = get_response(prompt)
print(response)


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a chain-of-thought prompt that asks the model to explain what the function does
prompt = f"""Explain what the following Python function does, thinking step by step:
{function}"""
 
response = get_response(prompt)
print(response)