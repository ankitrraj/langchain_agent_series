from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

# TOOL
@tool
def add(a: int, b: int) -> int:
    """Do simple addition."""
    return a + b

# MODEL - Google Gemini ka correct model name use karo
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # Ya "gemini-3-pro-preview" use kar sakte ho
    api_key=os.getenv("GEMINI_API_KEY")  # Correct parameter name
)

# AGENT
agent = create_agent(
    model=model,
    tools=[add],
    system_prompt="You are a helpful assistant that can do math."
)

# RUN - Correct message format
result = agent.invoke({
    "messages": [
        {"role": "user", "content": "What is 5 + 3?"}
    ]
})

print(result["messages"][-1].content)