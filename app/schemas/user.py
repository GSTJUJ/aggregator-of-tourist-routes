from pydantic import BaseModel


class UserCreate(BaseModel):
    full_name: str
    phone: str
    email: str
    region: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserUpdate(BaseModel):
    full_name: str
    phone: str
    email: str
    region: str
