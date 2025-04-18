import uuid
from sqlalchemy import Column, String, INT
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(String(120), primary_key=True, default=lambda: str(uuid.uuid4()))
    nickname = Column(String(120), unique=False, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    phone = Column(String(120), unique=True, nullable=True)
    description = Column(String(120), nullable=True)
