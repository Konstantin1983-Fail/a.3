import sqlite3

# Подключаемся к базе данных
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Создаём таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')
print("Таблица создана.")

# Заполняем таблицу 10 записями
users = [
    (f"User{i}", f"example{i}@gmail.com", i * 10, 1000) for i in range(1, 11)
]
cursor.executemany('''
INSERT INTO Users (username, email, age, balance)
VALUES (?, ?, ?, ?)
''', users)
print("10 записей добавлены.")

# Обновляем баланс у каждой 2-й записи
cursor.execute('''
UPDATE Users
SET balance = 500
WHERE id % 2 = 1
''')
print("Баланс обновлён у каждой 2-й записи.")

# Удаляем каждую 3-ю запись
cursor.execute('''
DELETE FROM Users
WHERE id % 3 = 0
''')
print("Каждая 3-я запись удалена.")

# Выбираем записи, где возраст не равен 60
cursor.execute('''
SELECT username, email, age, balance
FROM Users
WHERE age != 60
''')
results = cursor.fetchall()

# Выводим записи в консоль
for row in results:
    username, email, age, balance = row
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
print("База данных обновлена и сохранена.")
