from schemas.base import BaseSchema
from schemas.column import ColumnSchema


class TableSchema(BaseSchema):
    name: str


class FullTableSchema(TableSchema):
    columns: list[ColumnSchema]
