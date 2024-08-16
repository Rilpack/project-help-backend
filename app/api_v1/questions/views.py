from fastapi import APIRouter, HTTPException

from app.api_v1.questions import crud
from app.api_v1.questions import schemas
from app.db.datebase import db_dependency

router = APIRouter(tags=["Questions"])


@router.post("/")
async def create_question(question: schemas.QuestionBase, db: db_dependency):
    return crud.create_question(db, question)


@router.get("/{question_id}")
async def read_question(question_id: int, db: db_dependency):
    result = crud.get_question(db, question_id)
    if not result:
        raise HTTPException(status_code=404, detail="Question not found")
    return result
