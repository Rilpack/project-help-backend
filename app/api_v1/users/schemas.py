from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime


class UserBase(BaseModel):
    model_config = ConfigDict(strict=True)
    id: int
    username: str
    password: str
    email: EmailStr | None = None


class UserBaseView(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True
