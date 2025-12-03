from dotenv import load_dotenv
from langchain_google_vertexai import ChatVertexAI

import os

load_dotenv()

model = ChatVertexAI(
    model="gemini-2.5-flash",
    temperature=0.3,
    GOOGLE_API_KEY =os.getenv("GOOGLE_API_KEY")
)

message =[
    ("instruction","you are expert to transalte all language to hindi ")
    ("user","hello how are you ")
]
result = model.invoke(message)

print(message.content)





