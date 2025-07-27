from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from src.database.create import Base

class Admins(Base):
    __tablename__ = "admins"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    user = Column(Integer(), ForeignKey("users.id"), unique=True, nullable=False)
    rang = Column(Integer(), default=1)
    users = relationship("Users", back_populates="admins")