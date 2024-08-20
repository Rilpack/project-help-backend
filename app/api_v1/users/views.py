from fastapi import APIRouter, Depends, Request

from app.api_v1.users import crud, schemas
from app.api_v1.users.dependencies import get_current_user, get_current_token_payload
from app.db.datebase import db_dependency

router = APIRouter(tags=["Users"])


@router.post("/", response_model=schemas.UserBaseView)
async def create_users(db: db_dependency, user: schemas.UserBase):
    return crud.create_user(db, user)


@router.get("/get_me", response_model=schemas.UserBaseView)
async def get_info_me(
    request: Request,
    user: schemas.UserBaseView = Depends(get_current_user),
):
    return user
