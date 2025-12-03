from langchain_groq import ChatGroq # module load
from dotenv import load_dotenv # env load 
import os

# Load environment variables from .env file
load_dotenv()

# API key automatically miljayegi
model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2,
    # groq_api_key=os.getenv("GROQ_API_KEY")  # Explicitly pass bhi kar sakte ho
)

messages = [
    ("system", """You are a helpful translator. Translate the user sentence to hindi.
    Rules:
     -always solve the math question
     -strcit only the math equation
     -only one line answer
     


    
    """),
    ("user","how are you")
    
]

result = model.invoke(messages)
print(result.content)