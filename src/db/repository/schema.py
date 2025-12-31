from collections import defaultdict
from typing import Sequence

from sqlalchemy import text, select

from db.columns_table import columns_table
from db.repository.base import BaseDatabaseRepository
from schemas.column import ColumnSchema
from schemas.table import TableSchema, FullTableSchema


class Repository(BaseDatabaseRepository):
    async def get_tables(self) -> Sequence[TableSchema]:
        query = text("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
              AND table_type = 'BASE TABLE'
            ORDER BY table_name
        """)

        result = await self._session.execute(query)
        rows = result.fetchall()

        return [TableSchema(name=row[0]) for row in rows]

    async def get_columns_by_tables(
        self,
        tables: list[str],
    ) -> Sequence[FullTableSchema]:
        data: dict[str, list[ColumnSchema]] = defaultdict(list)

        stmt = (
            select(
                columns_table.c.table_name,
                columns_table.c.column_name,
                columns_table.c.data_type,
            )
            .where(
                columns_table.c.table_name.in_(tables),
            )
            .order_by(
                columns_table.c.table_name,
            )
        )

        result = await self._session.execute(stmt)

        for row in result.all():
            data[row[0]].append(ColumnSchema(name=row[1], type=row[2]))

        return [
            FullTableSchema(name=name, columns=columns)
            for name, columns in data.items()
        ]

    async def clear_db(self) -> None:
        tables = await self.get_tables()

        if not tables:
            return

        for table in tables:
            await self._session.execute(text(f'DROP TABLE IF EXISTS "{table}" CASCADE'))

        await self._session.commit()
