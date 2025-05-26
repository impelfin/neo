import os
from llama_index.readers import YoutubeTranscriptReader
from llama_index import GPTVectorStoreIndex, ServiceContext, LLMPredictor, LangchainEmbedding
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings
from llama_index import Document

# YoutubeTranscriptReader 초기화
loader = YoutubeTranscriptReader()

# YouTube 동영상에서 문서 로드
documents = loader.load_data(ytlinks=["https://www.youtube.com/watch?v=oc6RV5c1yd0"])
print('-' * 50)
print("Documents loaded successfully")
print(f"Loaded documents: {documents}")

# 임베딩 모델 준비
embed_model = LangchainEmbedding(HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
))
print('-' * 50)
print("Embedding model initialized successfully")

# LLMPredictor 준비
llm_predictor = LLMPredictor(llm=ChatOpenAI(
    temperature=0,  # 온도
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
index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)
print('-' * 50)
print("Index created successfully")

# 쿼리 엔진 생성
query_engine = index.as_query_engine()
print('-' * 50)
print("Query engine created successfully")

query = "이 동영상에서 전하고 싶은 말은 무엇인가요? 한국어로 대답해 주세요."
response = query_engine.query(query)
print('-' * 50)
print(f"Query: {query}", end="\n")
print(f"Response: {response}", end="\n")
print('-' * 50)