from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import Relationship
from utils.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, index=True, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = Relationship("Blogs", back_populates="creator")
