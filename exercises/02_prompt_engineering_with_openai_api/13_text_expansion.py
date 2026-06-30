client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to expand the product's description
prompt = f""" expand the {product_description} and write a one paragraph comprehensive overview capturing the key information of the product: unique features, benefits, and potential applications.
"""

response = get_response(prompt)

print("Original description: \n", product_description)
print("Expanded description: \n", response)