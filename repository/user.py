from schemas.user import UserRequest
from models.user import Users
from sqlalchemy.orm import Session
from utils.hash import get_password_hash


def create(request_body: UserRequest, db: Session):
    hashed_pwd = get_password_hash(request_body.password)
    new_user = Users(
        name=request_body.name,
        email=request_body.email,
        password=hashed_pwd
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
