from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import Relationship
from utils.database import Base


class Blogs(Base):
    __tablename__ = "blogs"

    id = Column(Integer, index=True, primary_key=True)
    title = Column(String)
    body = Column(String)
