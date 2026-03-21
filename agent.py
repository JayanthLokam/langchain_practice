from langchain.agents import create_agent
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

def get_weather(city: str)-> str:
    "Get weather from the give city"
    return f"It always sunny in {city}"

agent=create_agent(
    model="gpt-5.2",
    tools=[get_weather],
    system_prompt="Your an helpfull Ai Assistant. use your tools",
)

result=agent.invoke({"messages":[{"role":"user","content":"what is the weather in the mumbai?"}]})

response = result["messages"][-1].content
print(response)

