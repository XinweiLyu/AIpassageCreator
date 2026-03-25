"""密码工具。"""

from passlib.context import CryptContext

from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(raw_password: str) -> str:
    return pwd_context.hash(f"{raw_password}{settings.password_salt}")


def verify_password(raw_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(f"{raw_password}{settings.password_salt}", hashed_password)
