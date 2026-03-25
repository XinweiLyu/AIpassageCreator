"""用户相关路由。"""

from fastapi import APIRouter

from app.schemas.user import UserCreateRequest, UserResponse

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=UserResponse)
def create_user(payload: UserCreateRequest) -> UserResponse:
    return UserResponse(id=1, username=payload.username)
