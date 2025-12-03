from dotenv import load_dotenv
# from langchain_google_vertexai import ChatVertexAI
from langchain_google_genai import ChatGoogleGenerativeAI  # Google AI Studio ke liye
import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    temperature=0.3,
    google_api_key  =os.getenv("GOOGLE_API_KEY"),
)

message =[
    ("system","you are expert to transalte all language to hindi "),
    ("human","hello how are you ")
]
result = model.invoke(message)

print(result.content)





