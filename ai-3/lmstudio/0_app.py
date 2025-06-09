from openai import OpenAI

LM_STUDIO_SERVER_URL = "http://192.168.1.3:1234/v1" 

client = OpenAI(base_url=LM_STUDIO_SERVER_URL, api_key="lm-studio")

model_name = "llama3.2" 

try:
    completion = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": "What is the meaning of life?"}
        ],
        temperature=0.7,
        max_tokens=150,  
    )

    print(completion.choices[0].message.content)

except Exception as e:
    print(f"An error occurred: {e}")
    print("Please ensure LM Studio server is running, accessible at the specified URL, and a model is loaded.")