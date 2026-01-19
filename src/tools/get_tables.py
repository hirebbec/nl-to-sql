from dishka import AsyncContainer
from langchain_core.tools import tool
from services.db import DBService


def make_get_tables_tool(container: AsyncContainer):
    @tool
    async def get_tables() -> list[str]:
        """
        Возвращает список таблиц в БД.
        Используй перед построением SQL.
        """
        db_service = await container.get(DBService)
        tables = await db_service.get_tables()
        return [t.table_name for t in tables]

    return get_tables
