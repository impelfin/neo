from llama_index import download_loader, GPTVectorStoreIndex, ServiceContext, LLMPredictor, LangchainEmbedding
from llama_index.readers import BeautifulSoupWebReader
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings
from llama_index import Document

# BeautifulSoupWebReader 초기화
loader = BeautifulSoupWebReader()

# URL에서 문서 로드
documents = loader.load_data(urls=["https://openai.com/blog/planning-for-agi-and-beyond"])
print('-' * 50)
print("Documents loaded successfully")
print(f"Loaded documents: {documents}")

# Document 객체 생성
document_objects = [Document(text=doc.text) for doc in documents]

# 임베딩 모델 준비
embed_model = LangchainEmbedding(HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
))
print('-' * 50)
print("Embedding model initialized successfully")

# LLMPredictor 준비
llm_predictor = LLMPredictor(llm=ChatOpenAI(
    temperature=0, 
    model_name="gpt-3.5-turbo"  # 모델명
))
print('-' * 50)
print("LLMPredictor initialized successfully")

# ServiceContext 준비
service_context = ServiceContext.from_defaults(
    embed_model=embed_model,
    llm_predictor=llm_predictor
)
print('-' * 50)
print("ServiceContext created successfully")

# 인덱스 생성
index = GPTVectorStoreIndex.from_documents(document_objects, service_context=service_context)
print('-' * 50)
print("Index created successfully")

# 쿼리 엔진 생성
query_engine = index.as_query_engine()
print('-' * 50)
print("Query engine created successfully")

# 질의응답
query="이 웹페이지에서 전하고 싶은 말은 무엇인가요? 한국어로 대답해 주세요."
response = query_engine.query(query)
print('-' * 50)
print(f"Query: {query}", end="\n")
print(f"Response: {response}", end="\n")
print('-' * 50)
