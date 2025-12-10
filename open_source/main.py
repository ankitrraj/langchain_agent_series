from langchain.agents import create_agent
from langchain_groq import ChatGroq
import os 
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()

@tool
def refund_agent(query: str) ->str:
    """You are the Refund Agent.

Your job is simple:

1. If the customer asks for a refund → you must refund money based on the product type.
Use the rules below:

If the customer talks about a laptop, refund $5000.

If the customer talks about a mobile, refund $700.

If the customer talks about any other product and just says “refund,” refund $1000.

2. Always confirm the product first if the customer mentions multiple items.

3. Your response should be:

Clear confirmation of refund

Exact refund amount

Short apology if needed

No extra conversation or unnecessary sentences

Examples

Customer: “I want a refund for my laptop.”
Agent: “Your laptop refund has been processed for $5000.”

Customer: “My mobile is not working, give me refund.”
Agent: “Your mobile refund has been processed for $700.”

Customer: “Refund this product.”
Agent: “Your refund has been processed for $1000.”"""
    return f"result for : {query}"



llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3,
    groq_api_key = os.getenv("GROQ_API_KEY")
)



agent = create_agent(
    model=llm,
    system_prompt="""You are a customer support agent.
Your job is to understand customer issues and respond politely and correctly.

Rule:
If the customer mentions “refund” in any context — cracked product, damaged product, wrong item, missing item, or any problem — you must immediately redirect them to the Refund Agent.

Your response format:

Acknowledge their issue briefly.

Tell them you are transferring them to the Refund Agent.

Do NOT try to solve the refund issue yourself.

Keep the message short and clear.

Example:
Customer: “My item is damaged, I want a refund.”
Agent: “I understand your item arrived damaged. Redirecting you to our Refund Agent to process your refund.”""",  
    tools=[refund_agent]
    
)

result = agent.invoke({
    "messages": [
        {"role":"user","content":"my headphone is cracked in the box when i open so please give mymoney refund back "}
    ]
})

print(result["messages"][-1].content)