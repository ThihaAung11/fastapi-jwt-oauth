from sqlalchemy.orm import sessionmaker, Session
 
from app.core.config import settings
from app.core.schemas import UserCreate
from app.infrastructure import crud
from app.infrastructure.models import User



def create_superuser(db: Session):
    user = db.query(User).filter(User.username == settings.SUPERUSER_NAME).first()
    if not user:
        user_in = UserCreate(
            username=settings.SUPERUSER_NAME,
            password=settings.SUPERUSER_PASS,
            email=settings.SUPERUSER_EMAIL,
            is_superuser=True,
        )
        try:
            user = crud.create_user(db=db, userCreate=user_in)
            if user:
                print("Created User Successfully", user.username)
        except Exception as e:
            print("Error >> ", e)    
        
if __name__ == "__main__":
    from app.core.db import SessionLocal
    session = SessionLocal()
    create_superuser(session)