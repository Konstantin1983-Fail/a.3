# app/backend/main.py
from fastapi import FastAPI
from app.backend.routers import task, user
from app.backend.db import engine, Base
from sqlalchemy.schema import CreateTable
from app.backend.models.user import User
from app.backend.models.task import Task

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)

# Выводим SQL для таблицы User
print("SQL для User:")
print(CreateTable(User.__table__).compile(engine))

# Выводим SQL для таблицы Task
print("\nSQL для Task:")
print(CreateTable(Task.__table__).compile(engine))


