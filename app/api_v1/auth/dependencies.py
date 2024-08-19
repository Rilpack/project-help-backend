from fastapi import Form, HTTPException, status
from sqlalchemy.orm import Session

from app.db import models

import utils as auth_utils


def validate_auth_user(
    db: Session,
    username: str = Form(),
    password: str = Form(),
):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
    )
    if not (user := models.Users.username):
        raise unauthed_exc

    if not auth_utils.validate_password(password, hashed_password=user):
        raise unauthed_exc

    if not user.active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User inactive",
        )
    return user
