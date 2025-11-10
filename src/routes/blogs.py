from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from src.utils import database
from src.utils.auth import verify_access_token
from src.schemas.blog import BlogResponse, BlogRequest
from src.schemas.auth import TokenData
from src.repository import blog as blog_repository

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=BlogResponse)
def create_blog(
    request_body: BlogRequest,
    validate_auth: TokenData = Depends(verify_access_token),
    db: Session = Depends(database.get_db),
):
    return blog_repository.create(request_body, db)


@router.get("/", response_model=list[BlogResponse])
def get_blogs(
    db: Session = Depends(database.get_db),
    validate_auth: TokenData = Depends(verify_access_token),
):
    return blog_repository.get_all(db)


@router.get("/{id}", response_model=BlogResponse, status_code=status.HTTP_200_OK)
def get_blog(
    id: int,
    validate_auth: str = Depends(verify_access_token),
    db: Session = Depends(database.get_db),
):
    return blog_repository.get(id, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(
    id: int,
    db: Session = Depends(database.get_db),
    validate_auth: TokenData = Depends(verify_access_token),
):
    return blog_repository.delete(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(
    id: int,
    updated_blog: BlogRequest,
    db: Session = Depends(database.get_db),
    validate_auth: TokenData = Depends(verify_access_token),
):
    return blog_repository.update(id, updated_blog, db)
