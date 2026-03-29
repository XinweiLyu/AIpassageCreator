"""依赖注入
后端里认证/鉴权依赖注入的核心文件，给 FastAPI 路由提供 当前用户是谁、是否已登录、是否管理员
"""

import uuid
from typing import Optional
from fastapi import Cookie, Depends, HTTPException, status

from app.exceptions import ErrorCode, BusinessException
from app.schemas.user import LoginUserVO
from app.utils.session import get_session


async def get_session_id(session_id: Optional[str] = Cookie(None, alias="SESSION")) -> Optional[str]:
    """从 Cookie 中获取 Session ID"""
    return session_id


async def get_current_user(
    session_id: Optional[str] = Depends(get_session_id)
) -> Optional[LoginUserVO]:
    """获取当前登录用户（可选）"""
    if not session_id:
        return None
    
    session_data = await get_session(session_id)
    # 如果 session_data 为空或者 里面没有 user 字段，返回 None
    if not session_data or "user" not in session_data:
        return None
    
    user_data = session_data["user"]
    # 将 user_data 转换为 LoginUserVO 对象.
    return LoginUserVO(**user_data) # ** 是解包操作符, 将 user_data 中的键值对解包为 LoginUserVO 对象的属性.


async def require_login(
    current_user: Optional[LoginUserVO] = Depends(get_current_user)
) -> LoginUserVO:
    """要求必须登录"""
    if not current_user:
        raise BusinessException(ErrorCode.NOT_LOGIN_ERROR)
    return current_user


async def require_admin(
    current_user: LoginUserVO = Depends(require_login)
) -> LoginUserVO:
    """要求必须是管理员"""
    if current_user.user_role != "admin":
        raise BusinessException(ErrorCode.NO_AUTH_ERROR)
    return current_user


def generate_session_id() -> str:
    """生成 Session ID"""
    return str(uuid.uuid4()) # uuid.uuid4() 是生成一个随机的 UUID 对象. 
