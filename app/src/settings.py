from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:admin@postgres/currency_converter_db"
    API_KEY: str = "aa5b14f1fb6f4ce8c50c41c3"


settings = Settings()
