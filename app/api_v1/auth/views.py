from fastapi import APIRouter, Depends, Response

from app.api_v1.auth import utils as auth_utils
from app.db.datebase import db_dependency

from .dependencies import validate_auth_user
from .schemas import UserSchema, TokenInfo

router = APIRouter(tags=["Auth"])


@router.post("/login", response_model=TokenInfo)
async def login(
    response: Response,
    user: UserSchema = Depends(validate_auth_user),
):
    jwt_payload = {
        "sub": user.username,
        "username": user.username,
        "email": user.email,
    }
    token = auth_utils.encode_jwt(
        jwt_payload,
    )
    response.set_cookie(
        key="access_token", value=token, httponly=False, secure=True, expires=3600
    )
    return TokenInfo(access_token=token, token_type="Bearer")


@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie("access_token")
    return {"detail": "Logged out successfully"}
