"""Session 工具。"""

from datetime import datetime, timedelta, timezone

from app.config import settings


def get_session_expire_at() -> datetime:
    return datetime.now(timezone.utc) + timedelta(seconds=settings.session_max_age)
