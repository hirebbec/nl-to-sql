from sqlalchemy import text

from db.repository.base import BaseDatabaseRepository


class SchemaRepository(BaseDatabaseRepository):
    async def save_schema(self, ddl: str) -> None:
        query = text(
            """
            INSERT INTO db_schema (ddl)
            VALUES (:ddl)
            """
        )
        await self._session.execute(query, {"ddl": ddl})
        await self._session.commit()

    async def clear_schema(self) -> None:
        await self._session.execute(text("DELETE FROM db_schema"))
        await self._session.commit()