import functools
from datetime import timezone, timedelta
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    root_dir: Path = Path(__file__).resolve().parent.parent
    env_file: Path = root_dir.joinpath(".env.local")

    PROJECT_NAME: str = "nl-to-sql"

    USE_CORS_MIDDLEWARE: bool = True
    USE_TIMER_MIDDLEWARE: bool = True

    API_KEY: str = "api_key"

    TEMPERATURE: float = 0.0
    MAX_TOKENS: int = 512

    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 11900
    SERVER_WORKERS_COUNT: int = 5

    ENVIRONMENT: str = "local"
    TIME_ZONE: timezone = timezone(offset=timedelta(hours=+3))
    CORS_ALLOW_ORIGIN_LIST: str = "*"



    POSTGRES_HOST: str = "nl-to-sql-db"
    POSTGRES_PORT: int = 5932
    POSTGRES_USER: str = "nl-to-sql-db"
    POSTGRES_PASSWORD: str = "nl-to-sql-db"
    POSTGRES_DB: str = "nl-to-sql-db"

    @functools.cached_property
    def postgres_dsn(self) -> str:
        postgres_host = (
            "localhost" if self.ENVIRONMENT == "local" else self.POSTGRES_HOST
        )
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{postgres_host}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    model_config = SettingsConfigDict(
        env_file=env_file if env_file else None,
        env_file_encoding="utf-8",
        extra="allow",
    )


@functools.lru_cache()
def settings() -> Settings:
    return Settings()
