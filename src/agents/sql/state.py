from schemas.base import BaseSchema
from schemas.sql_result import SQLResultSchema
from schemas.table import FullTableSchema, TableSchema


class SQLAgentState(BaseSchema):
    user_prompt: str
    tables: list[TableSchema] = []
    schemas: list[FullTableSchema] = []
    sql_query: str = ""
    sql_result: SQLResultSchema | None = None
    attempts: int = 0
