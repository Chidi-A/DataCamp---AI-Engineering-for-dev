# Loop through each item in the response output
for item in response.output:
    # Check if the item is a reasoning item
    if item.type == 'reasoning':
        if item.summary:
            print(f"Reasoning: {item.summary[0]}")
        else:
            print("No reasoning summary found.")   
    
    # Check if the item is a message item
    if item.type == 'message':
        print(f"Assistant: {item.content[0].text}")