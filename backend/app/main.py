"""应用入口。"""

from fastapi import FastAPI

from app.routers.health import router as health_router
from app.routers.user import router as user_router

app = FastAPI(title="AI Passage Creator Backend")
app.include_router(health_router)
app.include_router(user_router)
