from sqlalchemy import Boolean, Integer, String, Column, ForeignKey, DateTime
from app.db.datebase import Base
import datetime


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, nullable=False)
    email = Column(String, index=True, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.datetime.now())
