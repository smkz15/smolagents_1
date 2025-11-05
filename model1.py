from smolagents import CodeAgent, LiteLLMModel, DuckDuckGoSearchTool

model = LiteLLMModel(model_id="ollama_chat/mistral-small:24b", api_base="http://127.0.0.1:11434", num_ctx=8192)
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    response = agent.run(user_input)
    print(f"Agent: {response}")
