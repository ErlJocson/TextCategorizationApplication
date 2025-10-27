from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    user_id: str
    date_created: datetime

    class Config:
        from_attributes = True

class UserUpdate(UserBase):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[str] = None
    password: Optional[str]

    class Congif:
        from_attributes = True

