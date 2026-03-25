"""用户业务逻辑。"""

from app.schemas.user import UserCreateRequest, UserResponse


def create_user(payload: UserCreateRequest) -> UserResponse:
    return UserResponse(id=1, username=payload.username)
