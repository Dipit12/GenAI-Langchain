from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()

model = GoogleGenerativeAI(model = "gemini-2.0-flash")

parser = JsonOutputParser()

template_1 = PromptTemplate(
    template = "Give me the name, age and city of a fictional person \n {format_instruction}",
    input_variables = [],
    partial_variables = {'format_instruction': parser.get_format_instructions()}
)

prompt = template_1.format()

result = model.invoke(prompt)

final_result = parser.parse(result)
print(final_result)
print(type(final_result))