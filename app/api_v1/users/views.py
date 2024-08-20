from fastapi import APIRouter, HTTPException, status, Depends

from app.api_v1.users import crud, schemas
from app.api_v1.users.dependencies import get_current_user, get_current_token_payload
from app.db.datebase import db_dependency

router = APIRouter(tags=["Users"])


@router.post("/", response_model=schemas.UserBaseView)
async def create_users(db: db_dependency, user: schemas.UserBase):
    return crud.create_user(db, user)


@router.get("/me", response_model=schemas.UserBaseView)
async def auth_user_check_self_info(
    payload: dict = Depends(get_current_token_payload),
    user: schemas.UserBaseView = Depends(get_current_user),
):
    iat = payload.get("iat")
    return user
