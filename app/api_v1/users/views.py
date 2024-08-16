from fastapi import APIRouter, HTTPException, status

from app.api_v1.users import crud, schemas
from app.db.datebase import db_dependency

router = APIRouter(tags=["Users"])


@router.post("/", response_model=schemas.UserBaseView)
async def create_users(db: db_dependency, user: schemas.UserBase):
    return crud.create_user(db, user)


@router.get("/{user_id}", response_model=schemas.UserBaseView)
async def get_user(db: db_dependency, user_id: int):
    result = crud.get_user_by_id(db, user_id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user is not found"
        )
    return result
