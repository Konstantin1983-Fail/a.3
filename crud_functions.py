import sqlite3


def initiate_db():
    """Инициализирует базу данных и таблицу Products."""
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        price INTEGER NOT NULL,
        image_path TEXT NOT NULL,
        category TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()


# Функция для добавления тестовых данных
def add_test_data():
    """Добавляет тестовые данные в таблицу."""
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    # Пример тестовых продуктов с картинками
    test_data = [
        ("Яблоки", "Сочные красные яблоки", 120, "images_new/apples.jpg", "Фрукты"),
        ("Бананы", "Свежие бананы из Эквадора", 90, "images_new/bananas.jpg", "Фрукты"),
        ("Апельсины", "Сладкие апельсины", 150, "images_new/oranges.jpg", "Фрукты"),
        ("Виноград", "Кишмиш без косточек", 200, "images_new/grapes.jpg", "Фрукты")
    ]

    cursor.executemany('''
    INSERT INTO Products (title, description, price, image_path, category)
    VALUES (?, ?, ?, ?, ?)
    ''', test_data)

    conn.commit()
    conn.close()


# Функция для получения всех категорий
def get_all_categories():
    """Возвращает список всех категорий продуктов."""
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT category FROM Products")
    categories = cursor.fetchall()
    conn.close()
    return [category[0] for category in categories]


# Функция для получения продуктов по категории
def get_products_by_category(category):
    """Возвращает все продукты из заданной категории."""
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, description, price, image_path FROM Products WHERE category = ?", (category,))
    products = cursor.fetchall()
    conn.close()
    return products
