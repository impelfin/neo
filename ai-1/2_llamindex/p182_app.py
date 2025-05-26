from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext
from langchain.chat_models import ChatOpenAI

documents = SimpleDirectoryReader('data').load_data()
print('-' * 50)
print('Documents : ', documents)

llm_predictor = LLMPredictor(llm=ChatOpenAI(
    temperature=0, 
    model_name="gpt-3.5-turbo"
))

ServiceContext = ServiceContext.from_defaults(
    llm_predictor=llm_predictor,
)

index = GPTVectorStoreIndex.from_documents(
    documents, 
    service_context=ServiceContext,
)

query_engine = index.as_query_engine()
print('-' * 50)
print('query : ', query_engine.query("미코의 성격은?"))
print('-' * 50)