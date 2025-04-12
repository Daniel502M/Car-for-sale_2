from pydantic import BaseModel, EmailStr


class UserFavoriteCars(BaseModel):
    post_id: int
