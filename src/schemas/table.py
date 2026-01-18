from schemas.base import BaseSchema
from schemas.column import ColumnSchema


class TableSchema(BaseSchema):
    table_name: str


class FullTableSchema(TableSchema):
    columns: list[ColumnSchema]
