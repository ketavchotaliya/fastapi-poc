from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from src.models.user import Users
from src.utils.database import get_db
from src.utils.hash import verify_password
from src.utils.auth import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(tags=["Auth"])


@router.post("/login")
def login(
    request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = db.query(Users).filter(Users.email == request.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"success": False, "message": "Invalid Credentials."},
        )

    if not verify_password(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"success": False, "message": "Invalid Credentials."},
        )
    # generate jwt token
    auth_token = create_access_token(
        data={"sub": user.email},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    return {"auth_token": auth_token, "token_type": "Bearer"}
