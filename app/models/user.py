from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .base import BaseModel
from ..db import Base

class User(BaseModel):
    __tablename__ = "user"

    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    # def __init__(self, name: str, email: str, password: str):
    #     self.name = name
    #     self.email = email
    #     self.password = password

# Validate the difference between BaseModel and Base
# class User(Base):
#     __tablename__ = "users"
#     name = Column(String, index=True)
#     email = Column(String, unique=True, index=True)
#     password = Column(String)