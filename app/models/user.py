from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from .base import BaseModel

class User(BaseModel):
    __tablename__ = "user"

    full_name: Mapped[str] = mapped_column(String, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    google_id: Mapped[str] = mapped_column(String, unique=True, index=True)
    profile_picture: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
