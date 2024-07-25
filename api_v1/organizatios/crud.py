from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Organization
from .schemas import OrganizationCreate, OrganizationUpdate, OrganizationUpdatePartial


async def get_organizations(session: AsyncSession) -> list[Organization]:
    smtm = select(Organization).order_by(Organization.id)
    result: Result = await session.execute(smtm)
    organization = result.scalars().all()
    return list(organization)


async def get_organization(
    session: AsyncSession, organizations_id: int
) -> Organization | None:
    return await session.get(Organization, organizations_id)


async def create_organization(
    session: AsyncSession, organization_in: OrganizationCreate
) -> Organization:
    organization = Organization(**organization_in.model_dump())
    session.add(organization)
    await session.commit()
    await session.refresh(organization)
    return organization


async def update_organization(
    session: AsyncSession,
    organization: Organization,
    organization_update: OrganizationUpdate | OrganizationUpdatePartial,
    partial: bool = False,
) -> Organization:
    for name, value in organization_update.model_dump(exclude_unset=partial).items():
        setattr(organization, name, value)
    await session.commit()
    return organization


async def delete_organization(
    session: AsyncSession,
    organization: Organization,
) -> None:
    await session.delete(organization)
    await session.commit()
