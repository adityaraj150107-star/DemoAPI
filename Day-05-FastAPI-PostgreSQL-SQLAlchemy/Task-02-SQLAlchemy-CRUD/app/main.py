from fastapi import FastAPI

from .auth import router as auth_router
from .tasks import router as tasks_router
from .users import router as users_router


app = FastAPI(
    title="DemoAPI — Task Manager",
    description="PostgreSQL task management API with JWT authentication and teacher/student roles.",
    version="4.0.0",
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(tasks_router)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "version": "4.0.0"}
