from sqlalchemy.orm import Session
from app.db import models
from app.api_v1.organizations import schemas


def create_organization(
    db: Session, organization: schemas.OrganizationCreate, user_id: int
):
    db_organization = models.Organizations(
        name=organization.name, description=organization.description, user_id=user_id
    )
    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)
    return db_organization
