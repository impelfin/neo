from sqlalchemy import Column, TEXT, INT
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class St_info(Base):
    __tablename__ = 'st_info'
    
    ST_ID = Column(INT, primary_key=True, nullable=False)
    NAME = Column(TEXT, nullable=False)
    DEPT = Column(TEXT, nullable=False)
    
class St_grade(Base):
    __tablename__ = 'st_grade'
    
    ST_ID = Column(INT, primary_key=True, nullable=False)
    Linux = Column(TEXT, nullable=False)
    DB = Column(TEXT, nullable=False)
