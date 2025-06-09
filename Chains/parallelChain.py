from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model_1 =GoogleGenerativeAI(model = "gemini-2.0-flash")

model_2 = ChatGroq(model="llama-3.3-70b-versatile")

parser = StrOutputParser()

prompt_1 = PromptTemplate.from_template("Generate simple and short notes based on this data : {data}")

prompt_2 = PromptTemplate.from_template("Generate quiz questions and answers based on the following text: {data}")

data = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64


"""

prompt_3 = PromptTemplate.from_template("Merge the provided notes and quiz into a single document \n notes => {notes} \n quiz -> {quiz}")

parallel_chain = RunnableParallel({
    'notes': prompt_1 | model_1 | parser,
    'quiz': prompt_2 | model_2 | parser
})

merge_chain = prompt_3 | model_1 | parser

chain = parallel_chain | merge_chain

result = chain.invoke({'data':data})

print(result)

chain.get_graph().print_ascii()