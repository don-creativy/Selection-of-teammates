from aiogram import Dispatcher
from aiogram.types import Message


async def cmd_start(message: Message):
    await message.answer("Привет!")


async def unknown(message: Message):
    await message.answer(f"{message.text} сам такой!")

def req_handler(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])

    dp.register_message_handler(unknown)