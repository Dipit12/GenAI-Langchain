
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model = "gemini-2.0-flash")

prompt = PromptTemplate.from_template("tell me a joke about {topic}")
parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"topic": "bears"})

print(result)