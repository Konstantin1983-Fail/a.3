from sqlalchemy.orm import Session
from app.db.session import SessionLocal  # Импортируем фабрику сессий

def get_db():
    """
    Генератор для получения сессии базы данных.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()