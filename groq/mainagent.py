from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool

from langchain import hub  # ✅ Add this


import os 
from dotenv import load_dotenv

load_dotenv()

# define tool

def calculator(expression: str) -> str:
    """Solves math expressions"""
    try:
        return str(eval(expression))
    except:
        return "Invalid expression"
    
tools=[
    Tool(
        name ="calcu",
        func= calculator,
        description = "usefull for solve math equation "

    )
]

# hub
prompt = hub.pull("hwchase17/react")


# define llm
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY")  # ✅ Added API key

    
)
#  create agent
agent = initialize_agent(
    llm=llm,
    tools = tools,
    promt = prompt,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,

)
# agent_execute = AgentExecutor(
#     agent =agent,
#     tools=tools
# )
result =agent.invoke({
    "input": "what is 2+2=?"
})

print(f"result is = {result}")




    


