from pydantic import BaseModel

class User(BaseModel):
    id: int | None = None
    email: str
    password: str
    name: str
    position: str

class UserLogin(BaseModel):
    email: str
    password: str