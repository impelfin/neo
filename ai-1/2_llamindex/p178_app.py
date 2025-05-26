from llama_index import SimpleDirectoryReader

documents = SimpleDirectoryReader('data').load_data()
print('-' * 50)
print("documents : ", documents)
print('-' * 50)
