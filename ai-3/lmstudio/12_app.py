import lmstudio as lms
from create_file_tool import create_file

model = lms.llm()
model.act(
    "Please create a filename output.txt with your understanding of meaning of life.",
    [create_file],
    # on_message = print
)

print("File Created.")
