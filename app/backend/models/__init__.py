from .user import User
from .task import Task

"""
Модуль для модели пользователя (User).

Содержит определение таблицы `users` в базе данных:
- id: Уникальный идентификатор пользователя
- username: Логин пользователя
- firstname: Имя пользователя
- lastname: Фамилия пользователя
- age: Возраст пользователя
- slug: Уникальный идентификатор для URL
"""

"""
Модуль для модели задачи (Task).

Содержит определение таблицы `tasks` в базе данных:
- id: Уникальный идентификатор задачи
- title: Заголовок задачи
- content: Содержание задачи
- priority: Приоритет задачи
- completed: Статус выполнения задачи
- user_id: Внешний ключ для связи с пользователем
- slug: Уникальный идентификатор для URL
"""