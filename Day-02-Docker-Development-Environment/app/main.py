from fastapi import FastAPI

app = FastAPI(
    title="Docker Demo API",
    description="A minimal FastAPI service packaged with Docker for the Day 02 task.",
    version="1.0.0",
)

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
