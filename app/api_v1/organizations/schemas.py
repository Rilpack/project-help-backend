from pydantic import BaseModel


class OrganizationBase(BaseModel):
    name: str
    description: str


class OrganizationCreate(OrganizationBase):
    pass


class OrganizationView(OrganizationBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
