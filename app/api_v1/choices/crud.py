from sqlalchemy.orm import Session

from app.db import models


def get_choices(db: Session, question_id: int):
    return (
        db.query(models.Choices).filter(models.Choices.question_id == question_id).all()
    )
