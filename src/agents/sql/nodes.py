from dishka import AsyncContainer
from services.db import DBService
from agents.sql.state import SQLAgentState
from core.config import settings


def make_get_tables_node(container: AsyncContainer):
    async def get_tables_node(state: SQLAgentState) -> dict:
        db_service = await container.get(DBService)
        tables = await db_service.get_tables()

        return {"tables": tables}

    return get_tables_node


def make_get_schemas_node(container: AsyncContainer):
    async def get_schemas_node(state: SQLAgentState) -> dict:
        db_service = await container.get(DBService)

        schemas = await db_service.get_table_schemas(
            tables=[table.table_name for table in state.tables]
        )
        return {"schemas": schemas}

    return get_schemas_node


def make_generate_sql_node(llm):
    async def generate_sql_node(state: SQLAgentState) -> dict:
        prompt = f"""
        Ты — SQL-генератор.

        Входные данные:
        1. Схемы таблиц (строго для анализа):
        {state.schemas}

        2. Запрос пользователя (на естественном языке):
        {state.user_prompt}

        Требования к ответу:
        - Верни ТОЛЬКО SQL-запрос.
        - Ответ должен начинаться с ключевого слова SELECT.
        - Запрещены любые комментарии (--, /* */).
        - Запрещены пояснения, текст, markdown, кавычки, блоки кода.
        - Запрещены символы до и после SQL-запроса.
        - Один SQL-запрос, в одну строку.
        - Используй ТОЛЬКО таблицы и поля из предоставленных схем.

        Формат ответа:
        SELECT ...
        """

        response = await llm.ainvoke(prompt)

        return {"sql_query": response.content.strip()}

    return generate_sql_node


def make_execute_sql_node(container: AsyncContainer):
    async def execute_sql_node(state: SQLAgentState) -> dict:
        db_service = await container.get(DBService)

        result = await db_service.execute_sql(state.sql_query)

        return {"sql_result": result}

    return execute_sql_node


def check_sql_result_node(state: SQLAgentState) -> str:
    if state.sql_result.success:
        return "final"

    if state.attempts >= settings().MAX_ATTEMPTS:
        return "final"

    return "regenerate_sql"


def make_regenerate_sql_node(llm):
    async def regenerate_sql_node(state: SQLAgentState) -> dict:
        prompt = f"""
            Ты SQL-генератор.
            
            Предыдущий SQL-запрос:
            {state.sql_query}
            
            Ошибка выполнения SQL:
            {state.sql_result.error}
            
            Схемы таблиц:
            {state.schemas}
            
            Запрос пользователя:
            {state.user_prompt}
            
            Исправь SQL-запрос.
            Верни ТОЛЬКО исправленный SQL-запрос.
            Без комментариев, markdown и пояснений.
            """

        response = await llm.ainvoke(prompt)

        return {
            "sql_query": response.content.strip(),
            "attempts": state.attempts + 1,
        }

    return regenerate_sql_node
