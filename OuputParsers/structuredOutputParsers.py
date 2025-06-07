from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
load_dotenv()

model = GoogleGenerativeAI(model = "gemini-2.0-flash")



schema = [
    ResponseSchema(name = "fact_1", description = "fact 1 about the topic"),
ResponseSchema(name = "fact_2", description = "fact 2 about the topic"),
ResponseSchema(name = "fact_3", description = "fact 3 about the topic"),
ResponseSchema(name = "fact_4", description = "fact 4 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)
template = PromptTemplate(
    template = """Give 4 facts about {topic}.
{format_instruction}""",
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)


prompt = template.invoke({'topic':'black hole'})

result = model.invoke(prompt)

final_result = parser.parse(result)
print(final_result)
