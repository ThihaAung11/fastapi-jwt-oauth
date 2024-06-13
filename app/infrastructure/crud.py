from sqlalchemy.orm import Session
from app.infrastructure.models import User
from app.core import schemas
from app.core.utils import authentication_utils

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, userCreate: schemas.UserCreate)-> User:
    # hashpassword
    hashed_password = authentication_utils.get_password_hash(userCreate.password)
    new_user = User(
        username = userCreate.username,
        hashed_password = hashed_password,
        is_superuser = userCreate.is_superuser, 
        email = userCreate.email,
        created_by = userCreate.created_by,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user