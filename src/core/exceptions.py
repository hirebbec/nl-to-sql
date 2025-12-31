from fastapi import HTTPException, status

incorrect_file_format_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Incorrect file format",
)

database_is_not_empty_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Database is not empty",
)

dump_upload_exception = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Failed to upload dump",
)
