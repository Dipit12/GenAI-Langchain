from langchain_google_genai import GoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv

model = GoogleGenerativeAI(model = "gemini-2.0-flash")
load_dotenv()

st.header("Reasearh Application")

user_input = st.text_input("Enter the prompt")

if st.button("Summarise"):
    result = model.invoke(user_input)
    st.write(result)