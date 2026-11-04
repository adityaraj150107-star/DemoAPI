from fastapi import FastAPI
from app.api.v1.endpoints.users import router as users_router

app = FastAPI(
    title="DemoAPI - Docker + FastAPI CRUD",
    description="Health check and Users CRUD API",
    version="1.0.0"
)

app.include_router(users_router)


@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}
