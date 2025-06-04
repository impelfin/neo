class Message:
    def __init__(self, content: str):
        self.content = content

class UserMessage(Message):
    pass

class AssistantMessage(Message):
    pass