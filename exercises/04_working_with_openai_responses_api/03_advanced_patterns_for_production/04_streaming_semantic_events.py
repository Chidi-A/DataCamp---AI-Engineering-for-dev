prompt = "Explain how to read a weather forecast in one sentence for a beginner hiker."

with client.responses.create(model="gpt-5.4-mini", input=prompt, stream=True) as stream:
    for event in stream:
        # Find response created events
        if event.type == "response.created":
            print("Forecast generation started...\n")

        # Find output text completed events
        elif event.type == "response.output_text.done":
            print("\n--- Forecast complete ---\n")

        # Find response completed events
        elif event.type == "response.completed":
            print(f"\nFull forecast:\n{current_text}")