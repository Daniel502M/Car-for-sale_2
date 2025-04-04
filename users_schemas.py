from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserUpdateSchema(BaseModel):
    name: str
    password: str