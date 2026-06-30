client = OpenAI(api_key="<OPENAI_API_TOKEN>")

code = '''
def calculate_rectangle_area(length, width):
    area = length * width
    return area
'''

# Create a prompt that analyzes correctness of the code
prompt = f""" assess the function provided in the delimited: {code}  according to the three criteria
Step 1 - correct syntax
Step 2 - receiving two inputs
Step 3 - returning one output
"""

response = get_response(prompt)
print(response)