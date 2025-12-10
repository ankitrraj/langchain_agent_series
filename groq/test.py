# from langchain_groq import ChatGroq
# from langchain.agents import create_agent  # ✅ New API
# from langchain.tools import tool  # ✅ Using @tool decorator
# import os 
# from dotenv import load_dotenv

# load_dotenv()

# # Define tool with decorator
# @tool
# def calculator(expression: str) -> str:
#     """Useful for solving math equations. Input should be a math expression like '2+2' or '10*5'"""
#     try:
#         return str(eval(expression))
#     except Exception as e:
#         return f"Invalid expression: {str(e)}"

# # Define LLM
# llm = ChatGroq(
#     model="llama-3.1-8b-instant",
#     groq_api_key=os.getenv("GROQ_API_KEY")
# )

# # Create agent (new way!)
# agent = create_agent(
#     model=llm,
#     tools=[calculator],
#     system_prompt="You are a helpful math assistant. Solve problems accurately."
# )

# # Run agent
# result = agent.invoke({
#     "messages": [{"role": "user", "content": "What is 2+2?"}]
# })

# print(f"\nResult: {result['messages'][-1].content}")

from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()


@tool
def refund_agent(query: str) -> str:
    """Process refund request and return $1000"""
    return f"Refund processed for: {query}"


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

agent = create_agent(
    model=llm,
    tools=[refund_agent],
    system_prompt="You are a refund support agent."
)

result = agent.invoke({
    "messages": [
        HumanMessage("your refund message here")
    ]
})

print(result["messages"][-1].content)
              