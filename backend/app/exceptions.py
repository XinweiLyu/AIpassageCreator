"""统一异常和错误码。"""

from fastapi import HTTPException, status


class AppErrorCode:
    INTERNAL_ERROR = "INTERNAL_ERROR"
    USER_NOT_FOUND = "USER_NOT_FOUND"


def not_found(message: str = "资源不存在") -> HTTPException:
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)
