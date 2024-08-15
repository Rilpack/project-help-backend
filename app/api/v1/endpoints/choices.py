from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Annotated

from app.api.v1.endpoints import schemas, crud
from app.db.datebase import get_db

router = APIRouter()


@router.get("/choices/{question_id}", response_model=list[schemas.ChoiceBase])
async def read_choices(question_id: int, db: Annotated[Session, Depends(get_db)]):
    result = crud.get_choices(db, question_id)
    if not result:
        raise HTTPException(status_code=404, detail="Choices not found")
    return result
