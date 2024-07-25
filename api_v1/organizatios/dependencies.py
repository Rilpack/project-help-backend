from typing import Annotated

from core.models import db_helper, Organization
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud


async def organization_by_id(
    organization_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Organization:
    organization = await crud.get_organization(
        session=session, organizations_id=organization_id
    )
    if organization is not None:
        return organization

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {organization_id} not found",
    )
