from pydantic import BaseModel, constr, EmailStr
from typing import Optional

UsernameType = constr(strip_whitespace=True, regex=r"^[a-zA-Z0-9_]+$")

class UserBase(BaseModel):
    name: UsernameType
    email: EmailStr

class UserCreate(UserBase):
    password: constr(min_length=8, max_length=100)
    pass

class UserUpdate(BaseModel):
    name: Optional[UsernameType] = None
    email: Optional[EmailStr] = None

class UserPasswordUpdate(BaseModel):
    current_password: constr(min_length=8, max_length=100)
    new_password: constr(min_length=8, max_length=100)

class UserOut(UserBase):
    disabled: bool = False

    class Config:
        orm_mode = True