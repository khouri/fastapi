from enum import Enum
from pydantic import BaseModel
from typing import Annotated
from fastapi import FastAPI, Query

from todo import todo_router

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return({"message" : "Hello World"})


app.include_router(todo_router)
