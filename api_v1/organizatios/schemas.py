from pydantic import BaseModel, ConfigDict


class OrganizationBase(BaseModel):
    name: str
    description: str
    total: int


class OrganizationCreate(OrganizationBase):
    pass


class OrganizationUpdate(OrganizationCreate):
    pass


class OrganizationUpdatePartial(OrganizationCreate):
    name: str | None = None
    description: str | None = None
    total: int | None = None


class Organization(OrganizationBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
