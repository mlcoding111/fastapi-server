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

    # OpenAI Configuration
    OPENAI_API_KEY: str

    # OAuth Configuration
    GOOGLE_CLIENT_ID: str
    GOOGLE_SECRET: str
    GOOGLE_CALLBACK_URL: str

    # JWT Configuration
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int

settings = Settings()

@lru_cache()
def get_settings():
    return settings
