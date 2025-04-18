import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import PlainTextResponse, JSONResponse
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import uuid
from database import db_conn
from models import User

app = FastAPI()

db = db_conn()
session = db.sessionmaker()

class RequestUserDto(BaseModel):
    id:str=Field(title="사용자 구분 ID", pattern="^[a-z]{1}[0-9a-z]{7}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$")
    nickname:str=Field(title="사용자 닉네임")
    email:EmailStr=Field(title="사용자 이메일 주소")
    phone:str=Field(title="사용자 휴대폰 번호", pattern="^010-([0-9]{4})-([0-9]{4})$")
    description:Optional[str]=Field(title="사용자 소개")

class ResponseUserDto(BaseModel):
    id:str=Field(title="사용자 구분 ID")
    email:EmailStr=Field(title="사용자 이메일 주소")
    
    class Config:
        json_schema_extra={
            "example": {
                "id": uuid.uuid4(),
                "email": "watson@buzzni.com",
            }
        }
        # orm_mode = True

@app.get(
    path='/', description="healthcheck용 포인트입니다.",
    status_code=status.HTTP_200_OK,
    response_class=PlainTextResponse,
    responses={200:{"description" : "Health check 응답"}}
)
async def health_check():
    return "OK"

@app.post (
    path='/registerReq', description="회원가입 API입니다.", status_code=201,
    response_class=JSONResponse,
    responses={
        201: {
            "description":"가입 사용자 정보",
            "content": {
                "application/json": {
                    "example": {
                        "nickname": "왓슨",
                        "email": "watson@buzzni.com",
                        "phone": "010-1234-5678",
                        "description":"버즈니 왓슨입니다."
                    }
                }
            }
        }
    }
)
async def register_req_user(req: RequestUserDto):
    return req.dict()

@app.post (
    path='/registerRes', description="회원가입 API입니다.", status_code=201,
    response_model=ResponseUserDto,
    responses={
        201: {
            "description":"가입 사용자 정보",
        }
    }
)
async def register_res_user(req: ResponseUserDto):
    return req.dict()

@app.post (
    path='/register', description="회원가입 API입니다.", status_code=201,
    response_model=ResponseUserDto,
    responses={201:{"description":"가입 사용자 정보"}}
)
async def register_user(req: RequestUserDto):
    user = User(**req.dict())
    session.add(user)
    session.commit()
    # return RequestUserDto(**req.dict())
    return RequestUserDto(**req.dict())

if __name__ == "__main__":
    uvicorn.run (app, host="0.0.0.0", port=3000)