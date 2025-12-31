import os
import subprocess
from typing import Sequence

from fastapi import Depends, UploadFile

from core.config import settings
from core.exceptions import (
    dump_upload_exception,
    incorrect_file_format_exception,
    database_is_not_empty_exception,
)
from db.repository.schema import Repository
from schemas.table import TableSchema, FullTableSchema
from services.base import BaseService


class DBService(BaseService):
    def __init__(self, repository: Repository = Depends()):
        self._repository = repository

    async def upload_dump(self, dump: UploadFile):
        if not dump.filename or not dump.filename.endswith(".sql"):
            raise incorrect_file_format_exception

        if self.get_tables():
            raise database_is_not_empty_exception

        try:
            dump_bytes = await dump.read()

            process = subprocess.run(
                [
                    "psql",
                    "-h",
                    str(settings().POSTGRES_HOST),
                    "-p",
                    str(settings().POSTGRES_PORT),
                    "-U",
                    str(settings().POSTGRES_USER),
                    "-d",
                    str(settings().POSTGRES_DB),
                    "--set",
                    "ON_ERROR_STOP=0",
                    "-v",
                    "ON_ERROR_ROLLBACK=on",
                ],
                input=dump_bytes,
                capture_output=True,
                env={
                    **os.environ,
                    "PGPASSWORD": str(settings().POSTGRES_PASSWORD),
                },
            )

            if process.returncode != 0:
                raise RuntimeError(process.stderr.decode())

        except Exception:
            raise dump_upload_exception

    async def get_tables(self) -> Sequence[TableSchema]:
        return await self._repository.get_tables()

    async def get_ddl_by_tables(
        self,
        tables: list[str],
    ) -> Sequence[FullTableSchema]:
        return await self._repository.get_columns_by_tables(tables=tables)

    async def clear_db(self):
        await self._repository.clear_db()
