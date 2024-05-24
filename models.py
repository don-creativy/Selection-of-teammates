from peewee import Model, SqliteDatabase, CharField # type: ignore
from states.anketa import *
# Создаем подключение к базе данных SQLite
db = SqliteDatabase('sqlite.db')


# Создаем таблицы в базе данных


# Добавляем данные в таблицу
new_user = Anketa(game='jjjj')
new_user.save()

# Запросы к базе данных
all_users = Anketa.select()
for user in all_users:
    print(user.game)

db.connect()
db.create_tables([Anketa], save=True)
db.close()