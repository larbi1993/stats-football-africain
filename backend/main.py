from fastapi import FastAPI
from app.api.v1.router import api_router
from app.core.config import PROJECT_NAME, API_V1_PREFIX

app = FastAPI(title=PROJECT_NAME)
 
@app.get("/a")
def root() :
    return {"test 1" : "réussi"}

app.include_router(api_router, prefix=API_V1_PREFIX)