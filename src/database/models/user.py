from sqlalchemy import Integer, String, Column, BigInteger
from sqlalchemy.orm import relationship
from src.database.create import Base

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    tg_id = Column(BigInteger(), unique=True)
    total = Column(Integer(), default=0)
    username = Column(String(length=50))
    admins = relationship("Admins", back_populates="users")