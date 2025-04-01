from fastapi import FastAPI, HTTPException 
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

@app.post(path='/users')
async def postUsers(id:str, name: str):
    data = dict(id=id, name=name)
    response = requests.post(base_url, json=data)
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
    response = requests.get(url)
    return response.json()

@app.get(path='/users/params2')
async def user_params(id:Optional[str]=None, name:Optional[str]=None):
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
    response = requests.get(url)
    return response.json()

@app.get(path='/users/data')
async def users_data(id:Optional[str]=None, name:Optional[str]=None):
    if (id is None) and (name is None):
        return "id, name을 입력하세요."
    else:
        if id is None:
            data = dict(name=name)
        elif name is None:
            data = dict(id=id)
        else:
            data = dict(id=id, name=name)
    response = requests.get(base_url, data)
    return jsonable_encoder(response.json())

# reqeust param
@app.get(path="/users/{id}")
async def users_param(id: str):
    try:
        url = base_url + '/' + id
        response = requests.get(url)
        response.raise_for_status()

        try:
            data = response.json()
        except ValueError: 
            raise HTTPException(status_code=500, detail="Invalid JSON response from server")

        if not data:
            return {"message": "User Not Found", "data": None}

        return data

    except requests.exceptions.RequestException:
        raise HTTPException(status_code=500, detail="Request failed")
    
# put - resource entire update
@app.get(path="/put/{id}")
async def putData(id: str, name:str):
    url = base_url + '/' + id
    data = dict(id=id,name=name)
    response = requests.put(url, json=data)
    return response.json()

# patch - resource partial update
@app.get(path="/patch/{id}")
async def patchData(id: str, name:str):
    url = base_url + '/' + id
    data = dict(name=name)
    response = requests.patch(url, json=data)
    return response.json()

# delete - resource delete
@app.get(path="/delete/{id}")
async def deleteData(id: str):
    url = base_url + '/' + id
    data = dict(id=id)
    response = requests.delete(url, json=data)
    response = requests.get(base_url)
    return response.json()
