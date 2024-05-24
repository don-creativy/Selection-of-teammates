from aiogram.fsm.state import State, StatesGroup
from peewee import Model, SqliteDatabase


class Anketa(StatesGroup):
    name = State()
    age = State()
    gender = State()
    game = State()

