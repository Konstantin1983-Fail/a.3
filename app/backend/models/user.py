# Импортируем необходимые компоненты из SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.backend.db import Base  # Импортируем базовый класс для моделей

# Определяем класс User, который представляет таблицу в базе данных
class User(Base):
    __tablename__ = 'users'  # Указываем имя таблицы в базе данных

    # Определяем колонки таблицы
    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор пользователя (первичный ключ)
    username = Column(String, index=True)  # Имя пользователя (с индексацией для быстрого поиска)
    firstname = Column(String, index=True)  # Имя пользователя (с индексацией для быстрого поиска)
    lastname = Column(String, index=True)  # Фамилия пользователя (с индексацией для быстрого поиска)
    age = Column(Integer, index=True)  # Возраст пользователя (с индексацией для быстрого поиска)
    slug = Column(String, unique=True, index=True)  # Уникальный идентификатор пользователя для URL (с индексацией)

    # Определяем отношение "один ко многим" с таблицей задач
    tasks = relationship("Task", back_populates="user")  # Связь с моделью Task, обратное отношение через поле user