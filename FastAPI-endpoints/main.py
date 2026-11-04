from fastapi import FastAPI 
from api.v1.endpoints.users import router
import uvicorn as uv 

app = FastAPI(title = "Hospital Management API")
app.include_router(router)

if __name__ == "__main__" : 
    uv.run(app=app)