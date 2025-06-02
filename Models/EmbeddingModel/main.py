from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

result = embeddings.embed_query("virat kohli is the best batsman")
print(result)