import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase
from sqlalchemy.sql import func

from datetime import datetime, timezone
# from app.core.db import Base

class Base(DeclarativeBase):
    metadata = sa.MetaData()


class CommonBase(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    created_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by = Column(String(50), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=True)
    updated_by = Column(String(50), nullable=True)


class User(CommonBase):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    hashed_password = Column(String, nullable=False)
    logins = relationship("UserLogin", back_populates="user", lazy="select")

class UserLogin(CommonBase):
    __tablename__ = "users_logins"
    ip_address = Column(String(255), nullable=False)
    jwt_token = Column(String(500), nullable=False)
    refresh_token = Column(String(255), unique=True, nullable=True)
    refresh_token_expired_at = Column(DateTime(timezone=True), nullable=True)
    login_at = Column(DateTime(timezone=True), nullable=False)
    is_readonly = Column(Boolean, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    user = relationship("User", back_populates="logins", lazy="select")  # Many to One