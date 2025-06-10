import lmstudio as lms

model = lms.embedding_model('nomic-embed-text-v1.5')

embedding = model.embed('Hello World!')
print(embedding)
