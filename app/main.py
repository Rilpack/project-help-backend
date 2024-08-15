from fastapi import FastAPI
from .db import models
from .db.datebase import engine
from .api.v1.endpoints import questions, choices

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(questions.router, prefix="/api/v1")
app.include_router(choices.router, prefix="/api/v1")


@app.get("/")
def get_root():
    return {"Hello": "World"}
