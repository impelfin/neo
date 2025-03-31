from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import requests
import json
from typing import Union
from typing import Optional

app = FastAPI()

base_url = 'http://192.168.1.34:5000/users'

@app.get(path='/')
async def healthCheck():
    return "OK"

@app.get(path='/users')
async def getUsers():
    response = requests.get(base_url)
    return response.json()

@app.get(path='/users')
async def postUsers(id:str, name: str):
    data = dict(id=id, name=name)
    response = requests.get(base_url, json=data)
    return response.json()

@app.get(path='/users/params1')
async def user_params(id:Union[str, None] = None, name:Union[str, None] = None):
    if (id is None) and (name is None):
        return "id, name을 입력하세요."
    else:
        if id is None:
            params = '?name=' + name
        elif name is None:
            params = '?id=' + id
        else:
            params = '?id=' + id
            params += '&name=' + name
    url = base_url + params
    response = requests.get(base_url)
    return response.json()

@app.get(path='/users/params2')
async def user_params(id:Optional[str] = None, name:Optional[str] = None):
    if (id is None) and (name is None):
        return "id, name을 입력하세요."
    else:
        if id is None:
            params = '?name=' + name
        elif name is None:
            params = '?id=' + id
        else:
            params = '?id=' + id
            params += '&name=' + name
    url = base_url + params
    response = requests.get(base_url)
    return response.json()

