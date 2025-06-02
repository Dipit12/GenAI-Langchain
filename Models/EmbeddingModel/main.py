from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
documents = [
    "Delhi is the capital of india",
    "Kolkata is the capital of WB",
    "Paris is the capital of France"
]
result = embeddings.embed_query("virat kohli is the best batsman")
result2 = embeddings.embed_documents(documents)
print(result[:5])
print("----")
print(result2)