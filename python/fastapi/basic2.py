from fastapi import FastAPI
from pydantic import BaseModel

class HelloWorldRequest(BaseModel):
    name : str
    age : int

app = FastAPI()

@app.get('/')
async def HealthCheck():
    return {"status": "ok"}

@app.get(path='/hello')
async def Hello_with_querystring(name:str):
        return "Hello with name. your name is " + name

@app.get(path='/hello/{name}')
async def Hello_with_name(name: str):
    return "Hello with name. your name is " + name

@app.post(path='hello/post')
async def Hello_post(request: HelloWorldRequest):
    return "Hello with post. your name is {} and your age is {}".format(request.name, request.age)

    

