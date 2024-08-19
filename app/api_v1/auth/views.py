from fastapi import APIRouter, Depends

import utils as auth_utils

from .dependencies import validate_auth_user
from .schemas import UserSchema, TokenInfo

router = APIRouter(tags=["Auth"])


@router.post("/login", response_model=TokenInfo)
def auth_user_issue_jwt(user: UserSchema = Depends(validate_auth_user)):
    jwt_payload = {
        "sub": user.username,
        "username": user.username,
        "email": user.email,
    }
    token = auth_utils.encode_jwt(
        jwt_payload,
    )
    return TokenInfo(access_token=token, token_type="Bearer")
