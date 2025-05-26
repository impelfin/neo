import os
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, ServiceContext, LLMPredictor, StorageContext, LangchainEmbedding
from llama_index.vector_stores.faiss import FaissVectorStore
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings
import faiss

documents = SimpleDirectoryReader('data').load_data()
print('-' * 50)
print("Documents loaded successfully")

embed_model = LangchainEmbedding(HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2",
))
print('-' * 50)
print('Embedding model initialized successfully')

llm_predictor = LLMPredictor(llm=ChatOpenAI(
    temperature=0, 
    model_name="gpt-3.5-turbo"  # 모델명
))
print('-' * 50)
print('LLM Predictor initialized successfully')

faiss_index = faiss.IndexFlatL2(384)
vector_store = FaissVectorStore(faiss_index)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
service_context = ServiceContext.from_defaults(
    llm_predictor=llm_predictor,
    embed_model=embed_model,
)
print('-' * 50)
print("Faiss Index and Vector Store initialized successfully")

index = GPTVectorStoreIndex.from_documents(
    documents, 
    service_context=service_context,
    storage_context=storage_context,
)
print('-' * 50)
print("Index created successfully")

query_engine = index.as_query_engine()
print('-' * 50)
print("Query Engine initialized successfully")

print('-' * 50)
query = '미코의 소꼽친구 이름은?'
response = query_engine.query(query)
print(f"Query: {query}", end="\n\n")
print(f"Response: {response}", end="\n")
print('-' * 50)
