from langchain_core.tools import tool
from core.container import container
from services.db import DBService


@tool
async def get_tables() -> list[str]:
    """
    Возвращает список таблиц в БД.
    Используй перед построением SQL.
    """
    db_service = container.get(DBService)
    tables = await db_service.get_tables()
    return [t.table_name for t in tables]
