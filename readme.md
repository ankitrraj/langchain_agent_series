# this is the all models and agentic ai series to learn agents 

## in that series we learn about agents || how llm workds

## tool calling
## context managment 
## RAG
## tokens managment
## pipelines
## pipelinesparsing large data(PDF)
## retry 

```python
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
```

```
Week 1: LLM Basics
Day 1-2: Understanding LLMs
 What are LLMs? (GPT, Claude, Llama basics)
 Tokens, Context Window, Temperature
 Prompt Engineering basics
 API calls (OpenAI, Groq setup)

```
# Next Step
```
Day 3-4: Prompt Engineering
 Zero-shot, Few-shot, Chain-of-Thought prompting
 System prompts vs User prompts
 Temperature, Top-p, Max tokens
 Prompt templates
Practice:
```
# Next Step

```
Day 5-7: LangChain Basics
 LangChain architecture
 Chains (LLMChain, SequentialChain)
 Prompt Templates
 Output Parsers
 Memory (ConversationBufferMemory)
Mini Project: Simple chatbot with memory

```
# its the phase 1




