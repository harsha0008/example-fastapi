from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional, Literal

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class Userout(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    model_config = ConfigDict(from_attributes=True) 

class UserLogin(BaseModel):
    email : EmailStr
    password : str 

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id : int
    created_at: datetime
    owner_id: int
    owner: Userout
    model_config = ConfigDict(from_attributes=True)

class PostOut(BaseModel):
    Post: PostResponse
    votes: int
    model_config = ConfigDict(from_attributes=True)  


class Vote(BaseModel):
    post_id: int
    dir: Literal[0,1]