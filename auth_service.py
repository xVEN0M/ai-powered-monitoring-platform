from sqlalchemy.orm import Session

from auth.hashing import verify_password
from auth.jwt_handler import create_access_token
from schemas.user_schema import UserLogin

from models.user import User
from schemas.user_schema import UserRegister
from auth.hashing import hash_password


def create_user(user: UserRegister, db: Session):
    # Check if email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        return None

    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
def login_user(user: UserLogin, db: Session):
    """
    Authenticate a user and return a JWT token.
    """

    db_user = db.query(User).filter(User.email == user.email).first()

    if db_user is None:
        return None

    if not verify_password(user.password, db_user.password):
        return None

    token = create_access_token(
        {
            "sub": db_user.email,
            "user_id": db_user.id,
            "username": db_user.username
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }