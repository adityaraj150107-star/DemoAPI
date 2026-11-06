from fastapi import FastAPI
from app.api.v1.endpoints.users import router as users_router

app = FastAPI(
    title="DemoAPI — Day 03 Users CRUD",
    description="Basic FastAPI Users CRUD operations using temporary in-memory storage.",
    version="1.0.0",
)

app.include_router(users_router)

@app.get("/", tags=["General"])
def root():
    return {"message": "Day 03 Users CRUD API is running", "docs": "/docs"}

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
