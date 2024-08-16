from fastapi import APIRouter, HTTPException, status

from app.api_v1.choices import crud, schemas
from app.db.datebase import db_dependency

router = APIRouter(tags=["Choices"])


@router.get("/{question_id}", response_model=list[schemas.ChoiceBase])
async def read_choices(question_id: int, db: db_dependency):
    result = crud.get_choices(db, question_id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Choices not found"
        )
    return result
