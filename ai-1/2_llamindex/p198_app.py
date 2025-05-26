import os
import pinecone
from pinecone import Pinecone, ServerlessSpec
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, ServiceContext, LLMPredictor, StorageContext
from llama_index.vector_stores.pinecone import PineconeVectorStore
from langchain.chat_models import ChatOpenAI

api_key = os.environ.get('PINECONE_API_KEY')

if api_key is None:
    raise ValueError(
        "PINECONE_API_KEY environment variable not set")

pinecone = Pinecone(api_key=api_key)
documents = SimpleDirectoryReader('data').load_data()
print('-' * 50)
print('Documents loaded successfully')

index_name = 'quickstart'

if index_name not in pinecone.list_indexes().names():
    pinecone.create_index(
        name=index_name,
        dimension=1536,
        metric="euclidean",
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1',
        )
    )

pinecone_index = pinecone.Index(index_name)
print('-' * 50)
print('Pinecone index created successfully')

llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo"))
print('-' * 50)
print('LLM Predictor created successfully')

service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
print('-' * 50)
print('Service Context created successfully')

vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
print('-' * 50)
print('Storage Context created successfully')

index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context, storage_context=storage_context)
print('-' * 50)
print('Index created successfully')

query_engine = index.as_query_engine()
print('-' * 50)
print('Query Engine created successfully')

query = "미코의 소꿉친구 이름은?"
response = query_engine.query(query)
print('-' * 50)
print(f"Query: {query}", end="\n\n")
print(f"Response: {response}", end="\n\n")
print('-' * 50)
