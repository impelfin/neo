from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import FewShotPromptTemplate
from langchain.prompts import PromptTemplate

# 답변 예시 준비
examples = [
    {"input": "밝은", "output": "어두운"},
    {"input": "재미있는", "output": "지루한"},
    {"input": "활기찬", "output": "무기력한"},
    {"input": "높은", "output": "낮은"},
    {"input": "빠른", "output": "느린"},
]

# 프롬프트 템플릿 생성
example_prompt = PromptTemplate(
    input_variables=["input","output"],
    template="입력: {input}\n출력: {output}",
)

# SemanticSimilarityExampleSelector 생성
example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples=examples, # 답변 예시
    embeddings=OpenAIEmbeddings(), # 임베디드 생성 클래스
    vectorstore_cls=FAISS, # 임베디드 유사 검색 클래스
    k=3 # 답변 예시 개수
)

# FewShotPromptTemplate 생성
prompt_from_string_examples = FewShotPromptTemplate(
    example_selector=example_selector,  # ExampleSelector
    example_prompt=example_prompt,
    prefix="모든 입력에 대한 반의어를 입력하세요",
    suffix="입력: {adjective}\n출력:",
    input_variables=["adjective"],
    example_separator="\n\n"
)

# 프롬프트 생성
print(prompt_from_string_examples.format(adjective="큰"))
