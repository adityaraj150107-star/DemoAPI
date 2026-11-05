"""Application entry point for DemoAPI."""
from fastapi import FastAPI

from app.api.v1.endpoints.users import router as users_v1_router
from app.api.v2.endpoints.users import router as users_v2_router

app = FastAPI(
    title="DemoAPI | Versioned Users API",
    description="A learning project demonstrating FastAPI, Pydantic v2, API versioning, and Docker.",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(users_v1_router)
app.include_router(users_v2_router)


@app.get("/", tags=["General"])
async def root():
    return {
        "message": "DemoAPI is running",
        "docs": "/docs",
        "health": "/health",
        "api_versions": {
            "v1": "/api/v1",
            "v2": "/api/v2/users",
        },
    }


@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}
