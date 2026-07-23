# Loop through the output items
for item in response.output:
    # Check for reasoning items
    if item.type == 'reasoning':
        print('Found reasoning item')
    
    # Check for message items and extract text
    if item.type == 'message':
        message_text = item.content[0].text
        print(message_text)