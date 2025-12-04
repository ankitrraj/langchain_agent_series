from langchain_groq import ChatGroq
import os
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

agent = create_agent(
    model=llm,
    system_prompt="you are a customer support agent from withcaring"
)

result = agent.invoke({
    "messages": [
        {"role": "user", "content": "please give me the contact to sales support"}
    ]
})

print("\nResult:", result["messages"][-1].content)
