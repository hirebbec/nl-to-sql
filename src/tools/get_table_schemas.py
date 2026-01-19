from typing import Sequence

from dishka import AsyncContainer
from langchain_core.tools import tool
from schemas.table import FullTableSchema
from services.db import DBService


def make_get_table_schemas_tool(container: AsyncContainer):
    @tool
    async def get_table_schemas(tables: list[str]) -> Sequence[FullTableSchema]:
        """
        Возвращает схему (DDL / структуру) указанных таблиц базы данных.

        Используй этот инструмент, когда тебе нужно узнать:
        - какие колонки есть в таблице
        - типы данных колонок
        - первичные и внешние ключи
        - структуру таблицы перед построением SQL-запроса

        Перед использованием этого инструмента убедись,
        что таблицы существуют (например, с помощью get_tables).

        Аргументы:
        - tables: список названий таблиц

        Возвращает:
        - список объектов, где каждый объект описывает одну таблицу
          (имя таблицы, колонки, ключи и связи)
        """
        db_service = await container.get(DBService)
        return await db_service.get_table_schemas(tables=tables)

    return get_table_schemas
