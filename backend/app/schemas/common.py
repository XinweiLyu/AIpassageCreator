"""通用响应模型。"""

from pydantic import BaseModel


class BaseResponse(BaseModel):
    success: bool = True
    message: str = "ok"
