from typing import Sequence

from fastapi import APIRouter, Depends, File, UploadFile, status

from schemas.table import TableSchema, FullTableSchema
from services.upload import DBService

router = APIRouter(prefix="/dump", tags=["Upload"])


@router.post("/", status_code=status.HTTP_200_OK)
async def upload_dump(
    dump: UploadFile = File(...), db_service: DBService = Depends()
) -> None:
    await db_service.upload_dump(dump=dump)


@router.get(
    "/tables", status_code=status.HTTP_200_OK, response_model=Sequence[TableSchema]
)
async def get_tables(db_service: DBService = Depends()) -> Sequence[TableSchema]:
    return await db_service.get_tables()


@router.post(
    "/ddl", status_code=status.HTTP_200_OK, response_model=Sequence[FullTableSchema]
)
async def get_ddl_by_tables(
    tables: list[str], db_service: DBService = Depends()
) -> Sequence[FullTableSchema]:
    return await db_service.get_ddl_by_tables(tables=tables)


@router.delete("/", status_code=status.HTTP_200_OK)
async def clear_db(db_service: DBService = Depends()) -> None:
    await db_service.clear_db()
