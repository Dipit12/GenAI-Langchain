from langchain_huggingface import HuggingFaceEmbeddings
import numpy as np

embedding = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

text1 = "Virat kohli is the best batsman in this world"
text2 = "Virat kohli is a good human being"
text3 = "HI there whats up"

vector1 = embedding.embed_query(text1);
vector2 = embedding.embed_query(text2);
vector3 = embedding.embed_query(text3);

def cosine_similarity(vec1,vec2):
    dot_product = np.dot(vec1,vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    return dot_product / (norm_vec1 * norm_vec2)

similarity1 = cosine_similarity(vector1,vector2)
similarity2 = cosine_similarity(vector1, vector3)

print(similarity1)
print(similarity2)