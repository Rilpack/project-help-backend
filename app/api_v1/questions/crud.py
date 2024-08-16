from sqlalchemy.orm import Session

from app.api_v1.questions import schemas
from app.db import models


def get_question(db: Session, question_id: int):
    return db.query(models.Questions).filter(models.Questions.id == question_id).first()


def create_question(db: Session, question: schemas.QuestionBase):
    db_question = models.Questions(question_text=question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    for choice in question.choices:
        db_choice = models.Choices(
            choice_text=choice.choice_text,
            is_correct=choice.is_correct,
            question_id=db_question.id,
        )
        db.add(db_choice)
    db.commit()
    return db_question
