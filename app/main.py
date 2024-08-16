from fastapi import FastAPI

from .db import models
from .db.datebase import engine

from .api_v1 import router as router_v1

app = FastAPI()
app.include_router(router=router_v1)
models.Base.metadata.create_all(bind=engine)


@app.get("/")
def get_root():
    return {"Hello": "World"}
