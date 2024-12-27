# Импортируем необходимые компоненты из SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.backend.db import Base  # Импортируем базовый класс для моделей

# Определяем класс Task, который представляет таблицу в базе данных
class Task(Base):
    __tablename__ = 'tasks'  # Указываем имя таблицы в базе данных

    # Определяем колонки таблицы
    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор задачи (первичный ключ)
    title = Column(String, index=True)  # Заголовок задачи (с индексацией для быстрого поиска)
    content = Column(String, index=True)  # Содержание задачи (с индексацией для быстрого поиска)
    priority = Column(Integer, default=0)  # Приоритет задачи (по умолчанию 0)
    completed = Column(Boolean, default=False)  # Статус выполнения задачи (по умолчанию False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)  # Внешний ключ для связи с пользователем
    slug = Column(String, unique=True, index=True)  # Уникальный идентификатор задачи для URL (с индексацией)

    # Определяем отношение "многие к одному" с таблицей пользователей
    user = relationship("User", back_populates="tasks")  # Связь с моделью User, обратное отношение через поле tasks