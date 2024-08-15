from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Annotated

from app.api.v1.endpoints import schemas, crud
from app.db.datebase import get_db, db_dependency

router = APIRouter()


@router.get("/questions/{question_id}")
async def read_question(question_id: int, db: db_dependency):
    result = crud.get_question(db, question_id)
    if not result:
        raise HTTPException(status_code=404, detail="Question not found")
    return result


@router.post("/questions/")
async def create_question(question: schemas.QuestionBase, db: db_dependency):
    return crud.create_question(db, question)
