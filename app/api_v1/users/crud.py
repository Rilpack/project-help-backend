from sqlalchemy.orm import Session

from app.db import models
from app.api_v1.auth import utils as auth_utils
from app.api_v1.users import schemas


def create_user(db: Session, user_data: schemas.UserBase):
    hashed_password = auth_utils.hash_password(user_data.password)
    user = models.Users(
        username=user_data.username,
        email=user_data.email,
        password=hashed_password,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
