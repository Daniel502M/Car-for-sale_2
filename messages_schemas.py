from pydantic import BaseModel


class MessageSchema(BaseModel):
    post_id: int
    message: str


class MessageUpdateSchema(BaseModel):
    message: str
