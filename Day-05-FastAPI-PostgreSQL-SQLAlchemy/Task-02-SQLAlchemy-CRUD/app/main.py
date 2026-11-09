from contextlib import asynccontextmanager

from fastapi import FastAPI

from . import models
from .auth import router as auth_router
from .database import Base, engine
from .migrations import migrate_legacy_users
from .tasks import router as tasks_router
from .users import router as users_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    migrate_legacy_users()
    yield

app = FastAPI(
    title="DemoAPI — Task Manager",
    description="PostgreSQL task management API with JWT authentication and teacher/student roles.",
    version="4.0.0",
    lifespan=lifespan,
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(tasks_router)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "version": "4.0.0"}
