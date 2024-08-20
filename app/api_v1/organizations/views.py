from fastapi import APIRouter, HTTPException, status, Depends

from app.api_v1.organizations import crud, schemas
from app.api_v1.users import schemas as users_schemas
from app.api_v1.users.dependencies import get_current_user
from app.db.datebase import db_dependency

router = APIRouter(tags=["Organizations"])


@router.post("/", response_model=schemas.OrganizationView)
async def create_organization(
    organization: schemas.OrganizationCreate,
    db: db_dependency,
    user: users_schemas.UserBase = Depends(get_current_user),
):
    return crud.create_organization(db, organization, user.id)
