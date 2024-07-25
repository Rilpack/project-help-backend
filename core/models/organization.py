from sqlalchemy.orm import Mapped

from .base import Base


class Organization(Base):
    __tablename__ = "organizations"

    name: Mapped[str]
    description: Mapped[str]
    total: Mapped[int]
