import ollama

response = ollama.chat(
    model = 'llama3.2:latest',
    messages = [
        {'role': 'system', 'content': 'You are a python expert. '},
        {'role': 'user', 'content': 'Code a Python function to generate a Fibonacci sequence.'}
    ]
)

print(response['message']['content'])