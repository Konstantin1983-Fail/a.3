# Импортируем APIRouter из FastAPI для создания маршрутов
from fastapi import APIRouter

# Создаём экземпляр APIRouter с настройками
router = APIRouter(
    prefix="/user",  # Префикс для всех маршрутов в этом роутере
    tags=["user"]    # Тег для группировки маршрутов в документации Swagger/OpenAPI
)

# Маршрут для получения всех пользователей
@router.get("/")
async def all_users():
    """
    Возвращает список всех пользователей.
    """
    pass

# Маршрут для получения пользователя по его ID
@router.get("/{user_id}")
async def user_by_id(user_id: int):
    """
    Возвращает пользователя по его уникальному идентификатору.

    Аргументы:
        user_id (int): Уникальный идентификатор пользователя.
    """
    pass

# Маршрут для создания нового пользователя
@router.post("/create")
async def create_user():
    """
    Создаёт нового пользователя.
    """
    pass

# Маршрут для обновления существующего пользователя
@router.put("/update")
async def update_user():
    """
    Обновляет существующего пользователя.
    """
    pass

# Маршрут для удаления пользователя
@router.delete("/delete")
async def delete_user():
    """
    Удаляет пользователя.
    """
    pass