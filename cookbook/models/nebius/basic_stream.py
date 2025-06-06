from agno.agent import Agent
from agno.models.nebius import Nebius

agent = Agent(
    model=Nebius(),
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

# Print the response in the terminal
agent.print_response("write a two sentence horror story", stream=True)
