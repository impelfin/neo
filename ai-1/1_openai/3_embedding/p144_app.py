import openai 
import numpy as np
import faiss

in_text = "오늘은 비가 오지 않아 다행이다."

response = openai.Embedding.create(
    input=in_text,
    model="text-embedding-ada-002"
)
in_embeds = [record["embedding"] for record in response["data"]]
in_embeds = np.array(in_embeds).astype("float32")

target_texts = [
    "좋아하는 음식은 무엇인가요?",
    "어디에 살고 계신가요?",
    "아침 지하철은 혼잡해요.",
    "오늘은 날씨가 좋네요!",
    "요즘 경기가 좋지 않네요."
]

response = openai.Embedding.create(
    input=target_texts,
    model="text-embedding-ada-002"
)
target_embeds = [record["embedding"] for record in response["data"]]
target_embeds = np.array(target_embeds).astype("float32")

index = faiss.IndexFlatL2(1536)
index.add(target_embeds)

D, I = index.search(in_embeds, 1)
print(D)
print(I)
print(target_texts[I[0][0]])
