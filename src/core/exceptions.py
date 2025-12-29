from fastapi import HTTPException, status

dump_upload_exception = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Failed to upload dump",
)
