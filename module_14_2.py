import sqlite3

# Подключаемся к базе данных
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Удаляем запись с id=6
cursor.execute('DELETE FROM Users WHERE id = 6')
print("Запись с ID 6 удалена.")

# Подсчитываем количество пользователей
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]
print(f"Количество пользователей: {total_users}")

# Подсчитываем сумму всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]
print(f"Сумма всех балансов: {all_balances}")

# Выводим средний баланс
if total_users > 0:
    average_balance = all_balances / total_users
    print(f"Средний баланс: {average_balance}")
else:
    print("Средний баланс не может быть рассчитан, так как пользователей нет.")

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
print("База данных обновлена и сохранена.")
