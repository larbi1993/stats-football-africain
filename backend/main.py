from fastapi import FastAPI

from app.api.v1.router import api_router

app = FastAPI(title="Stats Football Africain API")
 
@app.get("/a")
def root() :
    return {"test 1" : "réussi"}

app.include_router(api_router, prefix="/api/v1")