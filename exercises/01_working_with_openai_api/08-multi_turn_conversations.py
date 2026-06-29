messages = [{"role": "system", "content":"You are a data science tutor who provides short, simple explanations"}]

user_qs = ["Why is Python so popular?", "Summarize this in one sentence."]

for q in user_qs:
    print("User: ", q)

    user_dict = {"role":"user", "content":q}
    messages.append(user_dict)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    assistant_dict = {"role":"assistant", "content":response.choices[0].message.content}
    messages.append(assistant_dict)

    print("Assistant: ", response.choices[0].message.content)