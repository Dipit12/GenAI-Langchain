from langchain_huggingface import HuggingFaceEmbeddings
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()


embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-mpnet-base-v2");

result = embeddings.embed_query("hello world")
print(result);