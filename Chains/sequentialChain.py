from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()

model =GoogleGenerativeAI(model = "gemini-2.0-flash")

parser = StrOutputParser()

prompt_1 = PromptTemplate.from_template("Write a detailed report on {topic}")

prompt_2 = PromptTemplate.from_template("Give 5 most points from the report : {report}")

chain = prompt_1 | model | parser | prompt_2 | model | parser

result = chain.invoke({"topic":"tigers"})

print(result)

chain.get_graph().print_ascii()