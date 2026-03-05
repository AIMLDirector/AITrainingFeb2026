from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('google/functiongemma-270m-it')
embeddings = model.encode(sentences)

print(embeddings)
