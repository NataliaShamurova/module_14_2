import sqlite3

connection = sqlite3.connect('not_telegram')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)

''')

cursor.execute(' CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
#cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)',
#cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)',
               #('User1', 'example1@gmail.com', '10', '1000'))

# for i in range(1,10):
#     cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)',
#                    (f'User{i}', f'example{i}@gmail.com', f'{i*10}', '1000'))

#Обновляем balance у каждой 2ой записи начиная с 1ой на 500:

cursor.execute('''
    UPDATE Users
    SET balance = 500
    WHERE id IN (
        SELECT id
        FROM Users
        WHERE id % 2 = 1
    )
''')

# #Удаляем каждую 3ую запись в таблице начиная с 1ой:
cursor.execute('''
    DELETE FROM Users
    WHERE id IN (
        SELECT id
        FROM Users
        WHERE id % 3 = 1
    )
''')

# Выбираем записи с условием возраста не равного 60

cursor.execute('''
    SELECT username, email, age, balance
    FROM Users
    WHERE age != ?''', (60,)
)

# Получаем все выбранные записи
rows = cursor.fetchall()

# Выводим результаты в требуемом формате
# for row in rows:
#     username, email, age, balance = row
#     print(f'Имя: {username} | Почта: {email} '
#           f'| Возраст: {age} | Баланс: {balance}')

#Удаление пользователя с id=6

cursor.execute('''DELETE FROM Users WHERE id = ?''', (6,))

# Подсчёт кол-ва всех пользователей

cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]
#print(total_users)

# Подсчёт суммы всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]
#print(all_balances)

print(all_balances / total_users)

connection.commit()
connection.close()