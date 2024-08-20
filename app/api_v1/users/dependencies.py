from fastapi import Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt.exceptions import InvalidTokenError

from app.api_v1.users import schemas
from app.api_v1.auth import utils as auth_utils
from app.db import models
from app.db.datebase import get_db

http_bearer = HTTPBearer()


def get_current_token_payload(
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
) -> schemas.UserBase:
    token = request.cookies.get("access_token")
    if not token:
        token = credentials.credentials
        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Token not found"
            )

    try:
        payload = auth_utils.decode_jwt(token=token)
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid token error"
        )
    return payload


def get_current_auth_user(
    db: Session = Depends(get_db),
    payload: dict = Depends(get_current_token_payload),
) -> schemas.UserBase:
    username: str | None = payload.get("sub")
    user = db.query(models.Users).filter(models.Users.username == username).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found"
        )
    return user


def get_current_user(
    user: schemas.UserBase = Depends(get_current_auth_user),
):
    return user
