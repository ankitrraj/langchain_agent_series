import os
from langchain.agents import create_agent
from langchain.tools import tool
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


# first we have to create a tool 

@tool
def getrefund(query:str) ->str:
    """the user when request to refund and it has genuine reason to give his refund money 500ruppes only """
    return f"result for query:{query}"


model = ChatGroq(
    model= "llama-3.1-8b-instant",
    temperature=0.5,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

agent = create_agent(
    model= model,
    system_prompt="you are a customer support agent to reply peoples",
    tools=[getrefund]
)

result = agent.invoke({
    "messages":[
        {"role":"user","content":"my internet speed is very slow give me my refund back your plans have 300mbs but its only 10 mbps give me money refund"}
    ]
})

print(result["messages"][-1].content)