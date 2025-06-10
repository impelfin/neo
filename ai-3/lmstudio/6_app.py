from lmstudio import BaseModel
import lmstudio as lms

class BookSchema(BaseModel):
    title: str
    author: str
    year: str

model = lms.llm()

result = model.respond(
    "Tell me about the Hobbit",
    response_format = BookSchema
)

book = result.parsed

print(book)
