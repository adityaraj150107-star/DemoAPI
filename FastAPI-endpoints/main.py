from fastapi import FastAPI
import uvicorn
#from api.v1.endpoints import users as users_v1
from api.v2.endpoints import users as users_v2

app = FastAPI(
    title="Users Master API",
    version="1.0.0"
)

#app.include_router(
#    users_v1.router,
#    prefix="/api/v1"
#)

app.include_router(
    users_v2.router,
    prefix="/api/v2"
)


@app.get("/")
async def home():

    return {
        "message": "Users Master API is running",
        "version": {
            #"v1": "/api/v1/users",
            "v2": "/api/v2/users"
        }
    }

# Auto Run Server
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1",
                port=8000, reload=True)