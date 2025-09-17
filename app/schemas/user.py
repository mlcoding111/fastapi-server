from pydantic import BaseModel, EmailStr, StringConstraints
from typing import Optional, Annotated

UsernameType = Annotated[str, StringConstraints(strip_whitespace=True, pattern=r"^[a-zA-Z0-9_]+$")]

class UserBase(BaseModel):
    name: UsernameType
    email: EmailStr

class UserCreate(UserBase):
    password: Annotated[str, StringConstraints(min_length=8, max_length=100)]

class UserUpdate(BaseModel):
    name: Optional[UsernameType] = None
    email: Optional[EmailStr] = None

class UserPasswordUpdate(BaseModel):
    current_password: Annotated[str, StringConstraints(min_length=8, max_length=100)]
    new_password: Annotated[str, StringConstraints(min_length=8, max_length=100)]

class UserOut(UserBase):
    disabled: bool = False

    class Config:
        orm_mode = True