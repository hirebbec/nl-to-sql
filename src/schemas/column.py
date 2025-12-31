from schemas.base import BaseSchema


class ColumnSchema(BaseSchema):
    name: str
    type: str
