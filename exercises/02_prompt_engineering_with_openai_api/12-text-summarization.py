// Exercise 1: Report Summarization - Report
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to summarize the report
prompt = f"""summarize the {report} in maximum five sentences, while focusing on aspects related to AI and data privacy"""

response = get_response(prompt)

print("Summarized report: \n", response)

// Exercise 2: Report Summarization - Product Description
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to summarize the product description
prompt = f"summarize the {product_description} in no more than five bullet points."

response = get_response(prompt)

print("Original description: \n", product_description)
print("Summarized description: \n", response)