prompt = "What time is 2:30pm on January 20th in New York in Tokyo time?"

# Open the streaming connection and enable tool-calling
with ____ as stream:
    for event in stream:
        # Filter for function call arguments delta events
        if ____:
            print(f"\nTool args streaming: {event.delta}")
        # Filter for function call arguments complete events
        elif ____:
            print("Tool call args complete.")
        # Filter for response completed events
        elif ____:
            print("\n--- Completed ---")