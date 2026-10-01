from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from auth.auth_service import create_user, login_user
from schemas.user_schema import (
    UserRegister,
    UserResponse,
    UserLogin,
    TokenResponse,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):
    new_user = create_user(user, db)

    if new_user is None:
        raise HTTPException(
            status_code=400,
            detail="Email already registered."
        )

    return new_user


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    token = login_user(user, db)

    if token is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password."
        )

    return token