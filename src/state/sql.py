from typing import TypedDict


class SQLState(TypedDict):
    question: str
    ddl: str
    sql: [str] | None
