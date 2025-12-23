from typing import TypedDict, Optional

class SQLState(TypedDict):
    question: str
    ddl: str
    sql: [str] | None