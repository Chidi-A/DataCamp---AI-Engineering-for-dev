# Define the tools
tools = load_tools(["wikipedia"])

# Define the agent
agent = create_react_agent(tools, llm)

# Invoke the agent
response = agent.invoke({"messages": [("human", "How many people live in New York City?")]})
print(response['messages'][-1].content)