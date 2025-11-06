from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from utils import database
from schemas.blog import BlogResponse, BlogRequest
from repository import blog as blog_repository

router = APIRouter(
    tags=["Blogs"],
    prefix="/blogs"
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=BlogResponse)
def create_blog(
    request_body: BlogRequest,
    db: Session = Depends(database.get_db)
):
    return blog_repository.create(request_body, db)
