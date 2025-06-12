from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()
model =  ChatGroq(model="llama-3.3-70b-versatile")

parser = StrOutputParser()

prompt = PromptTemplate.from_template("Summarise this piece of text {content}")

loader = TextLoader("SVMData.txt", encoding = "utf-8")

result = loader.load()

content = result[0].page_content

chain = prompt | model | parser

ans = chain.invoke({"content":content})

print(ans)