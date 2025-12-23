from fastapi import Depends

from db.repository.schema import SchemaRepository
from services.base import BaseService


class UploadService(BaseService):
    def __init__(self, schema_repository: SchemaRepository = Depends()):
        self._schema_repository = schema_repository

    async def upload_dump(self, dump):
        ddl_statements = self._extract_ddl(dump)

        await self._schema_repository.clear_schema()

        for ddl in ddl_statements:
            await self._schema_repository.save_schema(ddl=ddl)

    def _extract_ddl(self, dump: str) -> list[str]:
        statements = []

        current = []
        for line in dump.splitlines():
            if line.strip().lower().startswith("create table"):
                current = [line]
            elif current:
                current.append(line)
                if line.strip().endswith(";"):
                    statements.append("\n".join(current))
                    current = []

        return statements
