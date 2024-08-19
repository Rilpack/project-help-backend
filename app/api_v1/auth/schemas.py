from pydantic import BaseModel, ConfigDict, EmailStr


class UserSchema(BaseModel):
    model_config = ConfigDict(strict=True)

    username: str
    password: str
    email: EmailStr | None = None


class TokenInfo(BaseModel):
    access_token: str
    token_type: str
