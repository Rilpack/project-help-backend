from fastapi import Form, HTTPException, status, Depends
from sqlalchemy.orm import Session

from app.db import models
from app.api_v1.auth import utils as auth_utils
from app.db.datebase import get_db


def validate_auth_user(
    db: Session = Depends(get_db),
    username: str = Form(...),
    password: str = Form(...),
):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
    )

    user = db.query(models.Users).filter(models.Users.username == username).first()
    if not user:
        raise unauthed_exc

    if not auth_utils.validate_password(password, hashed_password=user.password):
        raise unauthed_exc

    return user
