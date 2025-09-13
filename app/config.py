from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # App Configuration
    APP_NAME: str = "fastapi-server"

    # Database Configuration
    DATABASE_URL: str

    # Security Configuration
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRES_IN: int

settings = Settings()

@lru_cache()
def get_settings():
    return settings