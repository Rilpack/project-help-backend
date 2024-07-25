from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from . import crud
from .schemas import (
    Organization,
    OrganizationCreate,
    OrganizationUpdate,
    OrganizationUpdatePartial,
)
from .dependencies import organization_by_id

router = APIRouter(tags=["Organizations"])


@router.get("/", response_model=list[Organization])
async def get_organizations(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_organizations(session=session)


@router.post("/", response_model=Organization, status_code=status.HTTP_201_CREATED)
async def create_organization(
    organization_in: OrganizationCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_organization(
        session=session, organization_in=organization_in
    )


@router.get("/{organization_id}/", response_model=Organization)
async def get_organization(organization=Depends(organization_by_id)):
    return organization


@router.put("/{organization_id}/")
async def update_organization(
    organization_in: OrganizationUpdate,
    organization: Organization = Depends(organization_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_organization(
        session=session, organization=organization, organization_update=organization_in
    )


@router.patch("/{organization_id}/")
async def update_organization(
    organization_in: OrganizationUpdatePartial,
    organization: Organization = Depends(organization_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_organization(
        session=session,
        organization=organization,
        organization_update=organization_in,
        partial=True,
    )


@router.delete("/{organization_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_organization(
    organization: Organization = Depends(organization_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_organization(session=session, organization=organization)
