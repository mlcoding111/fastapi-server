from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .base import BaseModel

class User(BaseModel):
    __tablename__ = "user"

    name: Mapped[str] = mapped_column(String, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    password: Mapped[str] = mapped_column(String)
