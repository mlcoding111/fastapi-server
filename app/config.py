from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # App Configuration
    APP_NAME: str = "fastapi-server"

    # Database Configuration
    DATABASE_URL: str

    # Security Configuration
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRES_IN: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()