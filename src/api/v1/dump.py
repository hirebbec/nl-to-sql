from fastapi import APIRouter, Depends, File, UploadFile, status

from services.upload import DumpService

router = APIRouter(prefix="/dump", tags=["Upload"])


@router.post("/", status_code=status.HTTP_200_OK)
async def upload_dump(
    dump: UploadFile = File(...), dump_service: DumpService = Depends()
) -> None:
    await dump_service.upload_dump(dump=dump)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_dump(dump_service: DumpService = Depends()) -> None:
    return await dump_service.get_dump()


@router.delete("/", status_code=status.HTTP_200_OK)
async def delete_dump(dump_service: DumpService = Depends()) -> None:
    await dump_service.delete_dump()
