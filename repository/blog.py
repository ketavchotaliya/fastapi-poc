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


def get_all(db: Session):
    blogs = db.query(Blogs).all()
    return blogs


def get(id: int, db: Session):
    blog = db.query(Blogs).filter(Blogs.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"success": False, "message": "Blog not found."}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail={"success": False, "message": "Blog not found."})

    return blog


def delete(id: int, db: Session):
    blog = db.query(Blogs).filter(Blogs.id == id).first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail={"success": False, "message": "Blog not found."})
    db.delete(blog)
    db.commit()
    return {"details": blog, "message": "Blog has been deleted."}


def update(id: int, request_body: BlogRequest, db: Session):
    blog = db.query(Blogs).filter(Blogs.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
                            "success": False, "message": "Blog not found."})

    for key, value in request_body.dict().items():
        setattr(blog, key, value)
    db.commit()
    db.refresh(blog)
    return {"details": blog, "message": "Blog has been updated successfully."}
