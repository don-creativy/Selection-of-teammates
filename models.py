from peewee import Model, SqliteDatabase, CharField # type: ignore
# Создаем подключение к базе данных SQLite
db = SqliteDatabase('sqlite.db')

class BaseModel(Model):
    class Meta:
        database = db

# Создаем таблицы в базе данных


# Добавляем данные в таблицу
class Anketa:
    name = ()
    age = ()
    gender = ()
    game = ()

db.connect()
db.create_tables([Anketa], save=True)
db.close()