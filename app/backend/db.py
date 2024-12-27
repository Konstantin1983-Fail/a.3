# app/backend/db.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаем движок для SQLite
DATABASE_URL = "sqlite:///taskmanager.db"
engine = create_engine(DATABASE_URL, echo=True)  # echo=True выводит SQL в консоль

# Создаем базовый класс для моделей
Base = declarative_base()

# Создаем фабрику для сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
