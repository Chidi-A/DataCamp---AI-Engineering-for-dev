client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a one-shot prompt
prompt = """Q: Extract the odd numbers from the set {1, 3, 7, 12, 19}.
            A: {1, 3, 7, 19}
            Q: Extract the odd numbers from the set {3, 5, 11, 12, 16}.
            A:
            """

response = get_response(prompt)
print(response)