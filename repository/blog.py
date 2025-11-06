from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from schemas.blog import BlogRequest
from models.blog import Blogs


def create(request_body: BlogRequest, db: Session):
    new_blog = Blogs(**request_body.dict())

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
