from fastapi import APIRouter, Depends, File, UploadFile, status

from services.upload import UploadService

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("/dump", status_code=status.HTTP_200_OK)
async def upload_districts(
    dump: UploadFile = File(...), upload_service: UploadService = Depends()
) -> None:
    await upload_service.upload_dump(dump=dump)
