from langchain.memory import ConversationTokenBufferMemory
from langchain.chat_models import ChatOpenAI

memory = ConversationTokenBufferMemory(
    llm = ChatOpenAI(
        model = "gpt-3.5-turbo",
        temperature = 0
    ),
    max_token_limit = 50,
    return_messages = True
)

memory.save_context({"input": "안녕"}, {"output": "어디 가서 밥 먹을까?"})
memory.save_context({"input": "라면 먹으러 가자"}, {"output": "지하철역 앞에 있는 분식집으로 가자."})
memory.save_context({"input": "그럼 출발"}, {"output": "OK!!"})

print(memory.load_memory_variables({}))
