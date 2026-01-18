from typing import Any

from schemas.base import BaseSchema


class SQLResultSchema(BaseSchema):
    success: bool
    rows: list[dict[str, Any]] = []
    error: str | None = None
