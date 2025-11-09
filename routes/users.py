from fastapi import APIRouter, status, Depends
from schemas.user import UserResponse, UserRequest
from sqlalchemy.orm import Session
from utils.database import get_db
from repository import user as user_repository


router = APIRouter()


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(request_body: UserRequest, db: Session = Depends(get_db)):
    return user_repository.create(request_body, db)


@router.get("/{id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_users(id: int, db: Session = Depends(get_db)):
    return user_repository.get(id, db)
