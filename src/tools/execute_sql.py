from dishka import AsyncContainer
from langchain_core.tools import tool
from schemas.sql_result import SQLResultSchema
from services.db import DBService


def make_execute_sql_tool(container: AsyncContainer):
    @tool
    async def execute_sql(sql: str) -> SQLResultSchema:
        """
        Выполняет SQL-запрос к базе данных.
        - Разрешены ТОЛЬКО SELECT-запросы.

        Аргументы:
        - sql: строка с SQL-запросом для выполнения.

        Возвращает:
        - success: true, если запрос выполнен успешно.
        - rows: список строк результата запроса (если success = true).
        - row_count: количество возвращённых строк.
        - error: текст ошибки (если success = false).

        ВАЖНО:
        - После успешного вызова этого инструмента агент ОБЯЗАН
          немедленно завершить работу и не вызывать другие инструменты.
        - Финальный ответ ДОЛЖЕН содержать ТОЛЬКО SQL-запрос
        Пример правильного финального ответа:
        SELECT COUNT(*) FROM table_name;
        - Если произошла ошибка, агент ОБЯЗАН завершить работу и вернуть текст ошибки.
        """
        db_service = await container.get(DBService)
        return await db_service.execute_sql(sql)

    return execute_sql
