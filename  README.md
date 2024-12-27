# Структура проекта

```plaintext
shop_project/
│
├── app/
│   ├── backend/
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── task.py
│   │   │   └── user.py
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   ├── task.py
│   │   │   └── user.py
│   │   ├── __init__.py
│   │   └── db.py
│   └── __init__.py
│
├── main.py  # Перемещённый файл
├── myenv/  # Виртуальное окружение
│
└── requirements.txt