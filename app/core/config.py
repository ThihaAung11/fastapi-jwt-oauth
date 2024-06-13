import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


load_dotenv()

class Settings:
    PROJECT_NAME: str = "fastapi-jwt"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    SUPERUSER_NAME: str = 'admin'
    SUPERUSER_PASS: str = 'admin@1234'
    SUPERUSER_EMAIL: str = 'admin@gmail.com'

    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./test.db"     
    

settings = Settings()