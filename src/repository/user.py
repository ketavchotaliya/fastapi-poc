from fastapi import HTTPException, status
from src.schemas.user import UserRequest
from src.models.user import Users
from sqlalchemy.orm import Session
from src.utils.hash import get_password_hash


def create(request_body: UserRequest, db: Session):
    hashed_pwd = get_password_hash(request_body.password)
    new_user = Users(
        name=request_body.name, email=request_body.email, password=hashed_pwd
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get(id: int, db: Session):
    user = db.query(Users).filter(Users.id == id).first()
    if not user:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"success": False, "message": "Blog not found."}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"success": False, "message": "User not found."},
        )

    return user
