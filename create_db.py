from app.db.session import engine, Base
from app.models.user import User

# Создаем таблицы в базе данных
Base.metadata.create_all(bind=engine)