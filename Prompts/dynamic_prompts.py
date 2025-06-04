from langchain_google_genai import GoogleGenerativeAI
import streamlit as st
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
model = GoogleGenerativeAI(model = "gemini-2.0-flash")


# detailed way
template2 = PromptTemplate(
    template='Greet this person in 5 languages. The name of the person is {name}',
    input_variables=['name']
)

# fill the values of the placeholders
prompt = template2.invoke({'name':'Dipit'})

result = model.invoke(prompt)

print(result)