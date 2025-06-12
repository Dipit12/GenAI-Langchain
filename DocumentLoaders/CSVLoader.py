from langchain_community.document_loaders import CSVLoader

loader = CSVLoader("sample_data.csv")

result = loader.load()

# print(result)
for ans in result:
    print(ans)