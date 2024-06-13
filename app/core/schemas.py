from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str | None


class UserCreate(UserBase):
    password: str
    is_superuser: bool
    created_by: str = 'system'


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None

class TokenPayload(BaseModel):
    sub: int | None = None