from dotenv import load_dotenv
from langchain.agents import create_agent
import os
from langchain_groq import ChatGroq

load_dotenv()
# llm part


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3,
    groq_api_key = os.getenv("GROQ_API_KEY")
)

# AGENT
agent = create_agent(
    model=llm,

    system_prompt ="you are a pc and laptop seller to give the prices only the following laptop as use give "


)
result =agent.invoke({
    "messages":[
        {"role":"user","content":"what is the price of mac book 4 pro"}
    ]
})

# print(result["message"][-1].content)
print("\nResult:", result["messages"][-1].content)


