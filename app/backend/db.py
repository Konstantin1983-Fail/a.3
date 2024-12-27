# Импортируем необходимые компоненты из SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаем движок для подключения к базе данных SQLite
# DATABASE_URL указывает на файл базы данных SQLite (taskmanager.db в текущей директории)
DATABASE_URL = "sqlite:///taskmanager.db"

# Создаем движок (engine) для работы с базой данных
# echo=True включает вывод всех SQL-запросов в консоль (удобно для отладки)
engine = create_engine(DATABASE_URL, echo=True)

# Создаем базовый класс для всех моделей
# declarative_base() возвращает класс, который будет использоваться для создания моделей
Base = declarative_base()

# Создаем фабрику для сессий (SessionLocal)
# Сессии используются для взаимодействия с базой данных
# autocommit=False: Автоматическое подтверждение изменений отключено
# autoflush=False: Автоматическая синхронизация изменений с базой данных отключена
# bind=engine: Привязываем сессии к созданному движку
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)