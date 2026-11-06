from fastapi import FastAPI
from app.api.v2.endpoints.users import router as users_router

app = FastAPI(
    title="DemoAPI — Day 04 Pydantic V2 Users API",
    description="Users API using Pydantic V2 request and response models.",
    version="2.0.0",
)

app.include_router(users_router)

@app.get("/", tags=["General"])
def root():
    return {"message": "Day 04 Pydantic V2 API is running", "docs": "/docs"}

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
