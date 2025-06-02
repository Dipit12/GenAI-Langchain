from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

# Debug: check if the API token is loaded
print("Token:", os.getenv("HUGGINGFACEHUB_API_TOKEN"))

llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-small",  # known public model
    task="text2text-generation"      # correct task for flan-t5
)

model = ChatHuggingFace(llm=llm)
response = model.invoke("Who is the prime minister of India?")
print(response.content)
