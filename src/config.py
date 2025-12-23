import functools
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    root_dir: Path = Path(__file__).resolve().parent.parent
    env_file: Path = root_dir.joinpath(".env.local")

    API_KEY: str = "MDE5YjQxNWQtYjIzNi03M2JkLWJmMjYtYmQzYzViNTQ3NjI5OmNhOGFmZmE2LTI4YTAtNDlmMS04NmViLWVhZjRkNzdiZWI4NA=="

    TEMPERATURE: float = 0.0
    MAX_TOKENS: int = 512

    ENVIRONMENT: str = "local"

    model_config = SettingsConfigDict(
        env_file=env_file if env_file else None,
        env_file_encoding="utf-8",
        extra="allow",
    )


@functools.lru_cache()
def settings() -> Settings:
    return Settings()
