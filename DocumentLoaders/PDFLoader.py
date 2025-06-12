from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("concept2_details.pdf")

result = loader.load()

pages = []

for page in loader.lazy_load():
    pages.append(page)

print(pages[0].page_content)

print(pages[1].page_content)

print(pages[2].page_content)

print(len(result))