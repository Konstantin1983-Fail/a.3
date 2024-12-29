from fastapi import FastAPI
from app.routers.user import router as user_router  # Импортируем маршруты для пользователей

# Создаем экземпляр FastAPI
app = FastAPI()

# Подключаем маршруты для пользователей
app.include_router(user_router)

# Маршрут для главной страницы
@app.get("/")
def root():
    """
    Главная страница API.
    Возвращает приветственное сообщение.
    """
    return {"message": "Welcome to the User API"}