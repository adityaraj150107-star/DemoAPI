from fastapi import FastAPI

app = FastAPI(title="Demo Health API")


@app.get("/health")
def health_check():
    return {"status": "ok"}
