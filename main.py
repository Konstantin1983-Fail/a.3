# Импортируем FastAPI для создания приложения
from fastapi import FastAPI

# Импортируем роутеры для задач и пользователей
from app.backend.routers import task, user

# Импортируем движок и базовый класс для моделей из модуля базы данных
from app.backend.db import engine, Base

# Импортируем CreateTable для генерации SQL-запросов создания таблиц
from sqlalchemy.schema import CreateTable

# Импортируем модели User и Task
from app.backend.models.user import User
from app.backend.models.task import Task

# Создаем экземпляр FastAPI приложения
app = FastAPI()

# Маршрут для корневой страницы
@app.get("/")
async def welcome():
    """
    Возвращает приветственное сообщение.
    """
    return {"message": "Welcome to Taskmanager"}

# Подключаем роутеры для задач и пользователей
app.include_router(task.router)  # Подключаем роутер для задач
app.include_router(user.router)  # Подключаем роутер для пользователей

# Генерируем и выводим SQL-запрос для создания таблицы User
print("SQL для User:")
print(CreateTable(User.__table__).compile(engine))

# Генерируем и выводим SQL-запрос для создания таблицы Task
print("\nSQL для Task:")
print(CreateTable(Task.__table__).compile(engine))