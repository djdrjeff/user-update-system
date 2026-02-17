from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(Text)
    email = Column(Text, unique=True, index=True, nullable=False)
    phone = Column(Text)
    organization = Column(Text)
    last_updated = Column(DateTime, server_default=func.now())
