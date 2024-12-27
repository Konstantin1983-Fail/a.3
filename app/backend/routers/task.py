# Импортируем APIRouter из FastAPI для создания маршрутов
from fastapi import APIRouter

# Создаём экземпляр APIRouter с настройками
router = APIRouter(
    prefix="/task",  # Префикс для всех маршрутов в этом роутере
    tags=["task"]    # Тег для группировки маршрутов в документации Swagger/OpenAPI
)

# Маршрут для получения всех задач
@router.get("/")
async def all_tasks():
    """
    Возвращает список всех задач.
    """
    pass

# Маршрут для получения задачи по её ID
@router.get("/{task_id}")
async def task_by_id(task_id: int):
    """
    Возвращает задачу по её уникальному идентификатору.

    Аргументы:
        task_id (int): Уникальный идентификатор задачи.
    """
    pass

# Маршрут для создания новой задачи
@router.post("/create")
async def create_task():
    """
    Создаёт новую задачу.
    """
    pass

# Маршрут для обновления существующей задачи
@router.put("/update")
async def update_task():
    """
    Обновляет существующую задачу.
    """
    pass

# Маршрут для удаления задачи
@router.delete("/delete")
async def delete_task():
    """
    Удаляет задачу.
    """
    pass