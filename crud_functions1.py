import sqlite3


# Эта функция должна создавать таблицу
def initiate_db():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL DEFAULT 1000
        )
    ''')

    connection.commit()
    connection.close()


# Добавление данных в таблицу Products
def add_products():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    products = [
        ('Product1', 100),
        ('Product2', 200),
        ('Product3', 300),
        ('Product4', 400)
    ]

    cursor.executemany('''
        INSERT INTO Products (name, price) VALUES (?, ?)
    ''', products)

    connection.commit()
    connection.close()


# Эта функция добавляет нового пользователя в таблицу
def add_user(username, email, age):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO Users (username, email, age, balance) 
        VALUES (?, ?, ?, ?)
    ''', (username, email, age, 1000))

    connection.commit()
    connection.close()


# Эта функция проверяет, существует ли пользователь с таким именем в базе данных.
def is_included(username):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('SELECT id FROM Users WHERE username = ?', (username,))
    user = cursor.fetchone()

    connection.close()

    return user is not None
