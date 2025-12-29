import os
import subprocess

from fastapi import Depends, UploadFile

from core.config import settings
from core.exceptions import dump_upload_exception
from db.repository.schema import SchemaRepository
from services.base import BaseService


class DumpService(BaseService):
    def __init__(self, schema_repository: SchemaRepository = Depends()):
        self._schema_repository = schema_repository

    async def upload_dump(self, dump: UploadFile):
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

    async def get_dump(self):
        pass

    async def delete_dump(self):
        pass
