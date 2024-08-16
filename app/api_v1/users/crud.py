from sqlalchemy.orm import Session

from app.db import models

from app.api_v1.users import schemas


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.Users).filter(models.Users.id == user_id).first()


def create_user(db: Session, user: schemas.UserBase):
    db_user = models.Users(
        username=user.username,
        email=user.email,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
