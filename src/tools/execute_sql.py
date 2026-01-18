from langchain_core.tools import tool
from core.container import container
from schemas.sql_result import SQLResultSchema
from services.db import DBService


@tool
async def execute_sql(sql: str) -> SQLResultSchema:
    """
    Выполняет SQL-запрос к базе данных.
    Разрешены только SELECT-запросы
    Аргументы:
    - sql: SQL-запрос для выполнения

    Возвращает:
    - success: true, если запрос выполнен успешно
    - rows: список строк результата (если success=true)
    - row_count: количество строк
    - error: описание ошибки (если success=false)
    """
    db_service = container.get(DBService)
    return await db_service.execute_sql(sql)
