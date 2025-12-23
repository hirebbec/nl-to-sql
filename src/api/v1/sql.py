from fastapi import APIRouter, Depends, status

from services.sql import SqlService

router = APIRouter(prefix="/sql", tags=["SQL"])


@router.post("/", status_code=status.HTTP_200_OK)
async def generate_sql(prompt: str, sql_service: SqlService = Depends()) -> None:
    await sql_service.generate_sql(prompt=prompt)
